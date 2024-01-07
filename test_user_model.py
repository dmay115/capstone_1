import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User
from app import app

os.environ["DATABASE_URL"] = "postgresql:///bartender_test"

with app.app_context():
    db.create_all()


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        with app.app_context():
            db.drop_all()
            db.create_all()

            u1 = User.signup("test1", "email1@email.com", "password")
            uid1 = 1111
            u1.id = uid1

            u2 = User.signup("test2", "email2@email.com", "password")
            uid2 = 2222
            u2.id = uid2

            db.session.commit()

            self.u1 = User.query.get(uid1)
            self.uid1 = uid1

            self.u2 = User.query.get(uid2)
            self.uid2 = uid2

            self.client = app.test_client()

    def test_signup(self):
        with app.app_context():
            user = User.signup("testuser", "test@example.com", "password")

            self.assertIsInstance(user, User)
            self.assertEqual(user.username, "testuser")
            self.assertEqual(user.email, "test@example.com")
            self.assertTrue(user.password.startswith("$2b$"))

    def test_authenticate_success(self):
        with app.app_context():
            User.signup("testuser", "test@example.com", "password")
            db.session.commit()

            authenticated_user = User.authenticate("testuser", "password")

            self.assertIsInstance(authenticated_user, User)
            self.assertEqual(authenticated_user.username, "testuser")

    def test_authenticate_failure_wrong_password(self):
        with app.app_context():
            User.signup("testuser", "test@example.com", "password")
            db.session.commit()

            authenticated_user = User.authenticate("testuser", "wrong_password")

            self.assertFalse(authenticated_user)

    def test_authenticate_failure_wrong_username(self):
        with app.app_context():
            User.signup("testuser", "test@example.com", "password")
            db.session.commit()

            authenticated_user = User.authenticate("wrong_user", "password")

            self.assertFalse(authenticated_user)

    def tearDown(self):
        with app.app_context():
            res = super().tearDown()
            db.session.rollback()
            return res

    def test_user_model(self):
        """Does basic model work?"""
        with app.app_context():
            u = User(
                email="test@test.com", username="testuser", password="HASHED_PASSWORD"
            )
            db.session.add(u)
            db.session.commit()
