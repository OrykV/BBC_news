from flask import Flask, render_template, flash, request, redirect, session, url_for
from models.item import Item
from models.parser import Parser
from common.database import Database
from models.users.user import User
import models.users.errors as UserErrors
import models.users.decorators as user_decorators


app = Flask(__name__)
app.secret_key = 'dont tell anyone'
Database.initialize()


@app.route('/')
@user_decorators.requires_login
def new():
    news = Item.all()
    return render_template('new.html', news=news)


@app.route('/download_new')
@user_decorators.requires_login
def download():
    new_items = Parser.save_news()
    quantity = len(new_items)
    flash(f'{quantity} items was added!')
    return render_template('base.html', news=new_items, quantity=quantity)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.is_login_valid(email, password):
                session['email'] = email
                return redirect(url_for("new"))
        except UserErrors.IncorrectPasswordError as e:
            return e.message
    return render_template('user/login.html')


@app.route('/home')
def home():
    if 'email' not in session.keys() or session['email'] is None:
        return render_template('home.html')
    return redirect(url_for('new'))


@app.route('/signup',  methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for("new"))
        except UserErrors.UserError as e:
            return e.message
    return render_template('user/signup.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run()

# Parser.save_news()
# pars = Item.all()
# pars = Item.find_needed()

