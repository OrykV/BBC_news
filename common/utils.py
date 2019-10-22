from passlib.hash import pbkdf2_sha512
import re


class Utils(object):

    @staticmethod
    def email_is_valid(email):
        """ Checkes if email address is valid"""
        email_address_matcher = re.compile('^[\w-]+@([\w-]+\.)+[\w]+$')
        return True if email_address_matcher.match(email) else False

    @staticmethod
    def hash_password(password):
        """ Hashes a password using pbkdf2_sha512"""
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """Checks that the password the user sent matches that of the database."""
        return pbkdf2_sha512.verify(password, hashed_password)
