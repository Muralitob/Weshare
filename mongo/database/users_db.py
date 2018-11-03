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
collcetions_collection = 'collections'
articles_collection = 'articles'


def register(data):
    data['register_time'] = datetime.now()
    data['login_time'] = datetime.now()
    data['level'] = '0002'
    if 'nickname' not in data:
        data['nickname'] = ''
    data['birthday'] = ''
    data['sign'] = ''
    data['sex'] = ''
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
                                 {"$set": {'login_time': datetime.now()}})
        encoded = jwt.encode(
            {'account': user['account'], 'uid': str(user['uid']), 'organization': str(user['level']),
             'update_time': str(datetime.now())}, 'secret', algorithm='HS256')
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
    if '_id' in data:
        data.pop('_id')
    result = mongo_manager.update_one(users_collection, {'uid': uid}, {"$set": data})
    return result.acknowledged


def get_collections_by_uid(uid, page, limit):
    skip = (page - 1) * limit
    result = list(
        mongo_manager.find(collcetions_collection, {'uid': uid}).skip(skip).limit(limit).sort([("create_time", -1)]))
    articles = []
    for item in result:
        article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(item['article_id'])})
        articles.append(article)
    length = mongo_manager.find_count(collcetions_collection, {'uid': uid})
    return articles, length


def save_collection(uid, article_id):
    query = {'uid': uid, 'article_id': ObjectId(article_id)}
    collcetion = mongo_manager.find_one(collcetions_collection, query)
    if collcetion:
        return False
    result = mongo_manager.save_one(collcetions_collection,
                                    {'uid': uid, 'article_id': ObjectId(article_id), 'create_time': datetime.now(),
                                     'update_time': datetime.now()})
    return result.acknowledged


def delete_collections(uid, article_ids):
    for article_id in article_ids:
        article = mongo_manager.find_one(collcetions_collection, {'uid': uid, 'article_id': ObjectId(article_id)})
        if article:
            result = mongo_manager.remove_one(collcetions_collection, {'uid': uid, 'article_id': ObjectId(article_id)})
        else:
            return False
    return True
