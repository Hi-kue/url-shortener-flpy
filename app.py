from flask import Flask, request, redirect, render_template
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        urls_shortened= 1523,
        users= '4.3k',
        img_shortened= '1.3k'
    )

@app.route('/about', methods=['GET'])
def about_section():
    return 'This is a URL Shortener API'


if __name__ == '__main__':
    http_server = WSGIServer(('127.0.0.0', 5000), app)
    http_server.serve_forever()