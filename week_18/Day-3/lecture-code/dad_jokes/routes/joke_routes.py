from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User

jokes_router = Blueprint("jokes", __name__, url_prefix="/jokes")

print("Dunder name in joke blueprint", __name__)


@jokes_router.route('/all')
def all_jokes():
    """
    Returns all jokes in database
    """
    jokes = Joke.query.order_by(Joke.rating).all()
    return render_template('all_jokes.html', jokes=jokes)


@jokes_router.route('/<int:id>')
def one_joke(id):
    one_joke = Joke.query.get(id)
    # one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke with that ID"
    return render_template('all_jokes.html', jokes=[one_joke])


@jokes_router.route("/new", methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()
    form.user.choices = [(user.id, user.username) for user in User.query.all()]
    print(form.user.choices)

    if form.validate_on_submit():
        print(form.data["user"])
        selected_user = User.query.get(form.data["user"])
        print(selected_user)

        new_joke = Joke(
            joke_body=form.data['joke'],
            punchline=form.data['punchline'],
            rating=form.data['rating'],
            user=selected_user
        )

        print(new_joke)
        db.session.add(new_joke)
        db.session.commit()
        return redirect('/jokes/all')


    if form.errors:
          return form.errors  

    return render_template("joke_form.html", form=form)