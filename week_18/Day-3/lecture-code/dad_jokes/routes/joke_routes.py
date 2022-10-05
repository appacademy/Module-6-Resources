from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User

joke_router = Blueprint('jokes', __name__, url_prefix="/jokes")


# print("inside the jokes blueprint file", __name__)


@joke_router.route('/all')  #  URL is now /jokes/all
def all_jokes():
    jokes = Joke.query.order_by(Joke.rating).all()
    return render_template("all_jokes.html", jokes=jokes)



@joke_router.route('/<int:id>')
def get_joke_by_id(id):
    # print(id)
    joke = Joke.query.get(id)
    # print(one_joke)
    return render_template("all_jokes.html", jokes=[joke])



@joke_router.route('/new', methods=["GET", "POST"])
def create_new_joke():
    form = NewJokeForm()

    form.user.choices = [ (user.id, user.username) for user in User.query.all() ]
    print(form.user.choices)

    if form.validate_on_submit():
        # print(form.data['user'])
        selected_user = User.query.get(form.data['user'])
        print(selected_user)
        new_joke = Joke(
            joke_body = form.data['joke'],
            punchline = form.data['punchline'],
            rating = form.data['rating'],
            user=selected_user
        )
        
        db.session.add(new_joke)
        db.session.commit()
        return redirect('/jokes/all')

    if form.errors:
        return form.errors


    return render_template("joke_form.html", form=form)