#!/usr/bin/env python
"""
Django REST API Authentication Demo
Step-by-step guide for making authenticated requests
"""
import requests
import json

# API Configuration
BASE_URL = "http://127.0.0.1:8000"
API_URL = f"{BASE_URL}/api"

def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

def print_step(step, description):
    print(f"\n{step}. {description}")
    print("-" * 50)

def print_response(response, show_data=True):
    print(f"Status Code: {response.status_code}")
    if show_data and response.content:
        try:
            data = response.json()
            print(f"Response: {json.dumps(data, indent=2)}")
        except:
            print(f"Response: {response.text}")
    print()

def main():
    print_section("DJANGO REST API AUTHENTICATION GUIDE")
    
    # Step 1: Test unauthenticated access
    print_step(1, "Testing Unauthenticated Access (Read-Only)")
    
    print("📖 Getting books list (no auth required)...")
    response = requests.get(f"{API_URL}/books/")
    print_response(response)
    
    print("👥 Getting authors list (no auth required)...")
    response = requests.get(f"{API_URL}/authors/")
    print_response(response)
    
    # Step 2: Try to create without authentication (should fail)
    print_step(2, "Attempting to Create Data Without Authentication (Should Fail)")
    
    new_author = {
        "name": "Test Author",
        "email": "test@example.com",
        "bio": "A test author"
    }
    
    print("❌ Trying to create author without authentication...")
    response = requests.post(f"{API_URL}/authors/", json=new_author)
    print_response(response)
    
    # Step 3: Get authentication token
    print_step(3, "Getting Authentication Token")
    
    credentials = {
        "username": "john_doe",
        "password": "password123"
    }
    
    print("🔐 Getting auth token...")
    response = requests.post(f"{API_URL}/auth/token/", json=credentials)
    print_response(response)
    
    if response.status_code == 200:
        token = response.json().get('token')
        print(f"✅ Token obtained: {token}")
        
        # Step 4: Use token for authenticated requests
        print_step(4, "Making Authenticated Requests with Token")
        
        headers = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'
        }
        
        print("✅ Creating author with authentication...")
        response = requests.post(f"{API_URL}/authors/", json=new_author, headers=headers)
        print_response(response)
        
        if response.status_code == 201:
            author_id = response.json().get('id')
            print(f"✅ Author created with ID: {author_id}")
            
            # Create a book
            new_book = {
                "title": "Test Book",
                "author": author_id,
                "isbn": "1234567890123",
                "publication_date": "2025-01-01",
                "pages": 200,
                "genre": "fiction",
                "description": "A test book",
                "price": "19.99"
            }
            
            print("✅ Creating book with authentication...")
            response = requests.post(f"{API_URL}/books/", json=new_book, headers=headers)
            print_response(response)
            
            if response.status_code == 201:
                book_id = response.json().get('id')
                print(f"✅ Book created with ID: {book_id}")
                
                # Create a review
                new_review = {
                    "book": book_id,
                    "rating": 5,
                    "comment": "Excellent test book!"
                }
                
                print("✅ Creating review with authentication...")
                response = requests.post(f"{API_URL}/reviews/", json=new_review, headers=headers)
                print_response(response)
        
        # Step 5: Get user profile
        print_step(5, "Getting User Profile")
        print("👤 Getting user profile...")
        response = requests.get(f"{API_URL}/user/profile/", headers=headers)
        print_response(response)
        
        # Step 6: Update data
        print_step(6, "Updating Data with Authentication")
        print("✏️ Updating author...")
        updated_author = {
            "name": "Updated Test Author",
            "email": "updated@example.com",
            "bio": "An updated test author"
        }
        response = requests.put(f"{API_URL}/authors/{author_id}/", json=updated_author, headers=headers)
        print_response(response)
        
    else:
        print("❌ Failed to get token. Check credentials.")

def print_manual_steps():
    print_section("MANUAL AUTHENTICATION METHODS")
    
    print("""
🌐 METHOD 1: Browser-Based Authentication (Django REST Framework Browsable API)
═══════════════════════════════════════════════════════════════════════════════

1. Start the Django server:
   python manage.py runserver

2. Open browser and go to:
   http://127.0.0.1:8000/api-auth/login/

3. Login with credentials:
   Username: john_doe
   Password: password123

4. After login, navigate to any API endpoint:
   - http://127.0.0.1:8000/api/books/
   - http://127.0.0.1:8000/api/authors/
   - http://127.0.0.1:8000/api/reviews/

5. You'll see a web interface where you can:
   - View data in JSON format
   - Create new records using forms
   - Edit existing records
   - Delete records

🔧 METHOD 2: curl Commands
═══════════════════════════

1. Get authentication token:
   curl -X POST http://127.0.0.1:8000/api/auth/token/ \\
        -H "Content-Type: application/json" \\
        -d '{"username": "john_doe", "password": "password123"}'

2. Use token in subsequent requests:
   curl -X GET http://127.0.0.1:8000/api/books/ \\
        -H "Authorization: Token YOUR_TOKEN_HERE"

3. Create new data:
   curl -X POST http://127.0.0.1:8000/api/authors/ \\
        -H "Authorization: Token YOUR_TOKEN_HERE" \\
        -H "Content-Type: application/json" \\
        -d '{"name": "New Author", "email": "new@example.com"}'

📱 METHOD 3: Postman/Insomnia
═══════════════════════════

1. Create a new request
2. Set URL: http://127.0.0.1:8000/api/auth/token/
3. Set method: POST
4. Set body (JSON):
   {
     "username": "john_doe",
     "password": "password123"
   }
5. Send request to get token
6. For subsequent requests, add header:
   Authorization: Token YOUR_TOKEN_HERE

🐍 METHOD 4: Python requests (shown in script above)
══════════════════════════════════════════════════

See the automated demo above for complete Python example.

👤 Available Test Users:
═══════════════════════

- Username: john_doe    | Password: password123
- Username: jane_smith  | Password: password123  
- Username: bob_johnson | Password: password123

🔑 Available Endpoints:
═════════════════════

PUBLIC (No auth needed for GET):
- GET /api/books/
- GET /api/authors/
- GET /api/reviews/
- GET /api/overview/

AUTHENTICATED (Token required for POST/PUT/DELETE):
- POST/PUT/DELETE /api/books/
- POST/PUT/DELETE /api/authors/
- POST/PUT/DELETE /api/reviews/
- GET /api/user/profile/

AUTHENTICATION:
- POST /api/auth/token/ (get token)
- /api-auth/login/ (browser login)
""")

if __name__ == "__main__":
    print("🚀 Make sure Django server is running: python manage.py runserver")
    print("📡 Testing API authentication...")
    
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Make sure Django server is running!")
        print("   Run: python manage.py runserver")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print_manual_steps()
