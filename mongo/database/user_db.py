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
             'update_time': str(datetime.utcnow()), "exp": int(datetime.utcnow().second + 86400)}, 'secret',
            algorithm='HS256')
        return_object = {'status': 'login success', 'code': 200, 'token': encoded,
                         'account': user['account'], 'org': str(user['level']), 'uid': str(user['uid'])}
        return return_object
    else:
        return False


def check_token(token):
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    if payload:
        return True, token
    return False, token


def get_user_info(uid):
    query = {'uid': uid}
    one = list(mongo_manager.find_one('users', query))
    return one
