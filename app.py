from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/blogs")
def blogs():
    return render_template("main.html")
@app.route("/firstblog")
def firstblog():
    return render_template("introduction.html")
@app.route("/latestvid")
def latestvideo():
    return render_template("latestvid.html")
@app.route("/pagenotfound")
def pagenotfound():
    return render_template("404.html")
