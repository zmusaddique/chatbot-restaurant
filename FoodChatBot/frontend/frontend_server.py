# Serve a specific HTML file
import http.server

PORT = 5500  # Change this to your desired port
HTML_FILE = "home.html"  # Change this to your HTML file's name

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    ".html": "text/html",
})

with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"Serving {HTML_FILE} on port {PORT}")
    httpd.serve_forever()

