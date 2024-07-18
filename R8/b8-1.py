from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse
from datetime import datetime

events = [
    {"id": 1, "name": "東京オリンピック", "date": "2020-08-01"},
    {"id": 2, "name": "カタールワールドカップ", "date": "2022-09-15"},
    {"id": 3, "name": "パリオリンピック", "date": "2024-07-30"},
]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = urlparse.urlparse(self.path)
        query_string = url_components.query
        query_params = urlparse.parse_qs(query_string)
        event_id = int(query_params.get('id', [0])[0])

        event = next((event for event in events if event["id"] == event_id), None)
        
        if event:
            event_date = datetime.strptime(event["date"], "%Y-%m-%d")
            today = datetime.now()
            is_future_event = event_date > today
            color = "red" if is_future_event else "black"
            days_left = (event_date - today).days if is_future_event else "Event has passed"

            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"""
                <!DOCTYPE html>
                <html>
                <head><title>Event {event_id}</title></head>
                <body>
                    <h1 style="color: {color};">{event['name']}</h1>
                    <p>Date: {event['date']}</p>
                    <p>Days left: {days_left}</p>
                </body>
                </html>
            """.encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write("<html><body><h1>Event not found</h1></body></html>".encode('utf-8'))

def run(server_class=HTTPServer, handler_class=MyServer, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
