from flask import Blueprint, render_template
from ..db_jokes import jokes


joke_router = Blueprint('jokes', __name__, url_prefix="/jokes")


print("inside the jokes blueprint file", __name__)


@joke_router.route('/all')  #  URL is now /jokes/all
def all_jokes():
    # eventually we will query our DB  jokes = Joke.query.all()
    return render_template("all_jokes.html", jokes=jokes)


@joke_router.route('/<int:id>')
def get_joke_by_id(id):
    print(id)
    one_joke = jokes[id -1] if id <= len(jokes) else "No Joke at this ID!"
    # joke = Joke.query.get(id)
    print(one_joke)
    return render_template("all_jokes.html", jokes=[one_joke])