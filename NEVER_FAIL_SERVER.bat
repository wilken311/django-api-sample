@echo off
cls
color 0A
echo.
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║              DJANGO API - FOOLPROOF STARTUP                 ║
echo  ║          This script prevents the django_filters error      ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.

REM Step 1: Check current directory
echo [1/8] 📁 Checking current directory...
if not exist "manage.py" (
    echo ❌ ERROR: manage.py not found!
    echo    You must be in: c:\TheSourcecode\python\api
    echo    Current location: %cd%
    echo.
    echo    Fix: cd c:\TheSourcecode\python\api
    pause
    exit /b 1
)
echo ✅ Correct directory found

REM Step 2: Check virtual environment
echo.
echo [2/8] 🐍 Checking virtual environment...
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERROR: Virtual environment missing!
    echo    Expected: venv\Scripts\activate.bat
    echo.
    echo    Fix: python -m venv venv
    pause
    exit /b 1
)
echo ✅ Virtual environment exists

REM Step 3: Activate virtual environment
echo.
echo [3/8] ⚡ Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)
echo ✅ Virtual environment activated (you should see 'venv' in title)

REM Step 4: Verify Python path
echo.
echo [4/8] 🔍 Verifying Python executable...
python -c "import sys; path = sys.executable; print('Python:', path); exit(0 if 'venv' in path else 1)"
if errorlevel 1 (
    echo ❌ ERROR: Still using system Python!
    echo    Virtual environment activation failed
    echo.
    echo    Try closing this window and running again
    pause
    exit /b 1
)
echo ✅ Using virtual environment Python

REM Step 5: Check Django
echo.
echo [5/8] 🌐 Checking Django installation...
python -c "import django; print('Django version:', django.get_version())" 2>nul
if errorlevel 1 (
    echo ❌ ERROR: Django not found in virtual environment!
    echo    Installing from requirements.txt...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ ERROR: Failed to install requirements!
        pause
        exit /b 1
    )
)
echo ✅ Django is available

REM Step 6: Check django_filters specifically
echo.
echo [6/8] 🔧 Checking django_filters (the problematic module)...
python -c "import django_filters; print('django_filters version:', django_filters.__version__)" 2>nul
if errorlevel 1 (
    echo ❌ ERROR: django_filters missing!
    echo    This is the module causing your error. Installing...
    pip install django-filter
    if errorlevel 1 (
        echo ❌ ERROR: Failed to install django-filter!
        pause
        exit /b 1
    )
    echo ✅ django-filter installed successfully
) else (
    echo ✅ django_filters is available
)

REM Step 7: Django system check
echo.
echo [7/8] ✔️  Running Django system check...
python manage.py check
if errorlevel 1 (
    echo ❌ ERROR: Django configuration issues found!
    pause
    exit /b 1
)
echo ✅ Django configuration is valid

REM Step 8: Start server
echo.
echo [8/8] 🚀 Starting Django development server...
echo.
color 0F
echo  ╔══════════════════════════════════════════════════════════════╗
echo  ║                    🎉 SERVER STARTING! 🎉                    ║
echo  ║                                                              ║
echo  ║  Your Django REST API will be available at:                 ║
echo  ║                                                              ║
echo  ║  📱 Main API:        http://127.0.0.1:8000/api/             ║
echo  ║  🔐 Login Page:      http://127.0.0.1:8000/api-auth/login/  ║
echo  ║  📚 Books API:       http://127.0.0.1:8000/api/books/       ║
echo  ║  👥 Authors API:     http://127.0.0.1:8000/api/authors/     ║
echo  ║  ⭐ Reviews API:     http://127.0.0.1:8000/api/reviews/      ║
echo  ║                                                              ║
echo  ║  Test Login Credentials:                                     ║
echo  ║  👤 Username: john_doe                                       ║
echo  ║  🔑 Password: password123                                    ║
echo  ║                                                              ║
echo  ║  Press Ctrl+C to stop the server                            ║
echo  ╚══════════════════════════════════════════════════════════════╝
echo.
echo Starting server in 3 seconds...
timeout /t 3 /nobreak >nul
echo.

python manage.py runserver 127.0.0.1:8000

echo.
echo 👋 Server stopped. Press any key to exit...
pause >nul
