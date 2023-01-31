from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
# import sqlite3

# DB_FILE = "dev.db"

joke_routes = Blueprint('jokes', __name__, url_prefix='/jokes')

print('inside jokes BP file',__name__)



# def create_joke(joke_body, punchline, rating):
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
#         print("New joke created!")


@joke_routes.route("/all")
def get_all_jokes():
    """Route to return and display all the jokes we have"""
    # all_joke = Joke.query.all()
    return render_template("all-jokes.html", jokes=jokes)



@joke_routes.route("/<int:id>")
def get_joke_by_id(id):
    print(id)
    one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke"
    return render_template("all-jokes.html", jokes=[one_joke])



@joke_routes.route("/new", methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    # Handles post requests
    if form.validate_on_submit():
        # create_joke(form.data["joke"], 
        #     form.data["punchline"],
        #     form.data["rating"],
        # )
        new_joke = {
            "jokeid": len(jokes) + 1,
            "joke": form.data["joke"],
            "punchline": form.data["punchline"],
            "rating": form.data["rating"]
        }
        jokes.append(new_joke)
        return redirect("/jokes/all")

    if form.errors:
        return form.errors

    return render_template("joke-form.html", form=form)

