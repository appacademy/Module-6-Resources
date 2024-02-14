from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from flask_wtf.file import FileField, FileRequired, FileAllowed
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS


# AUTHOR_CHOICES = ["Patch", "Blue", "Mimi", "Other"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    # image = StringField("Post Image URL", validators=[DataRequired(), URL()])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Post Auther", choices=[])
    submit = SubmitField("Create Post")
