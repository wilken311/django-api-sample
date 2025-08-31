from rest_framework import generics, viewsets, filters, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.db.models import Q, Avg
from .models import Author, Book, Review
from .serializers import (
    AuthorSerializer, BookSerializer, BookListSerializer, 
    ReviewSerializer, UserSerializer
)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing authors.
    Supports CRUD operations for authors.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

    @action(detail=True, methods=['get'])
    def books(self, request, pk=None):
        """Get all books by a specific author"""
        author = self.get_object()
        books = author.books.all()
        serializer = BookListSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing books.
    Supports CRUD operations, search, filtering, and custom actions.
    """
    queryset = Book.objects.select_related('author').prefetch_related('reviews')
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['genre', 'author', 'is_available']
    search_fields = ['title', 'author__name', 'description', 'isbn']
    ordering_fields = ['title', 'publication_date', 'price', 'created_at']
    ordering = ['-created_at']

    def get_serializer_class(self):
        """Use different serializers for list and detail views"""
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer

    @action(detail=False, methods=['get'])
    def by_genre(self, request):
        """Get books grouped by genre"""
        genre = request.query_params.get('genre')
        if not genre:
            return Response({'error': 'Genre parameter is required'}, 
                          status=status.HTTP_400_BAD_REQUEST)
        
        books = self.queryset.filter(genre=genre)
        serializer = BookListSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def popular(self, request):
        """Get popular books (highest rated)"""
        books = self.queryset.annotate(
            avg_rating=Avg('reviews__rating')
        ).filter(avg_rating__gte=4).order_by('-avg_rating')[:10]
        
        serializer = BookListSerializer(books, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        """Get all reviews for a specific book"""
        book = self.get_object()
        reviews = book.reviews.all()
        serializer = ReviewSerializer(reviews, many=True, context={'request': request})
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing book reviews.
    Users can only edit/delete their own reviews.
    """
    queryset = Review.objects.select_related('book', 'user')
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['book', 'rating']
    ordering_fields = ['rating', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter reviews based on query parameters"""
        queryset = super().get_queryset()
        
        # Filter by user's own reviews if requested
        if self.request.query_params.get('my_reviews') == 'true':
            queryset = queryset.filter(user=self.request.user)
        
        return queryset

    def perform_create(self, serializer):
        """Set the user to the current authenticated user"""
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """Only allow users to update their own reviews"""
        if serializer.instance.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You can only edit your own reviews.")
        serializer.save()

    def perform_destroy(self, instance):
        """Only allow users to delete their own reviews"""
        if instance.user != self.request.user:
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("You can only delete your own reviews.")
        instance.delete()


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    """Get current user's profile information"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def api_overview(request):
    """
    API Overview - List all available endpoints
    """
    endpoints = {
        'API Overview': '/api/',
        'Authors': {
            'List/Create': '/api/authors/',
            'Detail/Update/Delete': '/api/authors/{id}/',
            'Author Books': '/api/authors/{id}/books/',
        },
        'Books': {
            'List/Create': '/api/books/',
            'Detail/Update/Delete': '/api/books/{id}/',
            'By Genre': '/api/books/by_genre/?genre={genre}',
            'Popular Books': '/api/books/popular/',
            'Book Reviews': '/api/books/{id}/reviews/',
        },
        'Reviews': {
            'List/Create': '/api/reviews/',
            'Detail/Update/Delete': '/api/reviews/{id}/',
            'My Reviews': '/api/reviews/?my_reviews=true',
        },
        'User': {
            'Profile': '/api/user/profile/',
        },
        'Authentication': {
            'Login': '/api/auth/login/',
            'Logout': '/api/auth/logout/',
            'Token': '/api/auth/token/',
            'Browsable API': '/api-auth/login/',
        },
        'Browsable API Access': {
            'description': 'You can access the browsable API by going to /api-auth/login/ first to log in, then navigate to any endpoint.',
            'sample_endpoints_no_auth_needed': [
                '/api/overview/',
                '/api/books/',
                '/api/authors/',
                '/api/reviews/',
            ]
        }
    }
    return Response(endpoints)
