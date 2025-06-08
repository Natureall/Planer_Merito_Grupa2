import threading
import time
import os
import subprocess
import webview

def install_requirements():
    try:
        subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
    except Exception as e:
        print("Błąd podczas instalacji paczek:", e)

def run_migrations():
    try:
        subprocess.run(["python", "manage.py", "makemigrations", "main"], check=True)
    except:
        pass  
    subprocess.run(["python", "manage.py", "makemigrations"], check=True)
    subprocess.run(["python", "manage.py", "migrate"], check=True)

def run_django():
    os.system("python manage.py runserver")

if __name__ == '__main__':
    print("🔧 Instalacja zależności...")
    install_requirements()
    print("🧱 Migracje bazy danych...")
    run_migrations()
    print("🚀 Uruchamianie aplikacji Django...")
    threading.Thread(target=run_django, daemon=True).start()
    time.sleep(2)
    webview.create_window("Panel Studenta WSB", "http://127.0.0.1:8000", width=1200, height=800)
    webview.start()
