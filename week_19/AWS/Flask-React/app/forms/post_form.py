from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, URL
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS

# AUTHOR_CHOICES = ["Patch", "Blue", "Mimi", "Brad"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    # image = StringField('Image URL', validators=[DataRequired(), URL()])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Author", choices=[])
    submit = SubmitField("Create Post")
