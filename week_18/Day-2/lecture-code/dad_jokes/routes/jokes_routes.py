from flask import Blueprint, render_template, redirect
from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
# import sqlite3

jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')

# DB_FILE='dev.db'

@jokes_router.route('/all')
def all_jokes():
    print("from jokes routes", __name__)
    # Eventually we will query our DB for the jokes here
    return render_template('all_jokes.html', jokes=jokes)    


@jokes_router.route('/<int:id>')
def one_joke(id):
    one_joke = jokes[id-1] if id <= len(jokes) else "No Joke with that ID"
    # print(one_joke)
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()

    if form.validate_on_submit():
        # IF we wanted to save to the DB 
        # with sqlite3.connect(DB_FILE) as conn:
        #     curs = conn.cursor()
        #     curs.execute(
        #         """
        #         INSERT INTO jokes (joke_body, punchline, rating)
        #         VALUES(:joke_body, :punchline, :rating)
        #         """,
        #         {
        #             "joke_body": form.data['joke'],
        #             "punchline": form.data['punchline'],
        #             "rating": form.data['rating']
        #         }
        #     )
        #     return redirect("/jokes/all")

        # Making a new resource in our jokes file    
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


    return render_template('joke_form.html', form=form)
