from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from books.models import Author, Book, Review
from datetime import date, datetime
from decimal import Decimal


class Command(BaseCommand):
    help = 'Populate the database with sample data for testing the API'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create sample users
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'bob_johnson', 'email': 'bob@example.com', 'first_name': 'Bob', 'last_name': 'Johnson'},
        ]

        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults=user_data
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(f'Created user: {user.username}')
            users.append(user)

        # Create sample authors
        authors_data = [
            {
                'name': 'J.K. Rowling',
                'email': 'jk.rowling@example.com',
                'bio': 'British author, best known for the Harry Potter series.',
                'birth_date': date(1965, 7, 31)
            },
            {
                'name': 'George Orwell',
                'email': 'g.orwell@example.com',
                'bio': 'English novelist and essayist, known for dystopian fiction.',
                'birth_date': date(1903, 6, 25)
            },
            {
                'name': 'Agatha Christie',
                'email': 'a.christie@example.com',
                'bio': 'English writer known for detective novels.',
                'birth_date': date(1890, 9, 15)
            },
            {
                'name': 'Isaac Asimov',
                'email': 'i.asimov@example.com',
                'bio': 'American science fiction writer and professor.',
                'birth_date': date(1920, 1, 2)
            }
        ]

        authors = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(
                email=author_data['email'],
                defaults=author_data
            )
            if created:
                self.stdout.write(f'Created author: {author.name}')
            authors.append(author)

        # Create sample books
        books_data = [
            {
                'title': 'Harry Potter and the Philosopher\'s Stone',
                'author': authors[0],  # J.K. Rowling
                'isbn': '9780747532699',
                'publication_date': date(1997, 6, 26),
                'pages': 223,
                'genre': 'fiction',
                'description': 'The first book in the Harry Potter series.',
                'price': Decimal('15.99'),
                'is_available': True
            },
            {
                'title': '1984',
                'author': authors[1],  # George Orwell
                'isbn': '9780451524935',
                'publication_date': date(1949, 6, 8),
                'pages': 328,
                'genre': 'sci_fi',
                'description': 'A dystopian social science fiction novel.',
                'price': Decimal('12.99'),
                'is_available': True
            },
            {
                'title': 'Murder on the Orient Express',
                'author': authors[2],  # Agatha Christie
                'isbn': '9780062693662',
                'publication_date': date(1934, 1, 1),
                'pages': 256,
                'genre': 'mystery',
                'description': 'A detective novel featuring Hercule Poirot.',
                'price': Decimal('13.49'),
                'is_available': True
            },
            {
                'title': 'Foundation',
                'author': authors[3],  # Isaac Asimov
                'isbn': '9780553293357',
                'publication_date': date(1951, 5, 1),
                'pages': 244,
                'genre': 'sci_fi',
                'description': 'The first novel in the Foundation series.',
                'price': Decimal('14.99'),
                'is_available': True
            },
            {
                'title': 'Animal Farm',
                'author': authors[1],  # George Orwell
                'isbn': '9780451526342',
                'publication_date': date(1945, 8, 17),
                'pages': 112,
                'genre': 'fiction',
                'description': 'An allegorical novella about farm animals.',
                'price': Decimal('10.99'),
                'is_available': False
            }
        ]

        books = []
        for book_data in books_data:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults=book_data
            )
            if created:
                self.stdout.write(f'Created book: {book.title}')
            books.append(book)

        # Create sample reviews
        reviews_data = [
            {'book': books[0], 'user': users[0], 'rating': 5, 'comment': 'Amazing book! Loved every page.'},
            {'book': books[0], 'user': users[1], 'rating': 4, 'comment': 'Great start to the series.'},
            {'book': books[1], 'user': users[0], 'rating': 5, 'comment': 'Thought-provoking and relevant.'},
            {'book': books[1], 'user': users[2], 'rating': 4, 'comment': 'Classic dystopian novel.'},
            {'book': books[2], 'user': users[1], 'rating': 4, 'comment': 'Great mystery with a twist.'},
            {'book': books[3], 'user': users[2], 'rating': 5, 'comment': 'Excellent science fiction.'},
        ]

        for review_data in reviews_data:
            review, created = Review.objects.get_or_create(
                book=review_data['book'],
                user=review_data['user'],
                defaults=review_data
            )
            if created:
                self.stdout.write(f'Created review for {review.book.title} by {review.user.username}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write('Users created (password: password123):')
        for user in users:
            self.stdout.write(f'  - {user.username} ({user.email})')
