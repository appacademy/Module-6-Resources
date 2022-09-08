from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User

jokes_router = Blueprint('jokes', __name__, url_prefix="/jokes")

# print("inside jokes blueprint", __name__)



@jokes_router.route("/all")
def all_jokes():
    jokes = Joke.query.order_by(Joke.rating).all()
    return render_template("all_jokes.html", jokes=jokes)


@jokes_router.route("/<int:id>")
def one_joke(id):
    print(id)
    # one_joke = jokes[id-1]
    one_joke = Joke.query.get(id)
    print(one_joke.to_dict())
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()
    form.user.choices = [ (user.id, user.username) for user in User.query.all()]
    print(form.user.choices)
   
    if form.validate_on_submit():
        select_user = User.query.get(form.data['user'])
        print(select_user)

        new_joke = Joke(
            joke_body= form.data['joke'],
            punchline= form.data['punchline'],
            rating= form.data['rating'],
            user=select_user
        )

        print(new_joke)
        db.session.add(new_joke)
        db.session.commit()
        return redirect("/jokes/all")

    if form.errors:
        return form.errors

    # handle form submission stuff here

    return render_template("joke_form.html", form=form)


# UPDATE A RESOURCE
# select_user = User.query.get(1)  # Brad resource
# select_user.username = "Bradley"
# db.session.commit()

# selected_user = User.query.get(1)
# selected_joke = Joke.query.get(1)
# if select_user not in selected_joke.joke_likes:
#     selected_joke.joke_likes.append(select_user)
# db.session.commit()


# DELETING A RESOURCE
# selected_user = User.query.get(1)
# db.session.delete(select_user)
# db.session.commit()
