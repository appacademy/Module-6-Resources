from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, URL
from ..routes.aws_helpers import ALLOWED_EXTENSIONS

# AUTHOR_CHOICES = ["Patch", "Blue", "Mimi"]
# AUTHOR_CHOICES = [(1, "Patch"), (2,"Blue"), (3,"Mimi")]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    # image = StringField("Image URL", validators=[DataRequired(), URL()])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Post Author", choices=[])
    submit = SubmitField("Create Post")
