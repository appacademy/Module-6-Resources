from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ..routes.AWS_helpers import ALLOWED_EXTENSIONS


class PostForm(FlaskForm):
  user_id = SelectField("Author", choices=[])
  caption = StringField("Caption", validators=[DataRequired(), Length(max=2000, min=5)])
  # image = StringField("Image", validators=[DataRequired(), URL()])
  image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
  submit = SubmitField("Submit")
  