from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    context = {
        "home" : "nav-link active",
        "about" : "nav-link"
    }
    return render_template("home.html", **context)


@app.route("/about/")
def about():
    context = {
        "home" : "nav-link",
        "about" : "nav-link active"
    }
    return render_template("about.html", **context)

if __name__ == "__main__":
    app.run()