from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


AUTHOR_CHOICES = ["Patch", "Blue", "Mimi"]
# ALT_AUTHOR_CHOICES = [(1, 'Patch'),(2, 'Blue'),(3, "Mimi")]

class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    image_url = StringField("Image_URL", validators=[DataRequired(), URL()])
    author = SelectField("Post Author", choices=AUTHOR_CHOICES)
    submit = SubmitField("Create Post")