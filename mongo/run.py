# encoding: utf-8
"""
__author__:cjhcw
"""
import sys
from datetime import datetime
from flask import Flask
from flask import request
from flask import make_response
from flask_cors import CORS
from flask import g
from flask import got_request_exception
from flask_restplus import Api
from os import path

from route.user import user
from route.article import article

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

program = Flask(__name__, static_url_path='', static_folder='../uploads')
api = Api(program)
CORS(program, supports_credentials=True)

program.register_blueprint(user)
program.register_blueprint(article)

if __name__ == '__main__':
    program.run(host='0.0.0.0', port=3090, debug=True, threaded=True)
