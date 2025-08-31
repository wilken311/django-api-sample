#!/usr/bin/env python
"""
Django API Troubleshooting Script
Diagnoses common issues with the Django REST API setup
"""
import os
import sys
import subprocess

def check_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print('='*60)

def run_command(cmd, description):
    print(f"\n🔍 {description}")
    print(f"Command: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=os.getcwd())
        if result.returncode == 0:
            print(f"✅ Success: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ Error: {result.stderr.strip()}")
            return False
    except Exception as e:
        print(f"❌ Exception: {e}")
        return False

def check_python_path():
    print(f"\n🐍 Python executable: {sys.executable}")
    print(f"🐍 Python version: {sys.version}")
    print(f"📁 Current working directory: {os.getcwd()}")
    print(f"📁 Python path: {sys.path}")

def check_virtual_env():
    venv_path = os.path.join(os.getcwd(), 'venv')
    if os.path.exists(venv_path):
        print(f"✅ Virtual environment found at: {venv_path}")
        
        # Check if we're in the virtual environment
        if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
            print("✅ Virtual environment is activated")
            return True
        else:
            print("⚠️  Virtual environment exists but is NOT activated")
            print("   Activate it with: venv\\Scripts\\activate")
            return False
    else:
        print(f"❌ Virtual environment not found at: {venv_path}")
        print("   Create it with: python -m venv venv")
        return False

def check_imports():
    modules_to_check = [
        'django',
        'rest_framework', 
        'corsheaders',
        'django_filters',
        'books.models'
    ]
    
    for module in modules_to_check:
        try:
            __import__(module)
            print(f"✅ {module} - OK")
        except ImportError as e:
            print(f"❌ {module} - FAILED: {e}")
        except Exception as e:
            print(f"⚠️  {module} - WARNING: {e}")

def main():
    print("Django API Troubleshooting Tool")
    print("This script will help diagnose issues with your Django setup")
    
    check_section("1. Python Environment Check")
    check_python_path()
    
    check_section("2. Virtual Environment Check")
    venv_ok = check_virtual_env()
    
    check_section("3. Django Setup Check")
    
    # Set up Django environment
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
    
    try:
        import django
        django.setup()
        print("✅ Django setup successful")
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return
    
    check_section("4. Module Import Check")
    check_imports()
    
    check_section("5. Django Commands Check")
    commands = [
        ("python manage.py check", "Django system check"),
        ("python manage.py showmigrations", "Show migrations status"),
        ("python --version", "Python version check"),
        ("pip list | findstr django", "Django packages check") if os.name == 'nt' else ("pip list | grep django", "Django packages check")
    ]
    
    for cmd, desc in commands:
        run_command(cmd, desc)
    
    check_section("6. Database Check")
    try:
        from books.models import Author, Book, Review
        from django.contrib.auth.models import User
        
        print(f"✅ Models imported successfully")
        print(f"📊 Authors: {Author.objects.count()}")
        print(f"📊 Books: {Book.objects.count()}")
        print(f"📊 Reviews: {Review.objects.count()}")
        print(f"📊 Users: {User.objects.count()}")
        
    except Exception as e:
        print(f"❌ Database check failed: {e}")
    
    check_section("7. Recommendations")
    
    if not venv_ok:
        print("🔧 Activate virtual environment:")
        print("   venv\\Scripts\\activate")
        print()
    
    print("🔧 If django_filters error persists:")
    print("   1. Make sure virtual environment is activated")
    print("   2. pip install django-filter")
    print("   3. Restart your terminal/command prompt")
    print()
    
    print("🔧 To start the server:")
    print("   1. venv\\Scripts\\activate")
    print("   2. python manage.py runserver")
    print()
    
    print("🔧 Or use the batch file:")
    print("   start_server.bat")

if __name__ == "__main__":
    main()
