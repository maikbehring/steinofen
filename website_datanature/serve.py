#!/usr/bin/env python3
"""
Einfacher HTTP-Server für die datanature-Website
"""

import http.server
import socketserver
import os
from pathlib import Path

PORT = 8001

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Füge CORS-Header hinzu
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

def main():
    # Wechsle ins Website-Verzeichnis
    os.chdir(Path(__file__).parent)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"Server läuft auf http://localhost:{PORT}")
        print(f"Öffne im Browser: http://localhost:{PORT}/index.html")
        print("Drücke Ctrl+C zum Beenden")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer beendet")

if __name__ == "__main__":
    main()

