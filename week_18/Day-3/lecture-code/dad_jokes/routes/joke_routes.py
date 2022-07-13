from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models.db import db, Joke, User


jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes')


@jokes_router.route('/all')
def all_jokes():
    jokes = Joke.query.order_by(Joke.rating).all()
    return render_template("all_jokes.html", jokes=jokes)


@jokes_router.route('/<int:id>')
def get_joke_by_id(id):
    print(id)
    one_joke = Joke.query.get(id)
    print(one_joke.to_dict())
    return render_template("all_jokes.html", jokes=[one_joke])



@jokes_router.route('/new', methods=["GET", "POST"])
def create_joke():
    form = NewJokeForm()

    form.user.choices = [ (user.id, user.username) for user in User.query.all()]
    print(form.user.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data['user'])
        print(selected_user.to_dict_no_joke())
        new_joke = Joke(
            joke_body=form.data['joke'],
            punchline=form.data['punchline'],
            rating=form.data['rating'],
            user= selected_user
        )
        db.session.add(new_joke)
        db.session.commit()
        return redirect('/jokes/all')

    if form.errors:
        return form.errors      

           # UPDATE A RECORD IN THE DB
            # joke1 = Joke.query.get(1)
            # user5 = User.query.get(5)
            # if user5 not in joke1.joke_likes:
            #     joke1.joke_likes.append(user5)
            #     db.session.commit()
            # else:
            #     print('User already likes this joke!')

    
            # DELETING A RECORD
            # joke1 = Joke.query.get(1)
            # db.sesssion.delete(joke1)
            # db.session.commit()          

    return render_template("joke_form.html", form=form)