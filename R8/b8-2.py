from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from datetime import datetime

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write("""
            <!DOCTYPE html>
            <html>
            <head><title>イベントまでの残り日時</title></head>
            <body>
                <h1>イベントまでの残り日時</h1>
                <form method="POST">
                    <label for="name">Event Name:</label>
                    <input type="text" id="name" name="name" required><br>
                    <label for="date">Event Date (YYYY-MM-DD):</label>
                    <input type="date" id="date" name="date" required><br>
                    <input type="submit" value="Submit">
                </form>
            </body>
            </html>
        """.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_params = urlparse.parse_qs(post_data.decode('utf-8'))
        event_name = post_params.get('name', [''])[0]
        event_date = post_params.get('date', [''])[0]

        try:
            event_date_obj = datetime.strptime(event_date, "%Y-%m-%d")
            today = datetime.now()
            days_left = (event_date_obj - today).days
            response = f"{event_name}まで、あと{days_left}日です。"
        except ValueError:
            response = "Invalid date format. Please use YYYY-MM-DD."

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(f"<p>{response}</p>".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
