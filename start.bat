@echo off
echo Uruchamianie aplikacji Panel Studenta...
start "" http://127.0.0.1:8000/
python manage.py runserver
pause
