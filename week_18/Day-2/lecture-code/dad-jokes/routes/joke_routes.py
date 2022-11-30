from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms import NewJokeForm


jokes_routes = Blueprint('joke', __name__, url_prefix="/jokes") 

print(__name__)


@jokes_routes.route("/all")
def all_jokes():
    # with sqlite3.connect(DB_FILE) as conn:
    #     curs = conn.cursor()
    #     curs.execute(
    #         """
    #         SELECT * FROM jokes;
    #         """
    #     )    
    #     results = curs.fetchone()
    #     print(results)
    # jokes = Joke.query.all()
    return render_template("all_jokes.html", jokes=jokes)


@jokes_routes.route("/<int:id>")
def joke_by_id(id):
    print(id)
    one_joke = jokes[id - 1]
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_routes.route("/new", methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    if form.validate_on_submit():
        # make new resource
        new_joke = {
            'jokeid': len(jokes) + 1,
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        print(new_joke)
        jokes.append(new_joke)
        return redirect('/jokes/all')

    if form.errors:
        return form.errors


    return render_template("joke_form.html", form=form)

# /
# /jokes/all
# /jokes/new
# /users/all