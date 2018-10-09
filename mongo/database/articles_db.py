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


def get_articles_by_uid(uid, category):
    """
    根据uid获取文章
    :param uid:
    :param category:
    :return:
    """
    result = list(mongo_manager.find(articles_collection, {'uid': int(uid), 'category': category}))
    return result


def edit_article_by_id(article):
    """
    根据id编辑文章
    :param id:
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
    for id in ids:
        result = mongo_manager.remove_one(articles_collection, {'_id': ObjectId(id)})
    return result.acknowledged
