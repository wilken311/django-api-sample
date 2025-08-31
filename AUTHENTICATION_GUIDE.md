# Django REST API Authentication - Complete Guide

## Overview

Your Django REST API supports multiple authentication methods. Here's how to use each one:

## Available Test Users

- **Username**: `john_doe` | **Password**: `password123`
- **Username**: `jane_smith` | **Password**: `password123`  
- **Username**: `bob_johnson` | **Password**: `password123`

## Method 1: Browser-Based Authentication (Easiest)

### Step 1: Start the Server
```bash
cd c:\TheSourcecode\python\api
venv\Scripts\activate
python manage.py runserver
```

### Step 2: Login via Browser
1. Open browser and go to: `http://127.0.0.1:8000/api-auth/login/`
2. Enter credentials:
   - **Username**: `john_doe`
   - **Password**: `password123`
3. Click "Log in"

### Step 3: Access API Endpoints
After login, you can visit these URLs and perform all operations:

- **Books**: `http://127.0.0.1:8000/api/books/`
- **Authors**: `http://127.0.0.1:8000/api/authors/`
- **Reviews**: `http://127.0.0.1:8000/api/reviews/`
- **User Profile**: `http://127.0.0.1:8000/api/user/profile/`

The browsable API interface allows you to:
- View JSON data
- Create new records using forms
- Edit existing records
- Delete records
- Test all endpoints interactively

## Method 2: Token Authentication

### Step 1: Get Authentication Token

**Using curl:**
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "john_doe", "password": "password123"}'
```

**Using Python requests:**
```python
import requests

response = requests.post('http://127.0.0.1:8000/api/auth/token/', 
                        json={'username': 'john_doe', 'password': 'password123'})
token = response.json()['token']
print(f"Token: {token}")
```

### Step 2: Use Token in Requests

**Headers to include:**
```
Authorization: Token YOUR_TOKEN_HERE
Content-Type: application/json
```

**Example curl commands:**

1. **Get books:**
```bash
curl -X GET http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Token YOUR_TOKEN_HERE"
```

2. **Create a new author:**
```bash
curl -X POST http://127.0.0.1:8000/api/authors/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -H "Content-Type: application/json" \
     -d '{"name": "New Author", "email": "new@example.com", "bio": "Test author"}'
```

3. **Create a new book:**
```bash
curl -X POST http://127.0.0.1:8000/api/books/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "Test Book",
       "author": 1,
       "isbn": "1234567890123",
       "publication_date": "2025-01-01",
       "pages": 200,
       "genre": "fiction",
       "description": "A test book",
       "price": "19.99"
     }'
```

4. **Create a review:**
```bash
curl -X POST http://127.0.0.1:8000/api/reviews/ \
     -H "Authorization: Token YOUR_TOKEN_HERE" \
     -H "Content-Type: application/json" \
     -d '{"book": 1, "rating": 5, "comment": "Great book!"}'
```

## Method 3: Using Postman/Insomnia

### Step 1: Get Token
1. Create new POST request
2. URL: `http://127.0.0.1:8000/api/auth/token/`
3. Body (JSON):
   ```json
   {
     "username": "john_doe",
     "password": "password123"
   }
   ```
4. Send request and copy the token from response

### Step 2: Use Token in Headers
For all subsequent requests, add header:
- **Key**: `Authorization`
- **Value**: `Token YOUR_TOKEN_HERE`

### Step 3: Test Endpoints
Now you can make requests to any endpoint with full access.

## Method 4: Python Script

Run the comprehensive demo:

```bash
cd c:\TheSourcecode\python\api
python auth_demo.py
```

This script will automatically:
1. Test unauthenticated access
2. Get authentication token
3. Create authors, books, and reviews
4. Show all authentication methods

## Available Endpoints

### Public Endpoints (No Auth Required for GET)
- `GET /api/books/` - List all books
- `GET /api/authors/` - List all authors  
- `GET /api/reviews/` - List all reviews
- `GET /api/overview/` - API overview

### Protected Endpoints (Auth Required)
- `POST/PUT/DELETE /api/books/` - Modify books
- `POST/PUT/DELETE /api/authors/` - Modify authors
- `POST/PUT/DELETE /api/reviews/` - Modify reviews
- `GET /api/user/profile/` - Get user profile

### Authentication Endpoints
- `POST /api/auth/token/` - Get authentication token
- `/api-auth/login/` - Browser-based login

## Quick Test Commands

1. **Start server:**
   ```bash
   python manage.py runserver
   ```

2. **Get token:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/auth/token/ \
        -H "Content-Type: application/json" \
        -d '{"username": "john_doe", "password": "password123"}'
   ```

3. **Test authenticated request:**
   ```bash
   curl -X GET http://127.0.0.1:8000/api/user/profile/ \
        -H "Authorization: Token YOUR_TOKEN_HERE"
   ```

## Troubleshooting

- **"Authentication credentials were not provided"**: You need to login or provide a token
- **"Invalid token"**: Get a new token using `/api/auth/token/`
- **"Permission denied"**: Make sure you're using the correct user credentials
- **Connection refused**: Make sure Django server is running (`python manage.py runserver`)

## Next Steps

1. Start the server: `python manage.py runserver`
2. Try the browser method first (easiest)
3. Then experiment with token authentication
4. Run the demo script for automated testing

The browsable API at `http://127.0.0.1:8000/api/` is the best way to explore and test your API!
