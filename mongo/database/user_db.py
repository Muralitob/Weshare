# encoding: utf-8
"""
__author__:cjhcw
"""

from datetime import datetime
from core_manager.mongo_manager import mongo_manager

users_collection = 'users'


def register(data):
    data['register_time'] = datetime.utcnow()
    data['login_time'] = datetime.utcnow()
    user = mongo_manager.find_one(users_collection, {'account': data['account']})
    if user:
        return False
    else:
        return mongo_manager.save_one(users_collection, data)


def login(data):
    user = mongo_manager.find_one(users_collection, {'account': data['account']})
    if user and user['password'] == data['password']:
        mongo_manager.update_one(users_collection, {'account': data['account']},
                                 {"$set": {'login_time': datetime.utcnow()}})
        return True
    else:
        return False
