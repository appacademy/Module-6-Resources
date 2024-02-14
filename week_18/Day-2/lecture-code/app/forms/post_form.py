from wtforms import StringField, SelectField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, URL, Length
from app.posts import users


choices = [ user["name"] for user in users]


class NewPost(FlaskForm):
    author = SelectField("Author", choices=choices, validators=[InputRequired()])
    image = StringField("Image URL", [InputRequired(), URL()])
    caption = StringField("Caption", validators=[InputRequired(), Length(min=3, max=200)])
    submit = SubmitField("Submit")


