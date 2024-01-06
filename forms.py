from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField("Username", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class RatingForm(FlaskForm):
    """Cocktail Rating Form"""

    rating = RadioField(
        "Rating",
        choices=[
            ("5", "5 stars"),
            ("4", "4 stars"),
            ("3", "3 stars"),
            ("2", "2 stars"),
            ("1", "1 star"),
        ],
        validators=[DataRequired()],
    )
    comments = TextAreaField("Comments")
