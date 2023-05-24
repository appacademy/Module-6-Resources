from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL


class PostForm(FlaskForm):
    caption = StringField("Caption", validators=[DataRequired(), Length(min=5)])
    image_url = StringField("Post Image URL", validators=[DataRequired(), URL()])
    author = SelectField("Post Author")
    submit = SubmitField("Create Post")
