from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL


# AUTHOR_CHOICES = ["Patch", "Blue", "Brad"]


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5, message="Post captions must be at least 5 chars!")])
    image = StringField("Post Image URL", validators=[DataRequired(), URL()]) 
    # author = SelectField("Post Author", choices=[])   
    submit = SubmitField("Save Post")
