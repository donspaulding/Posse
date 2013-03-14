import time
import json
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

msg = """
event: {name}
data: {data}

"""

class SSEHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200, "OK")
		req = self.path.replace('/', '')
		if req != "sse":
			self.send_header("Content-type", "text/html")
			self.end_headers()
			self.wfile.write(open(req).read())
			self.wfile.flush()
			return
		self.send_header("Content-type", "text/event-stream")
		self.end_headers()
		while True:
			time.sleep(3)
			self.wfile.write(msg.format(name="server-time", data=json.dumps({'time': time.time()})))
			self.wfile.flush()

if __name__ == '__main__':
	HTTPServer(('', 8000), SSEHandler).serve_forever()