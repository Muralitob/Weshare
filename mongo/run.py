# encoding: utf-8
"""
__author__:cjhcw
"""
import sys
from flask import Flask
from flask_cors import CORS
from flask_restplus import Api
from os import path

from route.users import users
from route.articles import articles
from route.news import news
from route.goods import goods

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

app = Flask(__name__, static_url_path='', static_folder='../uploads')
api = Api(app)
CORS(app, supports_credentials=True)

app.register_blueprint(users)
app.register_blueprint(articles)
app.register_blueprint(news)
app.register_blueprint(goods)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3090, debug=True, threaded=True)
