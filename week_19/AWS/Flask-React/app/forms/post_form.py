from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS


# AUTHOR_CHOICES = ["Patch", "Blue", "Brad"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5, message="Post captions must be at least 5 chars!")])
    # image = StringField("Post Image URL", validators=[DataRequired(), URL()]) 
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Post Author", choices=[])   
    submit = SubmitField("Save Post")
