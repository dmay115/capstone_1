"""SQLAlchemy models for Bartender."""

from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """User for bartender app"""

    __tablename__ = "users"

    userID = db.Column(
        db.Integer,
        primary_key=True,
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )

    @classmethod
    def signup(cls, username, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode("UTF-8")

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Drink(db.Model):
    """Drink in bartender app"""

    __tablename__ = "drinks"

    drinkID = db.Column(
        db.Integer,
        primary_key=True,
    )

    name = db.Column(
        db.Text,
    )

    total_rating = db.Column(
        db.Integer,
    )


class User_Rating(db.Model):
    """Info on drinks user has made"""

    __tablename__ = "userDrinks"

    user_drink_ID = db.Column(
        db.Integer,
        primary_key=True,
    )

    userID = db.Column(
        db.Integer,
        db.ForeignKey("users.userID", ondelete="cascade"),
    )

    drinkID = db.Column(
        db.Integer,
    )

    name = db.Column(
        db.Text,
    )

    user_rating = db.Column(
        db.Integer,
    )

    first_made = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    user_comments = db.Column(db.Text)


class Ingredients(db.Model):
    __tablename__ = "ingredients"

    ingID = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.Text,
    )


class Ingredients_On_Hand(db.Model):
    __tablename__ = "onHand"

    on_hand_ID = db.Column(
        db.Integer,
        primary_key=True,
    )

    userID = db.Column(
        db.Integer,
        db.ForeignKey("users.userID", ondelete="cascade"),
    )

    ingredient = db.Column(
        db.Text,
    )


def connect_db(app):
    db.app = app
    db.init_app(app)
