from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, URL, Email



class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    submit = SubmitField("Login")   


class LogoutForm(FlaskForm):
     submit = SubmitField("Logout")   


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=5)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()]) 
    profile_pic = StringField("Profile Pic URL", validators=[DataRequired(), URL()])
    bio = StringField("Bio")
    submit = SubmitField("Sign Up")  