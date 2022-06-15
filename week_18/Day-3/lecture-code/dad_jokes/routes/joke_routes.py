from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models.db import db, Joke, User


jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')

@jokes_router.route('/all')
def all_jokes():
    jokes = Joke.query.order_by(Joke.rating).all()
    # print(jokes)

    # author = User.query.get(1) 
    # print("Jokes from user 1", author.jokes)

    # author_jokes = Joke.query.join(User).filter(User.username.like("Brad")).all()
    # print("Long long query results", author_jokes)

    return render_template("all_jokes.html", jokes=jokes)


@jokes_router.route('/<int:id>')
def one_joke(id):
    print(id)
    one_joke = Joke.query.get(id)
    print(one_joke.to_dict())
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    form.user.choices = [ (user.id, user.username) for user in User.query.all() ]
    print(form.user.choices)

    if form.validate_on_submit():
    
        # UPDATING A RESOURCE
        # selected_user = User.query.get(form.data['user'])
        # selected_user.username = "Bradley"
        # db.session.commit()

        # DELETING A RESOURCE
        # selected_user = User.query.get(form.data['user'])
        # db.session.delete(selected_user)
        # db.session.commit()

        print(selected_user)

        new_joke = Joke(
            joke_body=form.data['joke'],
            punchline=form.data['punchline'],
            rating=form.data['rating'],
            user = selected_user
        )
        print(new_joke)
        db.session.add(new_joke)
        db.session.commit()
        return redirect("/jokes/all")

    if form.errors:
       return form.errors

    return render_template("joke_form.html", form=form)