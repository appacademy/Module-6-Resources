from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length
from ..routes.aws_helpers import ALLOWED_EXTENSIONS

# AUTHOR_CHOICES = ['Patch', 'Blue', "Mimi"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    # image = StringField("Image", validators=[DataRequired(), URL()])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Author", choices=[])
    submit = SubmitField("Create Post")