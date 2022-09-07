from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


RATING_CHOICES = ["G", "PG", "R"]


class NewJokeForm(FlaskForm):
    joke = StringField("Joke", validators=[DataRequired()])
    punchline = StringField("Punchline", validators=[DataRequired()])
    rating = SelectField("Rating", choices=RATING_CHOICES )
    submit = SubmitField("Add Joke")