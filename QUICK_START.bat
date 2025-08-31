@echo off
cd /d c:\TheSourcecode\python\api
call venv\Scripts\activate
echo.
echo ✅ Virtual environment activated
echo ✅ Starting Django server...
echo.
echo 📱 Your API will be at: http://127.0.0.1:8000/api/
echo 🔐 Login at: http://127.0.0.1:8000/api-auth/login/
echo 👤 Username: john_doe  🔑 Password: password123
echo.
python manage.py runserver 127.0.0.1:8000
