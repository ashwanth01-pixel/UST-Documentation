from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Server!")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
    print("Server running on port 8000")
    server.serve_forever()
