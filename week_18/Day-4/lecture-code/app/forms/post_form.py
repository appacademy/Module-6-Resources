from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, URL, Length



class PostForm(FlaskForm):
  user_id = SelectField("Author", choices=[])
  caption = StringField("Caption", validators=[DataRequired(), Length(max=2000, min=5)])
  image = StringField("Image", validators=[DataRequired(), URL()])
  submit = SubmitField("Submit")
  