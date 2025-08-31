# Django REST API - Complete Endpoint Reference

## 🚀 Server Setup

First, make sure your server is running:
```bash
cd c:\TheSourcecode\python\api
venv\Scripts\activate
python manage.py runserver
```

Or use the batch file:
```bash
start_server.bat
```

Server will be available at: `http://127.0.0.1:8000`

## 📋 Complete API Endpoint List

### 🔐 Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/auth/token/` | Get authentication token | No |
| `GET` | `/api-auth/login/` | Browser-based login page | No |
| `POST` | `/api-auth/login/` | Browser-based login | No |
| `POST` | `/api-auth/logout/` | Browser-based logout | Yes |

### 👥 Authors Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/authors/` | List all authors | No (Read-only) |
| `POST` | `/api/authors/` | Create new author | Yes |
| `GET` | `/api/authors/{id}/` | Get specific author details | No |
| `PUT` | `/api/authors/{id}/` | Update author (full) | Yes |
| `PATCH` | `/api/authors/{id}/` | Update author (partial) | Yes |
| `DELETE` | `/api/authors/{id}/` | Delete author | Yes |
| `GET` | `/api/authors/{id}/books/` | Get all books by author | No |

### 📚 Books Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/books/` | List all books | No (Read-only) |
| `POST` | `/api/books/` | Create new book | Yes |
| `GET` | `/api/books/{id}/` | Get specific book details | No |
| `PUT` | `/api/books/{id}/` | Update book (full) | Yes |
| `PATCH` | `/api/books/{id}/` | Update book (partial) | Yes |
| `DELETE` | `/api/books/{id}/` | Delete book | Yes |
| `GET` | `/api/books/by_genre/` | Get books by genre | No |
| `GET` | `/api/books/popular/` | Get popular books (4+ stars) | No |
| `GET` | `/api/books/{id}/reviews/` | Get all reviews for a book | No |

### ⭐ Reviews Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/reviews/` | List all reviews | No (Read-only) |
| `POST` | `/api/reviews/` | Create new review | Yes |
| `GET` | `/api/reviews/{id}/` | Get specific review | No |
| `PUT` | `/api/reviews/{id}/` | Update review (own only) | Yes |
| `PATCH` | `/api/reviews/{id}/` | Update review (own only) | Yes |
| `DELETE` | `/api/reviews/{id}/` | Delete review (own only) | Yes |

### 👤 User Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/user/profile/` | Get current user profile | Yes |

### 📖 Information Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/overview/` | API overview and documentation | No |
| `GET` | `/api/` | DRF browsable API root | No |

## 🔍 Query Parameters & Filtering

### Books Filtering & Search
```
GET /api/books/?genre=fiction
GET /api/books/?author=1
GET /api/books/?is_available=true
GET /api/books/?search=harry
GET /api/books/?search=orwell
GET /api/books/?ordering=-created_at
GET /api/books/?ordering=title
```

### Books Special Endpoints
```
GET /api/books/by_genre/?genre=fiction
GET /api/books/by_genre/?genre=sci_fi
GET /api/books/popular/
```

### Authors Filtering & Search
```
GET /api/authors/?search=rowling
GET /api/authors/?ordering=name
GET /api/authors/?ordering=-created_at
```

### Reviews Filtering
```
GET /api/reviews/?book=1
GET /api/reviews/?rating=5
GET /api/reviews/?my_reviews=true
GET /api/reviews/?ordering=-created_at
```

### Pagination
```
GET /api/books/?page=1
GET /api/books/?page=2
```

## 🛠 How to Access the API

### Method 1: Browser (Easiest)

1. **Login first**: Go to `http://127.0.0.1:8000/api-auth/login/`
   - Username: `john_doe` 
   - Password: `password123`

2. **Browse endpoints**: Visit any endpoint in your browser:
   - `http://127.0.0.1:8000/api/books/`
   - `http://127.0.0.1:8000/api/authors/`
   - `http://127.0.0.1:8000/api/reviews/`

3. **Interactive forms**: Create, edit, delete using web forms

### Method 2: Token Authentication

1. **Get token**:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "john_doe", "password": "password123"}'
```

2. **Use token in requests**:
```bash
curl -X GET http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Method 3: Python Requests

```python
import requests

# Get token
response = requests.post('http://127.0.0.1:8000/api/auth/token/', 
                        json={'username': 'john_doe', 'password': 'password123'})
token = response.json()['token']

# Use token
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/books/', headers=headers)
books = response.json()
```

## 📝 Example API Calls

### Get All Books
```bash
curl -X GET http://127.0.0.1:8000/api/books/
```

### Get Books by Genre
```bash
curl -X GET "http://127.0.0.1:8000/api/books/by_genre/?genre=fiction"
```

### Search Books
```bash
curl -X GET "http://127.0.0.1:8000/api/books/?search=harry"
```

### Create New Author (with authentication)
```bash
curl -X POST http://127.0.0.1:8000/api/authors/ \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "New Author",
       "email": "new@example.com",
       "bio": "A new author"
     }'
```

### Create New Book (with authentication)
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "New Book",
       "author": 1,
       "isbn": "1234567890123",
       "publication_date": "2025-01-01",
       "pages": 200,
       "genre": "fiction",
       "description": "A new book",
       "price": "19.99"
     }'
```

### Create Review (with authentication)
```bash
curl -X POST http://127.0.0.1:8000/api/reviews/ \
     -H "Authorization: Token YOUR_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{
       "book": 1,
       "rating": 5,
       "comment": "Excellent book!"
     }'
```

### Get User Profile (with authentication)
```bash
curl -X GET http://127.0.0.1:8000/api/user/profile/ \
     -H "Authorization: Token YOUR_TOKEN"
```

## 🔑 Available Test Accounts

| Username | Password | Email |
|----------|----------|-------|
| `john_doe` | `password123` | john@example.com |
| `jane_smith` | `password123` | jane@example.com |
| `bob_johnson` | `password123` | bob@example.com |

## 📊 Sample Data Available

- **4 Authors**: J.K. Rowling, George Orwell, Agatha Christie, Isaac Asimov
- **5 Books**: Harry Potter, 1984, Murder on Orient Express, Foundation, Animal Farm
- **6 Reviews**: Various ratings and comments
- **4 Users**: Including the 3 test users above

## 🎯 Quick Test URLs

Copy these URLs into your browser (after logging in):

```
http://127.0.0.1:8000/api/overview/
http://127.0.0.1:8000/api/books/
http://127.0.0.1:8000/api/books/1/
http://127.0.0.1:8000/api/books/popular/
http://127.0.0.1:8000/api/books/by_genre/?genre=fiction
http://127.0.0.1:8000/api/authors/
http://127.0.0.1:8000/api/authors/1/
http://127.0.0.1:8000/api/authors/1/books/
http://127.0.0.1:8000/api/reviews/
http://127.0.0.1:8000/api/reviews/?my_reviews=true
http://127.0.0.1:8000/api/user/profile/
```

## 🚀 Getting Started

1. **Start server**: `start_server.bat` or `python manage.py runserver`
2. **Login**: Visit `http://127.0.0.1:8000/api-auth/login/`
3. **Explore**: Go to `http://127.0.0.1:8000/api/` for interactive browsing
4. **Test**: Use the URLs above to test different endpoints

Your Django REST API is fully functional with complete CRUD operations! 🎉
