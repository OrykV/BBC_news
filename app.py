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
def new():
    if 'email' not in session.keys() or session['email'] is None:
        return render_template('home.html')
    return redirect(url_for('list_news'))



@app.route('/download_new')
@user_decorators.requires_login
def download():
    new_items = Parser.save_news()
    quantity = len(new_items)
    flash(f'{quantity} items was added!')
    return render_template('new.html', news=new_items, quantity=quantity)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if User.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for('new'))
    return render_template('user/login.html')


@app.route('/list')
def list_news():
    news = Item.all()
    return render_template('base.html', news=news)


@app.route('/signup',  methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            if User.register_user(email, password):
                session['email'] = email
                return redirect(url_for('new'))
        except UserErrors.UserError as e:
            return e.message
    return render_template('user/signup.html')


@app.route('/tools', methods=["GET", "POST"])
@user_decorators.requires_login
def tools():
    if request.method == 'POST':
        item_id = request.form['item_id']
        Item.remove_item(item_id)
        flash(f'Item with item id {item_id} was deleted!')
        news = Item.all()
        return render_template('tools.html', news=news)
    news = Item.all()
    return render_template('tools.html', news=news)


@app.route('/permanently_delete', methods=["GET", "POST"])
@user_decorators.requires_login
def permanently_delete():
    Item.delete_all()
    return redirect(url_for('new'))


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

