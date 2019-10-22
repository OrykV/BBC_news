""" This file wa created to store errors which should be raised"""


class UserError(Exception):
    def __init__(self, message):
        self.message = message


class UserNotExistsError(UserError):
    pass


class IncorrectPasswordError(UserError):
    pass


class UserAlreadyRegisteredError(UserError):
    pass


class InvalidEmailError(UserError):
    pass