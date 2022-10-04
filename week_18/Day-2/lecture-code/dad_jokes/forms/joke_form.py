from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


RATING_CHOICES = ["G", "PG", "R"]


# def user_exists(form, field):
#     # Checking if user exists
#     email = field.data
#     user = User.query.filter(User.email == email).first()
#     if user:
#         raise ValidationError('Email address is already in use.')



class NewJokeForm(FlaskForm):
    joke = StringField("Joke", validators=[DataRequired()])
    # email = StringField("email", validators=[DataRequired(), user_exists])
    punchline = StringField("Punchline", validators=[DataRequired()])
    rating = SelectField("Rating", choices=RATING_CHOICES)
    submit = SubmitField("Add Joke")