import uuid
from flask import flash, redirect, url_for
from common.database import Database
from common.utils import Utils
import models.users.errors as UserErrors


class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def __repr__(self):
        return "<User {}>".format(self.email)

    @staticmethod
    def is_login_valid(email, password):
        """
        This method verifies that an e-mail/password combo (as sent by the site forms) is valid or not.
        Checks that the e-mail exists, and that the password associated to that e-mail is correct.
        """
        user_data = Database.find_one("users", {"email": email})  # Password in sha512 -> pbkdf2_sha512
        if user_data is None:
            flash(f'User {email} does not exist. Try again or')
            redirect(url_for('login'))
            return False
        if not Utils.check_hashed_password(password, user_data['password']):
            flash('Your password was wrong. Try again!')
            redirect(url_for('login'))
            return False
        return True

    @staticmethod
    def register_user(email, password):
        """
        This method registers a user using e-mail and password.
        The password already comes hashed as sha-512.
        """
        user_data = Database.find_one("users", {"email": email})
        if user_data is not None:
            flash(f'The e-mail {email} you used to register already exists. Try again or')
            redirect(url_for('login'))
            return False
        if not Utils.email_is_valid(email):
            flash('The e-mail does not have the right format. Try again!')
            redirect(url_for('signup'))
            return False
        User(email, Utils.hash_password(password)).save_to_db()
        return True

    def save_to_db(self):
        Database.insert("users", self.json())

    def json(self):
        return {
            "_id": self._id,
            "email": self.email,
            "password": self.password
        }
