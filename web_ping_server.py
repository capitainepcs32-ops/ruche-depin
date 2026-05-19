from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Ruche Active</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>Statut : OK. Algorithmes en cours d execution.</p></body></html>", "utf-8"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    webServer = HTTPServer(("0.0.0.0", port), MyServer)
    print(f"Serveur anti-veille lance sur le port {port}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
  
