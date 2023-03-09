from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from app.routes.aws_helpers import ALLOWED_EXTENSIONS


# AUTHOR_CHOICES = ["Patchenator", "Blueberry44", "brads213"]

class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5, message="Post captions must be at least 5 characters long")])
    # image_url = StringField("Post Image URL", validators=[DataRequired(), URL()])
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    author = SelectField("Post Author", choices=[])
    submit = SubmitField("Create Post")
