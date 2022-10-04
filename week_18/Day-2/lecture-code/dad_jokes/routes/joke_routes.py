from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm


joke_router = Blueprint('jokes', __name__, url_prefix="/jokes")


# print("inside the jokes blueprint file", __name__)


@joke_router.route('/all')  #  URL is now /jokes/all
def all_jokes():
    # eventually we will query our DB  jokes = Joke.query.all()
    return render_template("all_jokes.html", jokes=jokes)



@joke_router.route('/<int:id>')
def get_joke_by_id(id):
    # print(id)
    one_joke = jokes[id -1] if id <= len(jokes) else "No Joke at this ID!"
    # joke = Joke.query.get(id)
    # print(one_joke)
    return render_template("all_jokes.html", jokes=[one_joke])



@joke_router.route('/new', methods=["GET", "POST"])
def create_new_joke():
    form = NewJokeForm()

    if form.validate_on_submit():
        new_joke = {
            'jokeid': len(jokes),
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        
        jokes.append(new_joke)
        return redirect('/jokes/all')
# If we were connecting to the DB we would add this code to make the resource    
#     with sqlite3.connect(DB_FILE) as conn:
#         curs = conn.cursor()
#         curs.execute(
#             """
#             INSERT INTO jokes(joke_body, punchline, rating)
#             VALUES (:joke_body, :punchline, :rating)    
#             """,
#             {
#                 "joke_body": joke_body,
#                 "punchline": punchline,
#                 "rating": rating
#             }
#         )

    if form.errors:
        return form.errors


    return render_template("joke_form.html", form=form)