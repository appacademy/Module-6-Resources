from flask import Blueprint, render_template, redirect
# from ..db_jokes import jokes
from ..forms.joke_form import NewJokeForm
from ..models import db, Joke, User


jokes_router = Blueprint('jokes', __name__, url_prefix='/jokes' )



@jokes_router.route('/all')
def get_all_jokes():
    jokes = Joke.query.order_by(Joke.rating).all()
    return render_template("all_jokes.html", jokes=jokes)



@jokes_router.route('/<int:id>')
def get_joke_by_id(id):
    print(id)
    joke = Joke.query.get(id)
    # one_joke = jokes[id - 1] if id <= len(jokes) else "No Joke with that ID"
    return render_template("all_jokes.html", jokes=[joke])



@jokes_router.route("/new", methods=["GET", "POST"])
def add_joke():
    form = NewJokeForm()
    
    form.user.choices = [ (user.id, user.username) for user in User.query.all()]
    print(form.user.choices)

    if form.validate_on_submit():
        selected_user = User.query.get(form.data['user'])
        print(selected_user)
        new_joke = Joke(
            joke_body=form.data["joke"],
            punchline=form.data['punchline'],
            rating=form.data['rating'],
            user=selected_user
        )
        db.session.add(new_joke)
        db.session.commit()
        return redirect("/jokes/all")

    if form.errors:
        return form.errors

    return render_template("joke_form.html", form=form)