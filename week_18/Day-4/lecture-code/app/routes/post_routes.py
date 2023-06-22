from random import randint
from datetime import date
from flask import Blueprint, render_template, redirect, url_for
from ..forms.post_form import PostForm
from ..models import Post, User, db


post_routes = Blueprint("posts", __name__)

# print(__name__)

@post_routes.route("/all")
def all_posts():
  all_posts = Post.query.order_by(Post.post_date.desc()).all()
  print(all_posts)
  response_posts = [post.to_dict() for post in all_posts]
  print(response_posts)
  # return render_template("feed.html", posts=all_posts)
  return response_posts


@post_routes.route("/<int:id>")
def get_post_by_id(id):
    # one_post = [post for post in posts if post["id"] == id]
    # print(one_post)
    one_post = Post.query.get(id)
    print(one_post)
    return render_template("feed.html", posts=[one_post])

    
@post_routes.route("/new", methods=["GET", "POST"])
def new_post():
  form = PostForm()
  # print(form.caption.label)
  form.user_id.choices = [ (user.id, user.username) for user in User.query.all()]
  # print(form.author.choices)
  
  if form.validate_on_submit():
    selected_user = User.query.get(form.data["user_id"])
    print(selected_user)

    new_post = Post(
      caption = form.data["caption"],
      image = form.data["image"],
      user = selected_user,
      post_date = date.today(),
    )
    print(new_post)
    db.session.add(new_post)
    db.session.commit()
    return redirect(url_for("posts.all_posts"))
  
  print(form.errors)
  if form.errors:
    return render_template("post_form.html", form=form, errors=form.errors)
  

  return render_template("post_form.html", form=form)



@post_routes.route("/update/<int:id>", methods=["GET", "POST"])
def update_post(id):
  form = PostForm()

  form.user_id.choices = [ (user.id, user.username) for user in User.query.all()]
  print(form.user_id.choices)

  if form.validate_on_submit():
    post_to_update = Post.query.get(id)

    selected_user = User.query.get(form.data["user_id"])
    post_to_update.user = selected_user
    post_to_update.caption = form.data["caption"]
    post_to_update.image = form.data["image"]
    post_to_update.post_date = date.today()
    db.session.commit()
    return redirect("/posts/all")


  elif form.errors:
    return render_template("post_form.html", form=form, errors=form.errors, type="update", id=id)


  else:
    current_data = Post.query.get(id)
    form.process(obj=current_data)
    return render_template("post_form.html", form=form, errors=None, type="update", id=id)


@post_routes.route("/delete/<int:id>")
def delete_post(id):
  post_to_delete = Post.query.get(id)
  db.session.delete(post_to_delete)
  db.session.commit()
  return redirect("/posts/all")

  