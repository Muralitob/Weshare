# encoding: utf-8
"""
__author__:cjhcw
"""
import os
import jwt
from functools import wraps
from flask import request
from datetime import datetime
from bson import ObjectId

from core_manager.mongo_manager import mongo_manager
from models.User import User

from utility import page_limit_skip

users_collection = 'users'
collcetions_collection = 'collections'
articles_collection = 'articles'
like_collection = 'like_articles'
attention_collection = 'attentions'


def register(data):
    data['level'] = '0002'
    data['uid'] = list(mongo_manager.find_select_sort_limit('users', {}, {'uid': 1}, [('uid', -1)], 1))[0]['uid'] + 1
    data['major'] = ''
    data['nickname'] = data['account']
    data['birthday'] = ''
    data['sign'] = ''
    data['branch'] = ''
    data['sex'] = ''
    data['register_time'] = datetime.now()
    data['login_time'] = None
    user = User.query_one(data['account'])
    if user:
        return False
    else:
        return mongo_manager.save_one(users_collection, data).acknowledged


def login(data):
    user = User.query_one(data['account'])
    if user and user['pwd'] == data['pwd']:
        User.update_one(data['account'], {'login_time': datetime.now()})
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
        if token:
            payload = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            user = User.query_one_by_uid(int(payload['uid']))
            if user:
                return f(*args, **kwargs)
        else:
            cookie_uid = request.cookies.get('uid')
            cookie_user = User.query_one_by_uid(int(cookie_uid))
            if cookie_user:
                return f(*args, **kwargs)

    return decorated


def get_user_info(other_id, uid):
    one = User.query_one_by_uid({'uid': other_id})
    # if 'avatar_url' in one:
    #     basepath = os.path.dirname(__file__)  # 当前文件所在路径
    #     avatar_url = basepath + 'static/uploads_user_photos/' + one['avatar_url']
    #     one['avatar_url'] = avatar_url
    if uid:
        attention = mongo_manager.find_one(attention_collection, {'uid': uid, 'attention_uid': other_id})
        if attention:
            one['attentioned'] = True
        else:
            one['attentioned'] = False
    return one


def get_me_info(uid):
    one = User.query_one_by_uid(uid)
    attentions = list(mongo_manager.find(attention_collection, {'uid': uid}))
    if attentions:
        attention_uids = [att['attention_uid'] for att in attentions]
    else:
        attention_uids = []
    one['attention_uids'] = attention_uids
    return one


def edit_user_info(uid, data):
    if '_id' in data:
        data.pop('_id')
    return User.update_one(uid, data)


def get_collections_by_uid(uid, page, limit):
    skip = page_limit_skip(limit, page)
    result = list(
        mongo_manager.find(collcetions_collection, {'uid': uid}).skip(skip).limit(limit).sort([('create_time', -1)]))
    articles = []
    for item in result:
        article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(item['article_id'])})
        article['col_num'] = mongo_manager.find_count(collcetions_collection, {'article_id': article['_id']})
        article['like_num'] = mongo_manager.find_count(like_collection, {'article_id': article['_id']})
        articles.append(article)
    length = mongo_manager.find_count(collcetions_collection, {'uid': uid})
    return articles, length


def save_collection(uid, article_id):
    query = {'uid': uid, 'article_id': ObjectId(article_id)}
    collcetion = mongo_manager.find_one(collcetions_collection, query)
    if collcetion:
        return False
    return mongo_manager.save_one(collcetions_collection,
                                  {'uid': uid, 'article_id': ObjectId(article_id), 'create_time': datetime.now(),
                                   'update_time': datetime.now()}).acknowledged


def delete_collections(uid, article_ids):
    for article_id in article_ids:
        article = mongo_manager.find_one(collcetions_collection, {'uid': uid, 'article_id': ObjectId(article_id)})
        if article:
            mongo_manager.remove_one(collcetions_collection, {'uid': uid, 'article_id': ObjectId(article_id)})
        else:
            return False
    return True


def add_attention(uid, attention_uid):
    is_attentions = mongo_manager.find_one(attention_collection, {'uid': uid, 'attention_uid': attention_uid})
    if is_attentions:
        return False
    else:
        return mongo_manager.save_one(attention_collection, {'uid': uid, 'attention_uid': attention_uid}).acknowledged


def delete_attention(uid, attention_uid):
    is_attentions = mongo_manager.find_one(attention_collection, {'uid': uid, 'attention_uid': attention_uid})
    if not is_attentions:
        return False
    else:
        return mongo_manager.remove_one(attention_collection, {'uid': uid, 'attention_uid': attention_uid}).acknowledged


def get_attentions(uid, page, limit):
    skip = page_limit_skip(limit, page)
    attentions = list(mongo_manager.find(attention_collection, {'uid': uid}).skip(skip).limit(limit))
    users = []
    for attention in attentions:
        user = User.query_one(attention['attention_uid'])
        if user:
            users.append(user)
    count = mongo_manager.find_count(attention_collection, {'uid': uid})
    return users, count
