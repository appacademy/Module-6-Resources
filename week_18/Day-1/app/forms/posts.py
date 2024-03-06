from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL, Length
from app.posts import users

select_choices = [user["name"] for user in users]

class NewPost(FlaskForm):
  # author = StringField(label="Author", validators=[DataRequired(), Length(min=3, max=200)])
  author = SelectField("Author", choices=select_choices, validators=[DataRequired()])
  image = StringField("Image", [DataRequired(), URL()])
  caption = StringField("Caption", validators=[DataRequired(), Length(min=3, max=200)])
  submit = SubmitField("Submit")
  