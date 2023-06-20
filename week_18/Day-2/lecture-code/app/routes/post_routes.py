from random import randint
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for
from ..posts import posts
from ..forms.post_form import PostForm

post_routes = Blueprint("posts", __name__)

# print(__name__)

@post_routes.route("/all")
def all_posts():
  return render_template("feed.html", posts=posts)

@post_routes.route("/<int:id>")
def get_post_by_id(id):
    one_post = [post for post in posts if post["id"] == id]
    # print(one_post)
    return render_template("feed.html", posts=one_post)

    
@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
  form = PostForm()
  # print(form.caption.label)
  
  if form.validate_on_submit():
    post_dict = {
      "author": form.data["author"],
      "caption": form.data["caption"],
      "image": form.data["image"],
      "likes": randint(1, 10),
      "id": max([post["id"] for post in posts]) + 1,
      "date": datetime.now()
    }
    posts.append(post_dict)
    return redirect(url_for("posts.all_posts"))
  
  print(form.errors)
  if form.errors:
    return render_template("post_form.html", form=form, errors=form.errors)
  

  return render_template("post_form.html", form=form)