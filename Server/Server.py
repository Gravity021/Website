import flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return flask.render_template("home.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/projects")
def projects():
    return flask.render_template("projects.html")

@app.route("/testing")
def testing():
    return flask.render_template("testing.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0", 
        port=80,
        debug=True
    )