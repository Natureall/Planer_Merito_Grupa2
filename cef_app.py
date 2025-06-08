import os
import sys
import time
import threading
from cefpython3 import cefpython as cef

def run_django():
    os.system("python manage.py runserver")

def main():
    
    t = threading.Thread(target=run_django, daemon=True)
    t.start()

    time.sleep(2)

    sys.excepthook = cef.ExceptHook
    cef.Initialize()
    window_info = cef.WindowInfo()
    window_info.SetAsChild(0)
    browser = cef.CreateBrowserSync(url="http://127.0.0.1:8000/")
    cef.MessageLoop()
    cef.Shutdown()

if __name__ == '__main__':
    main()
