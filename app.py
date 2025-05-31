from flask import Flask, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "Diggy Gorgonzola"




users_db = {"pass1234":"Diggy"} # database, I'll fix this later
post_db = SQLAlchemy(app)

SQLALCHEMY_BINDS = {}
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
with app.app_context():
     db.create_all()
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

@app.route('/posts.html')
def posts():
    all_posts = Post.query.all()
    return render_template('posts.html', posts=all_posts)


@app.route('/new_post.html', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        # assuming user_id is 1 for now
        post = Post(title=title, content=content, user_id=1)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template('new_post.html')

@app.route('/login.html', methods=["GET", "POST"])
def login():
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    if username == users_db[password]:
      return redirect('/posts.html')
    else:
      return redirect('/index.html')
  return render_template("login.html")
