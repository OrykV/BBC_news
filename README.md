BBC_news service

This application allows user to  download Ukrainian news from https://www.bbc.com/ukrainian/news . Unregistered users can only watch news, which are storing in database.
However users who are logged in are allowed to download and store news they want or to delete which they don`t want to store. Ability to clear all database is available too.

Application checks if user exist when you log in or sign up. If information you provide contains any errors you will be announced about them.

This service is created with Python3.7 and MongoDB. Flask, beautifulsoup4, requests, passlib, uwsgi were used too. 
Finally, this project was deployed to heroku. You can always try it https://bbcnews1.herokuapp.com . 
