from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


AUTHOR_CHOICES = ['Patch', 'Blue', "Mimi"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    image_url = StringField("Image", validators=[DataRequired(), URL()])
    author = SelectField("Author", choices=AUTHOR_CHOICES)
    submit = SubmitField("Create Post")