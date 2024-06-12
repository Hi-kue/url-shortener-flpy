from flask import Flask, request, redirect, render_template, url_for
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
CORS(app)


# Handling Improper Routes
@app.errorhandler(404)
def page_not_found(e: Exception):
    return render_template(
        "error.html",
        error_code=404,
        reason="Whoops! The Page you are Looking for is not Found!"
    ), 404


@app.errorhandler(500)
def internal_server_error(e: Exception):
    return render_template(
        "error.html",
        error_code=500,
        reason="Whoops! Something went wrong on our end!"
    ), 500


@app.errorhandler(405)
def method_not_allowed(e: Exception):
    return render_template(
        "error.html",
        error_code=405,
        reason="Provided Method is not Allowed; please use POST Method instead."
    )


@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        urls_shortened=1523,
        users="4.3k",
        img_shortened="1.3k"
    )


@app.route("/about", methods=["GET"])
def about_section():
    return "This is a URL Shortener API"


@app.route("/url", methods=["GET", "POST"])
def your_url():
    if request.method == "POST":
        return render_template("your_url.html", url=request.form["url"])
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    http_server = WSGIServer(("127.0.0.0", 8080), app)
    http_server.serve_forever()
