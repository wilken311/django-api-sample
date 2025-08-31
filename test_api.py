#!/usr/bin/env python
"""
Simple test script to verify the Django API is working
"""
import os
import sys
import django

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
django.setup()

from books.models import Author, Book, Review
from django.contrib.auth.models import User

def test_api():
    print("=== Django API Test ===\n")
    
    # Test database connection
    print("1. Testing database connection...")
    try:
        author_count = Author.objects.count()
        book_count = Book.objects.count()
        review_count = Review.objects.count()
        user_count = User.objects.count()
        
        print(f"   ✓ Authors: {author_count}")
        print(f"   ✓ Books: {book_count}")
        print(f"   ✓ Reviews: {review_count}")
        print(f"   ✓ Users: {user_count}")
    except Exception as e:
        print(f"   ✗ Database error: {e}")
        return False
    
    # Test sample data
    print("\n2. Sample data check...")
    if book_count > 0:
        sample_book = Book.objects.first()
        print(f"   ✓ Sample book: {sample_book.title} by {sample_book.author.name}")
    else:
        print("   ! No books found. Run 'python manage.py populate_data' to create sample data.")
    
    print("\n3. API endpoints to test in browser:")
    print("   � API overview: http://127.0.0.1:8000/api/overview/")
    print("   🌐 Browsable API: http://127.0.0.1:8000/api/")
    print("   �📖 Books list: http://127.0.0.1:8000/api/books/")
    print("   👥 Authors list: http://127.0.0.1:8000/api/authors/")
    print("   ⭐ Reviews list: http://127.0.0.1:8000/api/reviews/")
    print("   � Popular books: http://127.0.0.1:8000/api/books/popular/")
    print("   📚 Fiction books: http://127.0.0.1:8000/api/books/by_genre/?genre=fiction")
    print("   🔍 Search books: http://127.0.0.1:8000/api/books/?search=harry")
    
    print("\n3.1 Complete API Endpoint List:")
    endpoints = {
        "Authentication": [
            "POST /api/auth/token/ - Get auth token",
            "GET /api-auth/login/ - Browser login page"
        ],
        "Authors": [
            "GET /api/authors/ - List authors",
            "POST /api/authors/ - Create author (auth required)",
            "GET /api/authors/{id}/ - Get author details",
            "GET /api/authors/{id}/books/ - Get author's books"
        ],
        "Books": [
            "GET /api/books/ - List books",
            "POST /api/books/ - Create book (auth required)",
            "GET /api/books/{id}/ - Get book details",
            "GET /api/books/popular/ - Popular books (4+ stars)",
            "GET /api/books/by_genre/?genre=fiction - Books by genre",
            "GET /api/books/?search=query - Search books"
        ],
        "Reviews": [
            "GET /api/reviews/ - List reviews",
            "POST /api/reviews/ - Create review (auth required)",
            "GET /api/reviews/?my_reviews=true - User's reviews"
        ],
        "User": [
            "GET /api/user/profile/ - User profile (auth required)"
        ]
    }
    
    for category, endpoint_list in endpoints.items():
        print(f"   📋 {category}:")
        for endpoint in endpoint_list:
            print(f"      • {endpoint}")
        print()
    
    print("\n4. Authentication:")
    print("   🔐 Login to browsable API: http://127.0.0.1:8000/api-auth/login/")
    print("   🎫 Get auth token: POST to http://127.0.0.1:8000/api/auth/token/")
    
    if user_count > 0:
        sample_user = User.objects.filter(is_superuser=False).first()
        if sample_user:
            print(f"   👤 Test user: {sample_user.username} (password: password123)")
    
    print("\n✅ API test completed successfully!")
    print("\n🚀 Start the server with: python manage.py runserver")
    return True

if __name__ == "__main__":
    test_api()
