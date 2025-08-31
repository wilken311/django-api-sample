# Django Server Error Fix - ModuleNotFoundError: No module named 'django_filters'

## ❌ **The Problem**

You're getting this error because you're running Django commands outside of the virtual environment. The error occurs when:

1. The virtual environment is not activated
2. You're using system Python instead of virtual environment Python
3. Dependencies are installed in the virtual environment but you're running from system Python

## ✅ **The Solution**

### **Step 1: Always Activate Virtual Environment**

Before running any Django commands, **ALWAYS** activate your virtual environment first:

```bash
# Navigate to project directory
cd c:\TheSourcecode\python\api

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your prompt
```

### **Step 2: Verify You're in the Virtual Environment**

Check that you're using the correct Python:

```bash
python -c "import sys; print('Python path:', sys.executable)"
```

**Correct output** (virtual environment):
```
Python path: C:\TheSourcecode\python\api\venv\Scripts\python.exe
```

**Wrong output** (system Python):
```
Python path: C:\Users\monte\AppData\Local\Programs\Python\Python313\python.exe
```

### **Step 3: Install Missing Dependencies**

If you're in the virtual environment and still getting the error:

```bash
pip install django-filter django-cors-headers
```

### **Step 4: Test the Setup**

```bash
python manage.py check
```

Should output: `System check identified no issues (0 silenced).`

### **Step 5: Start the Server**

```bash
python manage.py runserver
```

## 🛠️ **Quick Fix Commands**

Run these commands in order:

```bash
cd c:\TheSourcecode\python\api
venv\Scripts\activate
pip install django-filter
python manage.py check
python manage.py runserver
```

## 🚀 **Easy Startup Script**

Use the batch file I created for you:

```bash
start_server.bat
```

This script automatically:
- Checks virtual environment
- Activates it
- Installs missing dependencies
- Runs system checks
- Starts the server

## 🔍 **How to Avoid This Error**

### **Always Remember:**
1. **Navigate to project**: `cd c:\TheSourcecode\python\api`
2. **Activate venv**: `venv\Scripts\activate`
3. **See (venv) in prompt**: `(venv) C:\TheSourcecode\python\api λ`
4. **Then run Django commands**: `python manage.py runserver`

### **Visual Indicators:**
- ✅ **Correct**: `(venv) C:\TheSourcecode\python\api λ`
- ❌ **Wrong**: `C:\TheSourcecode\python\api λ` (missing venv)

## 🆘 **Troubleshooting**

### **If you still get the error:**

1. **Delete and recreate virtual environment:**
   ```bash
   rmdir /s venv
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Verify installations:**
   ```bash
   pip list | findstr django
   ```
   Should show:
   ```
   Django                5.2.4
   django-cors-headers   4.7.0
   django-filter         25.1
   djangorestframework   3.16.0
   ```

3. **Test imports:**
   ```bash
   python -c "import django_filters; print('OK')"
   ```

## 📋 **Your Current Status**

After running the fix commands above, your server should be working at:
- **API Root**: http://127.0.0.1:8000/api/
- **Login**: http://127.0.0.1:8000/api-auth/login/
- **Books**: http://127.0.0.1:8000/api/books/

## 🎯 **Key Takeaway**

**Always activate your virtual environment before running any Django commands!**

The virtual environment contains all your project dependencies, while system Python doesn't have django-filter installed.
