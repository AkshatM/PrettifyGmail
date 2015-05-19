import BaseHTTPServer as bhttp
from urlparse import urlparse as parser
from crawler import crawler

port = 5000

'''Implements BaseHTTPServer that runs the crawler before responding to a GET request.

GET request from client is URL-encoded i.e. desired URL is passed as a field in the response.

For instance, if I wanted to link to www.google.com, I could do:

GET www.example.com:<port>/?https://www.google.com

The class Handler allows me to define the GET response.'''

class Handler(bhttp.BaseHTTPRequestHandler):        

    def do_GET(self):
        requests_response = crawler(parser(self.path).query)
        if requests_response != 'ERR':
            self.send_response(200)
            self.send_header("Content-type", requests_response[-1])
            self.end_headers()
            self.wfile.write(requests_response[0])
        else:
            self.send_error(400)

if __name__ == '__main__':
    server = bhttp.HTTPServer(('localhost', port), Handler) #alter localhost to actual IP
    print('Starting server, use a KeyboardInterrupt to stop')
    server.serve_forever()
        
        
    
