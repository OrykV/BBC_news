from flask import Flask, render_template
from models.item import Item
from models.parser import Parser
from common.database import Database

app = Flask(__name__)
Database.initialize()


@app.route('/')
def home():
    return render_template('new.html', headers=Item.load_news()[0], summary=Item.load_news()[1], urls=Item.load_news()[2])


# if __name__ == '__main__':
#     app.run()

# Parser.save_news()
pars = Item.all()
print(pars)