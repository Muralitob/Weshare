# encoding: utf-8
"""
__author__:cjhcw
"""
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId

articles_collection = 'articles'


def create_new_article(data):
    """
    新建文章
    :param data:
    :return:
    """
    data['create_time'] = datetime.utcnow()
    data['update_time'] = datetime.utcnow()
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
    result = list(
        mongo_manager.find(articles_collection, {'article.uid': uid, 'category': category}).skip(skip).limit(limit))
    return result, len(result)


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


def delete_article_by_id(ids):
    """
    批量删除文章
    :param ids:
    :return:
    """
    for _id in ids:
        result = mongo_manager.remove_one(articles_collection, {'_id': ObjectId(_id)})
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
    length = len(list(mongo_manager.find(articles_collection, query)))
    return result, length
