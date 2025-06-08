import threading
import webview
import os
import time
from subprocess import Popen

def run_server():
    os.system("python manage.py runserver")

if __name__ == '__main__':
    threading.Thread(target=run_server, daemon=True).start()

    time.sleep(2)

    webview.create_window("Panel Studenta WSB", "http://127.0.0.1:8000/", width=1200, height=800)
    webview.start()
