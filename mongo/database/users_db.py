# encoding: utf-8
"""
__author__:cjhcw
"""
import jwt
from functools import wraps
from flask import request
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId

users_collection = 'users'
articles_collection = 'articles'


def register(data):
    data['register_time'] = datetime.utcnow()
    data['login_time'] = datetime.utcnow()
    data['level'] = '0002'
    if 'collections' not in data:
        return False
    data['collections'] = []
    if 'nickname' not in data:
        return False
    data['nickname'] = ''
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
    return mongo_manager.find_one(users_collection, query)


def edit_user_info(uid, data):
    result = mongo_manager.update_one(users_collection, {'uid': uid}, {"$set": data})
    return result.acknowledged


def get_collections_by_uid(uid):
    user = mongo_manager.find_one(users_collection, {'uid': uid})
    if 'collections' in user:
        collections = user['collections']
        articles = []
        for article in collections:
            collection_article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(article)})
            articles.append(collection_article)
        return articles
    else:
        return []


def save_collection(uid, article_id):
    user = mongo_manager.find_one(users_collection, {'uid': uid})
    if 'collections' not in user or user['collections']:
        collections = [article_id]
    else:
        collections = user['collections'].append(article_id)
    result = mongo_manager.update_one(users_collection, {'uid': uid}, {"$set": {'collections': collections}})
    return result.acknowledged


def delete_collections(uid, article_ids):
    user = mongo_manager.find_one(users_collection, {'uid': uid})
    for article_id in article_ids:
        if article_id in user['collections']:
            user['collections'].pop(article_id)
    result = mongo_manager.update_one(users_collection, {'uid': uid}, {"$set": {'collections': user['collections']}})
    return result.acknowledged
