import uuid
import requests
import datetime
from bs4 import BeautifulSoup
from common.database import Database


class Item(object):
    def __init__(self, header, summary, url, _id=None, saved_date=None):
        self.header = header
        self.summary = summary
        self.url = url
        self._id = uuid.uuid4().hex if _id is None else _id
        self.saved_date = datetime.datetime.today().strftime('%d %b %Y') if saved_date is None else saved_date

    def __repr__(self):
        return f"{self.header} || {self.summary} || {self.url} || {self.saved_date} \n"

    def json(self):
        return {
            "_id": self._id,
            "header": self.header,
            "summary": self.summary,
            "url": f'https://www.bbc.com{self.url}',
            "saved_date": self.saved_date
        }

    def save_to_mongo(self):
        Database.insert('news', self.json())

    @staticmethod
    def parse_news():
        """ This method parse content from url"""
        URL = "https://www.bbc.com/ukrainian/news"
        TAG_NAME = "div"
        QUERY = {"class": "eagle-item"}
        response = requests.get(URL)
        content = response.content
        soup = BeautifulSoup(content, "html.parser")
        elements = soup.findAll(TAG_NAME, QUERY)
        return elements

    @staticmethod
    def delete_all():
        Database.remove('news', {})

    @staticmethod
    def remove_item(item_id):
        Database.remove('news', {'_id': item_id})

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find('news', {})]







