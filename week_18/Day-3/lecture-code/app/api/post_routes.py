from random import randint
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect
from ..posts import posts
from ..forms import Post

post_routes = Blueprint("post_routes", __name__, url_prefix="/posts")

@post_routes.route("/all")
def feed():
  return render_template("feed.html", posts=posts)

@post_routes.route("/new", methods=["GET", "POST"])
def get_post_form():
  form = Post()
  print(form.data)
  if form.validate_on_submit():
    post = {
      "id": len(posts) + 1,
      "author": form.data["author"],
      "caption": form.data["caption"],
      "image": form.data["image"],
      "date": datetime.now(),
      "likes": randint(0,100)
    }
    posts.append(post)
    return redirect(url_for("post_routes.feed"))
  
  if form.errors:
    print(form.errors)
    return form.errors
    
    
    
  
  return render_template("post-form.html", post=form)