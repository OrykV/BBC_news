from models.item import Item
from common.database import Database


class Parser:
    @staticmethod
    def save_news():
        news = Item.parse_news()
        array = []
        for element in news:
            header = element.find('a').text.strip()
            summary = element.find('p').text
            url = element.find('a').attrs['href']
            data = Parser.retrieve_news(header)
            if data is None:
                new = Item(header, summary, url)
                new.save_to_mongo()
                new_to_array = Item(header, summary, f'https://www.bbc.com{url}')
                array.append(new_to_array)
        return array

    @staticmethod
    def retrieve_news(header):
        data = Database.find_one('news', {'header': header})
        return data








