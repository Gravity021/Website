import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/error_testing")
def error_testing():
    return "", 304

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=80,
        debug=True
    )