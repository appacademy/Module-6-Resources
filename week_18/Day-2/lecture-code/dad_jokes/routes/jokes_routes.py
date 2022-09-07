from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm

jokes_router = Blueprint('jokes', __name__, url_prefix="/jokes")

print("inside jokes blueprint", __name__)



@jokes_router.route("/all")
def all_jokes():
    # jokes = Joke.query.all()
    return render_template("all_jokes.html", jokes=jokes)



@jokes_router.route("/<int:id>")
def one_joke(id):
    print(id)
    one_joke = jokes[id-1]

    # one_joke = Joke.query.get(id)
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    # users = User.query.all()
    # form.user.choices = users

    if form.validate_on_submit():
        new_joke = {
            'jokeid': len(jokes) + 1,
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        print(new_joke)
        jokes.append(new_joke)

        return redirect("/jokes/all")

    if form.errors:
        return form.errors

    # handle form submission stuff here

    return render_template("joke_form.html", form=form)
