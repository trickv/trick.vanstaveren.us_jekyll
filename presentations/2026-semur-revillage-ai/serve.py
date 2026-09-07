#!/usr/bin/env python3
"""Serve the deck and a phone remote that follows it.

    python3 serve.py            # port 8765
    python3 serve.py 9000       # custom port

Laptop:  http://localhost:8765/          (present from this tab; F for fullscreen)
Phone:   http://<laptop-ip>:8765/remote  (Tailscale IP or MagicDNS name works)

Stdlib only. The deck POSTs its state here on every change; the phone POSTs
commands; everything is rebroadcast to all listeners over server-sent events.
Anyone who can reach this port can drive the deck, so keep it on your tailnet.
"""
import http.server, json, queue, socket, subprocess, sys, threading
from pathlib import Path

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
ROOT = Path(__file__).resolve().parent
DECK = "ai-coffee-chat.html"

clients = set()
lock = threading.Lock()
last_state = None


def broadcast(msg: str):
    with lock:
        for q in list(clients):
            q.put(msg)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/events":
            return self.sse()
        if path == "/":
            self.path = "/" + DECK
        elif path == "/remote":
            self.path = "/remote.html"
        return super().do_GET()

    def sse(self):
        q = queue.Queue()
        with lock:
            clients.add(q)
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        try:
            if last_state:
                self.wfile.write(f"data: {last_state}\n\n".encode())
                self.wfile.flush()
            while True:
                try:
                    msg = q.get(timeout=15)
                    self.wfile.write(f"data: {msg}\n\n".encode())
                except queue.Empty:
                    self.wfile.write(b": ping\n\n")
                self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError, OSError):
            pass
        finally:
            with lock:
                clients.discard(q)

    def do_POST(self):
        global last_state
        n = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(n).decode("utf-8", "replace")
        try:
            msg = json.loads(body)
        except ValueError:
            self.send_response(400); self.end_headers(); return
        if msg.get("type") == "state":
            last_state = body
        broadcast(body)
        self.send_response(204)
        self.end_headers()

    def log_message(self, *a):
        pass


def addresses():
    found = []
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        found.append(("lan", s.getsockname()[0]))
        s.close()
    except OSError:
        pass
    for cmd in (["tailscale", "ip", "-4"],
                ["/Applications/Tailscale.app/Contents/MacOS/Tailscale", "ip", "-4"]):
        try:
            ip = subprocess.run(cmd, capture_output=True, text=True, timeout=3).stdout.strip().splitlines()
            if ip:
                found.append(("tailscale", ip[0]))
                break
        except (OSError, subprocess.SubprocessError):
            pass
    return found


if __name__ == "__main__":
    srv = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"deck    http://localhost:{PORT}/")
    for kind, ip in addresses():
        print(f"remote  http://{ip}:{PORT}/remote   ({kind})")
    print("Ctrl-C to stop")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
