from flask import Flask, render_template, redirect
from .config import Config
# from .helpers.helper1 import add2, add4
# from .helpers.helper2 import add6, add8, vals  
# from .helpers import add2, add4, add6, add8, add10, vals
from .posts import posts


app = Flask(__name__)
print(__name__)
app.config.from_object(Config)



@app.route("/")
def index():
    """renders the home/index page"""
    # return render_template("index.html")
    return redirect("/another")



@app.route("/another")
def another_route():
    return "<h1>This is another route!</h1>"



@app.route("/all")
def view_all_posts():
    # all_posts = Post.query.all()
    return render_template("feed.html", posts=posts)



@app.route("/<int:id>")
def post_by_id(id):
    # post = Post.guery.get(id)
    one_post = [post for post in posts if post['id'] == id]
    print(one_post)
    return render_template("feed.html", posts=one_post)



