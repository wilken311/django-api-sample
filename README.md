# Django REST API - Books Management System

A comprehensive Django REST API for managing books, authors, and reviews. This project demonstrates a complete API-only Django application using Django REST Framework.

## Features

- **Authors Management**: CRUD operations for authors
- **Books Management**: CRUD operations for books with advanced filtering
- **Reviews System**: User reviews and ratings for books
- **Authentication**: Token-based authentication
- **Search & Filtering**: Advanced search and filtering capabilities
- **Pagination**: Built-in pagination for large datasets
- **CORS Support**: Cross-origin resource sharing for frontend integration

## API Endpoints

### Authentication
- `POST /api/auth/token/` - Get authentication token
- `GET /api-auth/` - Django REST Framework browsable API authentication

### Authors
- `GET /api/authors/` - List all authors
- `POST /api/authors/` - Create new author
- `GET /api/authors/{id}/` - Get author details
- `PUT /api/authors/{id}/` - Update author
- `DELETE /api/authors/{id}/` - Delete author
- `GET /api/authors/{id}/books/` - Get books by author

### Books
- `GET /api/books/` - List all books
- `POST /api/books/` - Create new book
- `GET /api/books/{id}/` - Get book details
- `PUT /api/books/{id}/` - Update book
- `DELETE /api/books/{id}/` - Delete book
- `GET /api/books/by_genre/?genre={genre}` - Get books by genre
- `GET /api/books/popular/` - Get popular books (highest rated)
- `GET /api/books/{id}/reviews/` - Get reviews for a book

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review (own reviews only)
- `DELETE /api/reviews/{id}/` - Delete review (own reviews only)
- `GET /api/reviews/?my_reviews=true` - Get current user's reviews

### User
- `GET /api/user/profile/` - Get current user profile

## Setup Instructions

### 1. Clone and Setup Environment

```bash
# Navigate to project directory
cd c:\TheSourcecode\python\api

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data
python manage.py populate_data
```

### 3. Run the Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## Sample Data

The `populate_data` management command creates:

- **3 sample users** (password: `password123`)
  - john_doe (john@example.com)
  - jane_smith (jane@example.com)
  - bob_johnson (bob@example.com)

- **4 sample authors**
  - J.K. Rowling
  - George Orwell
  - Agatha Christie
  - Isaac Asimov

- **5 sample books** with various genres
- **6 sample reviews** with different ratings

## API Usage Examples

### Get Authentication Token

```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "john_doe", "password": "password123"}'
```

### List Books with Authentication

```bash
curl -X GET http://127.0.0.1:8000/api/books/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Search Books

```bash
# Search by title or author
curl -X GET "http://127.0.0.1:8000/api/books/?search=harry"

# Filter by genre
curl -X GET "http://127.0.0.1:8000/api/books/?genre=fiction"

# Get popular books
curl -X GET "http://127.0.0.1:8000/api/books/popular/"
```

### Create a Review

```bash
curl -X POST http://127.0.0.1:8000/api/reviews/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"book": 1, "rating": 5, "comment": "Excellent book!"}'
```

## API Features

### Filtering and Search
- **Books**: Filter by genre, author, availability; search by title, author name, description, ISBN
- **Authors**: Search by name, email
- **Reviews**: Filter by book, rating; get user's own reviews

### Permissions
- **Read access**: Available to all authenticated users
- **Write access**: Authenticated users can create content
- **Review management**: Users can only edit/delete their own reviews

### Pagination
- Default page size: 20 items
- Use `?page=2` to navigate pages

### Response Format
All responses are in JSON format. Example book response:

```json
{
  "id": 1,
  "title": "Harry Potter and the Philosopher's Stone",
  "author": 1,
  "author_name": "J.K. Rowling",
  "isbn": "9780747532699",
  "publication_date": "1997-06-26",
  "pages": 223,
  "genre": "fiction",
  "description": "The first book in the Harry Potter series.",
  "price": "15.99",
  "is_available": true,
  "average_rating": 4.5,
  "reviews_count": 2,
  "created_at": "2025-08-06T10:30:00Z",
  "updated_at": "2025-08-06T10:30:00Z"
}
```

## Admin Interface

Access the Django admin at `http://127.0.0.1:8000/admin/` to manage data through a web interface.

## Project Structure

```
api_project/
├── api_project/          # Main project settings
│   ├── settings.py       # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── books/               # Books app
│   ├── models.py        # Data models
│   ├── serializers.py   # API serializers
│   ├── views.py         # API views
│   ├── urls.py          # App URLs
│   ├── admin.py         # Admin configuration
│   └── management/      # Custom management commands
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Technology Stack

- **Django 5.2.4** - Web framework
- **Django REST Framework 3.16.0** - API framework
- **django-cors-headers** - CORS support
- **django-filter** - Advanced filtering
- **SQLite** - Database (default, can be changed to PostgreSQL/MySQL)

## Next Steps

1. **Add more advanced features**:
   - File uploads for book covers
   - User favorites/wishlist
   - Advanced search with Elasticsearch
   - Rate limiting

2. **Deploy to production**:
   - Configure PostgreSQL database
   - Set up Redis for caching
   - Configure static files serving
   - Set up CI/CD pipeline

3. **Frontend Integration**:
   - Build React/Vue.js frontend
   - Mobile app with React Native/Flutter
   - API documentation with Swagger/OpenAPI
