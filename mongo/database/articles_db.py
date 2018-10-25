# encoding: utf-8
"""
__author__:cjhcw
"""
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId

articles_collection = 'articles'
comments_collection = 'comments'
users_collection = 'users'


def create_new_article(data):
    """
    新建文章
    :param data:
    :return:
    """
    data['create_time'] = datetime.now()
    data['update_time'] = datetime.now()
    data['like_num'] = 0
    data['read_num'] = 0
    result = mongo_manager.save_one(articles_collection, data)
    return result.acknowledged


def get_articles_by_uid(uid, category, page, limit):
    """
    根据uid获取文章
    :param uid:
    :param category:
    :param page:
    :param limit:
    :return:
    """
    skip = (page - 1) * limit
    query = {'article.uid': uid, 'category': category}
    result = list(mongo_manager.find(articles_collection, query).skip(skip).limit(limit))
    length = mongo_manager.find_count(articles_collection, query)
    return result, length


def get_articles_by_id(_id):
    """
    根据_id获取文章
    :param _id:
    :return:
    """
    return mongo_manager.find_one(articles_collection, {'_id': ObjectId(_id)})


def edit_article_by_id(article):
    """
    根据id编辑文章
    :param article:
    :return:
    """
    _id = article.get('_id')
    if _id:
        result = mongo_manager.update_one(articles_collection, {'_id': _id}, {'$set': article})
        return result.acknowledged
    else:
        return False


def delete_article_by_id(article_ids):
    """
    批量删除文章
    :param article_ids:
    :return:
    """
    result = mongo_manager.remove_many(articles_collection, {'_id': ObjectId(_id) for _id in article_ids})
    return result.acknowledged


def like_article(article_id, add):
    """
    文章点赞
    :param article_id:
    :param add +1 点赞 -1 取消点赞
    :return:
    """
    query = {'_id': ObjectId(article_id)}
    article = mongo_manager.find_one(articles_collection, query)
    if add == -1 and article['like_num'] == 0:
        return False
    comment = {"$set": {'like_num': article['like_num'] + add}}
    result = mongo_manager.update_one(articles_collection, query, comment)
    return result.acknowledged


def read_article(article_id):
    """
    文章阅读数
    :param article_id:
    :return:
    """
    query = {'_id': ObjectId(article_id)}
    article = mongo_manager.find_one(articles_collection, query)
    comment = {"$set": {'read_num': article['read_num'] + 1}}
    result = mongo_manager.update_one(articles_collection, query, comment)
    return result.acknowledged


def get_real_articles(page, limit):
    """
    获取category:real文章
    :return:
    """
    query = {"category": "real"}
    limit = int(limit)
    skip = (int(page) - 1) * limit
    result = list(mongo_manager.find(articles_collection, query).skip(skip).limit(limit))
    length = mongo_manager.find_count(articles_collection, query)
    return result, length


def add_comment(parent_id, uid, content):
    """
    新增评论
    :param parent_id:
    :param uid:
    :param content:
    :return:
    """
    article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(parent_id)})
    if article:
        is_first_comment = True
    else:
        is_first_comment = False
    user = mongo_manager.find_one(users_collection, {'uid': uid})
    comment = {'parent_id': ObjectId(parent_id), 'name': user['nickname'], 'content': content,
               'comment_time': datetime.now(),
               'is_first_comment': is_first_comment, 'like_num': 0}
    result = mongo_manager.save_one(comments_collection, comment)
    return result.acknowledged


def get_comments(article_id, page, limit):
    """
    获取评论
    :param article_id:
    :param page:
    :param limit:
    :return:
    """
    skip = (page - 1) * limit
    result = list(mongo_manager.find(comments_collection, {'parent_id': ObjectId(article_id)}).skip(skip).limit(limit))
    for item in result:
        comments = list(mongo_manager.find(comments_collection, {'parent_id': item['_id']}))
        item['comments'] = comments
    length = mongo_manager.find_count(comments_collection, {'parent_id': ObjectId(article_id)})
    return result, length


def delete_comment(_id):
    """
    删除单条评论
    :param _id:
    :return:
    """
    return mongo_manager.remove_one(comments_collection, {'_id': ObjectId(_id)}).acknowledged


def edit_comment(_id, content):
    """
    编辑单条评论
    :param _id:
    :param content:
    :return:
    """
    query = {'_id': ObjectId(_id)}
    old_comment = mongo_manager.find_one(comments_collection, query)
    comment = {"$set": {'content': content, 'comment_time': datetime.now(), 'like_num': old_comment['like_num']}}
    result = mongo_manager.update_one(comments_collection, query, comment)
    return result.acknowledged


def like_comment(_id, add):
    """
    点赞
    :param _id:
    :param add +1 点赞 -1 取消点赞
    :return:
    """
    query = {'_id': ObjectId(_id)}
    old_comment = mongo_manager.find_one(comments_collection, query)
    if add == -1 and old_comment['like_num'] == 0:
        return False
    comment = {"$set": {'like_num': old_comment['like_num'] + add}}
    result = mongo_manager.update_one(comments_collection, query, comment)
    return result.acknowledged
