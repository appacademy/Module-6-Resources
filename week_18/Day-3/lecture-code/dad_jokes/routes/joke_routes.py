from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User


joke_routes = Blueprint('jokes', __name__, url_prefix='/jokes')

print('inside jokes BP file',__name__)


@joke_routes.route("/all")
def get_all_jokes():
    """Route to return and display all the jokes we have"""
    all_jokes = Joke.query.order_by(Joke.rating).all()
    print([joke.to_dict() for joke in all_jokes])
    return render_template("all-jokes.html", jokes=all_jokes)



@joke_routes.route("/<int:id>")
def get_joke_by_id(id):
    print(id)
    # one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke"
    one_joke = Joke.query.get(id)
    return render_template("all-jokes.html", jokes=[one_joke])



@joke_routes.route("/new", methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    form.user.choices = [(user.id, user.username) for user in User.query.all()]
    print("User choices", form.user.choices)
    # Handles post requests
    if form.validate_on_submit():
        selected_user = User.query.get(form.data["user"])
        print(selected_user)

        new_joke = Joke(
            joke_body= form.data["joke"],
            punchline= form.data["punchline"],
            rating= form.data["rating"],
            user=selected_user
        )
        db.session.add(new_joke)
        db.session.commit()
        return redirect("/jokes/all")

    if form.errors:
        return form.errors

    return render_template("joke-form.html", form=form)



# UPDATING A RECORD
# selected_user = User.query.get(form.data["user"])
# selected_user.username = "Bradley"
# db.session.commit()


# # DELETE A RECORD
# selected_user = User.query.get(form.data["user"])
# db.session.delete(selected_user)
# db.session.commit()









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