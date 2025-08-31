# 🚨 CRITICAL: How to Avoid the "django_filters" Error

## ❌ **The Problem You Keep Having:**

You get `ModuleNotFoundError: No module named 'django_filters'` because you're **NOT in the virtual environment** when running Django commands.

## ✅ **The Solution (ALWAYS Follow These Steps):**

### **STEP 1: Navigate to Project Directory**
```cmd
cd c:\TheSourcecode\python\api
```

### **STEP 2: Activate Virtual Environment** ⭐ **MOST IMPORTANT STEP**
```cmd
venv\Scripts\activate
```

### **STEP 3: Verify You See (venv) in Prompt**
Your command prompt should look like:
```
(venv) C:\TheSourcecode\python\api λ
```

**If you don't see `(venv)`, STOP and repeat Step 2!**

### **STEP 4: Now You Can Run Django Commands**
```cmd
python manage.py runserver
```

## 🎯 **Visual Indicators:**

### ✅ **CORRECT (Virtual Environment Active):**
```
(venv) C:\TheSourcecode\python\api λ python manage.py runserver
```
**Notice the `(venv)` at the beginning!**

### ❌ **WRONG (System Python):**
```
C:\TheSourcecode\python\api λ python manage.py runserver
```
**No `(venv)` = You'll get the error!**

## 🛠 **Easy Ways to Start Server:**

### **Method 1: Use the Improved Batch Script**
```cmd
START_SERVER.bat
```
This script does everything automatically and prevents the error.

### **Method 2: Manual (Always Follow the 4 Steps Above)**
```cmd
cd c:\TheSourcecode\python\api
venv\Scripts\activate
python manage.py runserver
```

## 🔍 **How to Check if You're in Virtual Environment:**

Run this command to see which Python you're using:
```cmd
python -c "import sys; print('Python path:', sys.executable)"
```

**CORRECT OUTPUT (Virtual Environment):**
```
Python path: C:\TheSourcecode\python\api\venv\Scripts\python.exe
```

**WRONG OUTPUT (System Python):**
```
Python path: C:\Users\monte\AppData\Local\Programs\Python\Python313\python.exe
```

## 🎯 **Remember This:**

**EVERY TIME you open a new terminal/command prompt, you MUST:**
1. Navigate to the project directory
2. Activate the virtual environment with `venv\Scripts\activate`
3. Look for `(venv)` in your prompt
4. Only then run Django commands

## 🚀 **Your Server URLs (After Starting Correctly):**

- **API Root**: http://127.0.0.1:8000/api/
- **Login**: http://127.0.0.1:8000/api-auth/login/
- **Books**: http://127.0.0.1:8000/api/books/
- **Authors**: http://127.0.0.1:8000/api/authors/

**Test Credentials:**
- Username: `john_doe`
- Password: `password123`
