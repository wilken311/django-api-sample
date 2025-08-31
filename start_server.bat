@echo off
echo.
echo ================================================
echo   DJANGO API SERVER - FOOLPROOF STARTUP
echo ================================================
echo.

echo 🔍 Step 1: Checking current directory...
if not exist "manage.py" (
    echo ❌ ERROR: manage.py not found!
    echo    You must run this from: c:\TheSourcecode\python\api
    echo    Current directory: %cd%
    pause
    exit /b 1
)
echo ✅ Found manage.py - We're in the right directory

echo.
echo 🔍 Step 2: Checking virtual environment...
if not exist "venv\Scripts\activate.bat" (
    echo ❌ ERROR: Virtual environment not found!
    echo    Expected: venv\Scripts\activate.bat
    echo    Please create it with: python -m venv venv
    pause
    exit /b 1
)
echo ✅ Virtual environment found

echo.
echo 🔍 Step 3: Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ ERROR: Failed to activate virtual environment!
    pause
    exit /b 1
)
echo ✅ Virtual environment activated - You should see (venv) in prompt

echo.
echo 🔍 Step 4: Verifying Python path...
for /f "tokens=*" %%i in ('python -c "import sys; print(sys.executable)"') do set PYTHON_PATH=%%i
echo    Python executable: %PYTHON_PATH%
echo %PYTHON_PATH% | findstr "venv" >nul
if errorlevel 1 (
    echo ❌ ERROR: Still using system Python instead of virtual environment!
    echo    Expected path to contain 'venv'
    echo    Try running: venv\Scripts\activate.bat
    pause
    exit /b 1
)
echo ✅ Using virtual environment Python

echo.
echo 🔍 Step 5: Checking Django installation...
python -c "import django; print('Django version:', django.get_version())" 2>nul
if errorlevel 1 (
    echo ❌ ERROR: Django not found in virtual environment!
    echo    Installing requirements...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ ERROR: Failed to install requirements!
        pause
        exit /b 1
    )
)
echo ✅ Django is available

echo.
echo 🔍 Step 6: Checking django_filters...
python -c "import django_filters; print('django_filters is available')" 2>nul
if errorlevel 1 (
    echo ❌ ERROR: django_filters not found!
    echo    Installing django-filter...
    pip install django-filter
    if errorlevel 1 (
        echo ❌ ERROR: Failed to install django-filter!
        pause
        exit /b 1
    )
)
echo ✅ django_filters is available

echo.
echo 🔍 Step 7: Running Django system check...
python manage.py check >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Django system check failed!
    echo    Running detailed check...
    python manage.py check
    pause
    exit /b 1
)
echo ✅ Django system check passed

echo.
echo 🔍 Step 8: Checking database migrations...
python manage.py showmigrations --plan | findstr "\[ \]" >nul
if not errorlevel 1 (
    echo ⚠️  Unapplied migrations found. Applying them...
    python manage.py migrate
)
echo ✅ Database is up to date

echo.
echo ================================================
echo   🚀 STARTING DJANGO SERVER
echo ================================================
echo.
echo   Server will be available at:
echo   👉 http://127.0.0.1:8000/
echo   👉 http://127.0.0.1:8000/api/
echo   👉 http://127.0.0.1:8000/api-auth/login/
echo.
echo   Test credentials:
echo   👤 Username: john_doe
echo   🔑 Password: password123
echo.
echo   Press Ctrl+C to stop the server
echo ================================================
echo.

python manage.py runserver 127.0.0.1:8000
