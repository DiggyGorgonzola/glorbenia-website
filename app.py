from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

users_db = {"pass1234":"Diggy"} # database, I'll fix this later

app = Flask(__name__)
app.secret_key = "Diggy Gorgonzola"


@app.route('/')
def home():
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

@app.route('/citizenship.html')
def citizenship():
  return render_template("citizenship.html")

@app.route('/glorbgames.html')
def index():
  return render_template("glorbgames.html")



@app.route('/login.html', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    if username == users_db[password]:
      return redirect('/index.html')
    else:
      return redirect('/citizenship.html')
  return render_template("login.html")
