def app(environ, start_response):
    f = open("index.html", "rb")
    data = f.read()
    status = "200 OK"
    response_headers = [("Content-type", "text/html")]
    start_response(status, response_headers)
    return [data]


#  waitress-serve --listen=127.0.0.1:5001 server:app
# No windows executar no terminal este servidor de aplicação ao invés do gunicorn
