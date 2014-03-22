#!/usr/bin/python

# This will listen on port 80 and redirect any HTTP requests to KA Lite on port 8008.
# Run this in the background using:
# sudo python redirect_port80_to_port8008.py &

import BaseHTTPServer

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_HEAD(self):
        host = self.headers.get("host", "1.1.1.1").split(":")[0]
        self.send_response(302)
        self.send_header("Location", "http://%s:8008/" % host)
        self.end_headers()

    def do_GET(self):
        self.do_HEAD()

if __name__ == '__main__':
    try:
        httpd = BaseHTTPServer.HTTPServer(("", 80), RedirectHandler)
    except:
        # print "Port 80 is in use or could not be acquired; exiting redirect script."
        exit(1)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
