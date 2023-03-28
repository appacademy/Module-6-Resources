from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL 


AUTHOR_CHOICES = ["Patchenator", "Blueberry44", "brads213"]

# DIFFERNT_CHOICES = [(1, "Patchenator"), (2, "Blueberry44"), (3, "brads213")]

class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5, message="Post captions must be at least 5 characters")])
    image_url = StringField("Post Image URL", validators=[DataRequired(), URL()])
    author = SelectField("Post Image", choices=AUTHOR_CHOICES)
    submit = SubmitField("Create Post")