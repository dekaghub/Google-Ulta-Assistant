from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('base.html')

@app.route("/partial/")
def partial():
    return render_template("partial.html")

