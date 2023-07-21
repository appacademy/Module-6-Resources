from random import randint
from pprint import pprint
from datetime import datetime
from flask import Blueprint, render_template, url_for, redirect
from ..forms import PostForm
from app.models import Post, User, db

post_routes = Blueprint("post_routes", __name__, url_prefix="/posts")

@post_routes.route("/all")
def feed():
  posts = Post.query.all()
  posts_list = [post.to_dict() for post in posts]
  
  return render_template("feed.html", posts=posts_list)

@post_routes.route("/new", methods=["GET", "POST"])
def get_post_form():
  form = PostForm()
  users = db.session.query(User).all()
  form.author.choices = [(user.id, user.username) for user in users]
  if form.validate_on_submit():
    user_id = form.data["author"]
    post = {
      "user_id": user_id,
      "caption": form.data["caption"],
      "image": form.data["image"],
      "date": datetime.now(),
    }
    # posts.append(post)
    new_post= Post(**post)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("post_routes.feed"))
  
  if form.errors:
    print(form.errors)
    return form.errors
  
  return render_template("post-form.html", post=form)

@post_routes.route("/delete/<int:id>")
def delete_post(id):
  post_to_delete = Post.query.get(id)
  db.session.delete(post_to_delete)
  db.session.commit()
  return redirect("/posts/all")
    
    
    
  