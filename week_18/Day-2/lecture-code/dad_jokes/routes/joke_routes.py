from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm

# # IF we are connecting to the DB, we need this code
# import psycopg2

# CONNECTION_PARAMETERS = {
#     "dbname": 'dadjokes',
#     "user": 'dadjokesuser',
#     "password": 'jokes'
# }


jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')

@jokes_router.route('/all')
def all_jokes():
    print("inside jokes",__name__)
    return render_template("all_jokes.html", jokes=jokes)


@jokes_router.route('/<int:id>')
def one_joke(id):
    print(id)
    one_joke = jokes[id] if id < len(jokes) else "No Joke at this ID!"
    print(one_joke)
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    if form.validate_on_submit():
        new_joke = {
            'jokeid': len(jokes),
            'joke': form.data['joke'],
            'punchline': form.data['punchline'],
            'rating': form.data['rating']
        }
        jokes.append(new_joke)
        

        # with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        #     with conn.cursor() as curs:
        #         curs.execute(
        #             """
        #             INSERT INTO jokes (joke_body, punchline, rating)
        #             VALUES (%(joke_body)s, %(punchline)s, %(rating)s)
        #             """,
        #             {
        #                 "joke_body": form.data['joke'],
        #                 "punchline": form.data['punchline'],
        #                 "rating": form.data['rating']
        #             }
        #         )
            
        return redirect("/jokes/all")

    if form.errors:
       return form.errors

    return render_template("joke_form.html", form=form)