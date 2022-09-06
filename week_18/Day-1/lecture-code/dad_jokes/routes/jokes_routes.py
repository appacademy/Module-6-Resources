from flask import Blueprint, render_template
from ..db_jokes import jokes

jokes_router = Blueprint('jokes', __name__, url_prefix="/jokes")

print("inside jokes blueprint", __name__)



@jokes_router.route("/all")
def all_jokes():
    # jokes = Joke.query.all()
    return render_template("all_jokes.html", jokes=jokes)