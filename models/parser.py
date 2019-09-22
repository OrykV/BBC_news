from models.item import Item
from common.database import Database


class Parser:
    @staticmethod
    def save_news():
        news = Item.parse_news()
        for element in news:
            header = element.find('a').text.strip()
            summary = element.find('p').text
            url = element.find('a').attrs['href']
            data = Parser.retrieve_news(header)
            if data is None:
                new = Item(header, summary, url)
                new.save_to_mongo()

    @staticmethod
    def retrieve_news(header):
        data = Database.find_one('news', {'header': header})
        return data








