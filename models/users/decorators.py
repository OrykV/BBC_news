from functools import wraps
from flask import session, flash, redirect, url_for, request


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """ Gives permit to use function only for users who are logged in"""
        if 'email' not in session.keys() or session['email'] is None:
            flash(u'You need to be signed in for this page.')
            return redirect(url_for('home', next=request.path))
        return f(*args, **kwargs)
    return decorated_function


