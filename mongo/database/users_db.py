# encoding: utf-8
"""
__author__:cjhcw
"""
import jwt
from functools import wraps
from flask import request
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

users_collection = 'users'


def register(data):
    data['register_time'] = datetime.utcnow()
    data['login_time'] = datetime.utcnow()
    data['level'] = '0002'
    data['uid'] = max(list(mongo_manager.find_projection(users_collection, {}, {'uid': 1, '_id': 0})))['uid'] + 1
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
            {'account': user['account'], 'uid': str(user['uid']), 'organization': str(user['level']),
             'update_time': str(datetime.utcnow())}, 'secret', algorithm='HS256')
        return_object = {'status': 'login success', 'code': 200, 'token': encoded,
                         'account': user['account'], 'org': str(user['level']), 'uid': str(user['uid'])}
        return return_object
    else:
        return False


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        payload = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        if payload:
            right = mongo_manager.find_one(users_collection, {'uid': payload['uid']})
            if not right:
                return f(*args, **kwargs)
    return decorated


def get_user_info(uid):
    query = {'uid': int(uid)}
    one = mongo_manager.find_one(users_collection, query)
    return one


def edit_user_info(uid, data):
    result = mongo_manager.update_one(users_collection, {'uid': uid}, {"$set": data})
    return result.acknowledged
