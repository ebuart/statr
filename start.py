import subprocess
import sys
import os
import socket
import threading
import time
import webbrowser

def install_deps():
    req = os.path.join(os.path.dirname(__file__), "requirements.txt")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req, "-q"])

def free_port(preferred=5000):
    """Nimm den Wunsch-Port, sonst den nächsten freien (macOS AirPlay belegt oft 5000)."""
    for p in [preferred] + list(range(5001, 5050)):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("127.0.0.1", p)) != 0:
                return p
    return preferred

def open_browser(port):
    time.sleep(1.5)
    webbrowser.open(f"http://localhost:{port}")

if __name__ == "__main__":
    print("StatR – Installiere Abhängigkeiten...")
    install_deps()
    port = int(os.environ.get("PORT") or free_port(5000))
    print(f"Starte Server auf http://localhost:{port} ...")
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    import app
    app.app.run(debug=False, port=port)
