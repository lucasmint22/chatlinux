import webview
import socket
import threading
import time

CHECK_HOST = "chat.openai.com"
CHECK_PORT = 443

def is_online():
    try:
        socket.create_connection((CHECK_HOST, CHECK_PORT), timeout=3)
        return True
    except:
        return False

def network_watcher(window):
    last = None
    while True:
        online = is_online()
        if online != last:
            if online:
                window.load_url("https://chat.openai.com")
            else:
                window.load_html("""
                    <html>
                    <body style="background:#1e1e1e;color:white;
                                 display:flex;align-items:center;justify-content:center;
                                 font-family:monospace;">
                        <div>
                            <h1>⚠ Offline</h1>
                            <p>No internet connection detected.</p>
                        </div>
                    </body>
                    </html>
                """)
            last = online
        time.sleep(5)

def main():
    window = webview.create_window("ChatGPT Desktop", width=1100, height=720)
    t = threading.Thread(target=network_watcher, args=(window,), daemon=True)
    t.start()
    webview.start(gui='gtk')

if __name__ == "__main__":
    main()
