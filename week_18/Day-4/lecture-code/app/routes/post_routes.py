from flask import Blueprint, render_template, redirect
from ..posts import posts as seed_posts
from ..forms.post_form import PostForm
from datetime import date
from random import randint
from ..models import db, Post, User


posts = Blueprint("posts", __name__)

# print("inside the post BP",__name__)


@posts.route("/all")
def get_all_posts():
    # Query for all posts
    posts = Post.query.order_by(Post.post_date.desc()).all()
    # print(posts)
    # sorted_posts = sorted(seed_posts, key=lambda post: post['date'], reverse=True)
    # return render_template("feed.html", posts=posts)
    response = [post.to_dict() for post in posts]
    print(response)
    return response


@posts.route("/<int:id>")
def get_post_by_id(id):
    print(id)
    # Query
    one_post=Post.query.get(id)
    # one_post = [post for post in seed_posts if post['id'] == id]
    print(one_post)
    print(one_post.to_dict())
    return render_template("feed.html", posts=[one_post])



@posts.route("/new", methods=['GET', 'POST'])
def create_new_post():
    '''renders an empty form on a get route, validates 
    the form and creates a new post resource on post 
    requests
    '''
    form = PostForm()
    
    # print(form.data['author'])

    form.author.choices = [ (user.id, user.username) for user in User.query.all()]
    # print(form.author.choices)

    if form.validate_on_submit():

        selected_user = User.query.get(form.data["author"])
        print(selected_user)
        #enter block and create our resource
        new_post = Post(
            user=selected_user,
            caption= form.data["caption"],
            image= form.data["image_url"],
            post_date= date.today(),
        )
        print(new_post)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts/all")

    if form.errors:
        print(form.errors)
        return render_template("post_form.html", form=form, errors=form.errors)

    # form.author.choices = #get from the DB
    return render_template("post_form.html", form=form, errors=None)



# UPDATE
# selected_user = User.query.get(form.data["user"])
# selected_user.username = "Brad"
# db.session.commit()

# selected_post = Post.query.get(1)
# user_to_like = User.query.get(1)
# if user_to_like not in selected_post.user_likes:
#     selected_post.user_likes.append(user_to_like)
# db.session.commit()

# DELETE
# selected_user = User.query.get(3)
# db.session.delete(selected_user)
# db.session.commit()
