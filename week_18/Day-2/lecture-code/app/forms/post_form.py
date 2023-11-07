from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL


AUTHOR_CHOICES = ["Patch", "Blue", "Mimi", "Brad"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    image_url = StringField('Image URL', validators=[DataRequired(), URL()])
    author = SelectField("Author", choices=AUTHOR_CHOICES)
    submit = SubmitField("Create Post")
