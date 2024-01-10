from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, URL, Length


AUTHOR_CHOICES = [(1,"Pip"), (2,"Luna"), (3,"Loki")]

class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[InputRequired(), Length(min=5, max=500)])
    image = StringField("Post Image URL", validators=[InputRequired(), URL()])
    author = SelectField("Author", choices=AUTHOR_CHOICES)
    submit = SubmitField("Create Post")

