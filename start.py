import subprocess
import sys
import os
import threading
import time
import webbrowser

def install_deps():
    req = os.path.join(os.path.dirname(__file__), "requirements.txt")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req, "-q"])

def open_browser():
    time.sleep(1.5)
    webbrowser.open("http://localhost:5000")

if __name__ == "__main__":
    print("StatR – Installiere Abhängigkeiten...")
    install_deps()
    print("Starte Server auf http://localhost:5000 ...")
    threading.Thread(target=open_browser, daemon=True).start()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    import app
    app.app.run(debug=False, port=5000)
