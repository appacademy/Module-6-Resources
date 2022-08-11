from flask import Blueprint, render_template, redirect, request
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User
# import sqlite3

jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')

# DB_FILE='dev.db'

@jokes_router.route('/all')
def all_jokes():
    print("from jokes routes", __name__)
    jokes = Joke.query.order_by(Joke.rating).all()
    # Eventually we will query our DB for the jokes here
    return render_template('all_jokes.html', jokes=jokes)    


@jokes_router.route('/<int:id>')
def one_joke(id):
    # one_joke = jokes[id-1] if id <= len(jokes) else "No Joke with that ID"
    one_joke = Joke.query.get(id)
    print(one_joke.to_dict())
    return render_template("all_jokes.html", jokes=[one_joke])


@jokes_router.route('/new', methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()



    form.user.choices = [(user.id, user.username) for user in User.query.all()]
    print(form.user.choices)

    if request.method == "POST":
        pass
        # DO LOGIC HERE

    if form.validate_on_submit():
        print("User ID from form", form.data['user'])
        selected_user = User.query.get(form.data['user'])
        print(selected_user.to_dict_no_jokes())

        new_joke = Joke(
            joke_body=form.data['joke'],
            punchline=form.data['punchline'],
            rating=form.data['rating'],
            user=selected_user
        )

        db.session.add(new_joke)
        db.session.commit()

        # UPDATING a RESOURCE
        # user_to_update = User.query.get(1)
        # user_to_update.username = 'Bradley'
        # db.session.commit()

        # DELETE a RESOURCE
        # user_to_delete = User.query.get(1)
        # db.session.delete(user_to_delete)
        # db.session.commit()


        # Making a new resource in our jokes file    
        # new_joke = {
        #     'jokeid': len(jokes) + 1,
        #     'joke': form.data['joke'],
        #     'punchline': form.data['punchline'],
        #     'rating': form.data['rating']
        # }
        # print(new_joke)
        # jokes.append(new_joke)
        return redirect("/jokes/all")
        
    if form.errors:
        return form.errors


    return render_template('joke_form.html', form=form)
