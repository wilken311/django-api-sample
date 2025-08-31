from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets
router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)

app_name = 'books'

urlpatterns = [
    path('', include(router.urls)),
    path('user/profile/', views.user_profile, name='user-profile'),
    path('overview/', views.api_overview, name='api-overview'),
]
