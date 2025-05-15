from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
  return render_template("index.html")
@app.route('/index.html')
def index():
  return render_template("index.html")
@app.route('/webstates.html')
def webstates():
  return render_template("webstates.html")
@app.route('/updates.html')
def updates():
  return render_template("updates.html")
@app.route('/pagenotfound.html')
def pagenotfound():
  return render_template("pagenotfound.html")
