# encoding: utf-8
"""
__author__:cjhcw
"""
import jwt
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
    if user and user['pwd'] == data['pwd']:
        mongo_manager.update_one(users_collection, {'account': data['account']},
                                 {"$set": {'login_time': datetime.utcnow()}})
        encoded = jwt.encode(
            {'account': user.account, '_id': str(user._id), 'organization': str(user.level),
             'update_time': str(datetime.utcnow())}, 'secret', algorithm='HS256')
        return_object = {'message': 'success', 'token': encoded,
                         'account': user.account, 'org': str(user.level), '_id': str(user._id)}
        return return_object
    else:
        return False
