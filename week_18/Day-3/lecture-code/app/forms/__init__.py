from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
  author = SelectField("Author", choices=["Pip", "Loki", "Luna"])
  caption = StringField("Caption", validators=[DataRequired()])
  image = StringField("Image", [DataRequired()])
  submit = SubmitField("Submit")