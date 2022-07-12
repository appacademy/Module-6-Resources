from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm

jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')


@jokes_router.route('/all')
def all_jokes():
    print("inside all jokes", __name__)
    return render_template("all_jokes.html", jokes=jokes)


@jokes_router.route('/<int:id>')
def get_joke_by_id(id):
    print(id)
    one_joke = jokes[id - 1] if id <= len(jokes) else "No joke for you!"
    print(one_joke)
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def create_joke():
    form = NewJokeForm()

    if form.validate_on_submit():
        new_joke = {
            'jokeid': len(jokes) + 1,
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        jokes.append(new_joke)
        return redirect('/jokes/all')

    if form.errors:
        return form.errors                

    return render_template("joke_form.html", form=form)