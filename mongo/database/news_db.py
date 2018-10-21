# encoding: utf-8
"""
__author__:cjhcw
"""
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId
from datetime import datetime

news_collection = 'news'


def create_new_news(data):
    """
    创建一条新闻
    :param data:
    :return:
    """
    data['create_time'] = datetime.now()
    data['update_time'] = datetime.now()
    result = mongo_manager.save_one(news_collection, data)
    return result.acknowledged


def get_all_news(page, limit):
    """
    获取所有新闻
    :return:
    """
    skip = (page - 1) * limit
    news_list = list(mongo_manager.find(news_collection, {}).skip(skip).limit(limit))
    length = mongo_manager.find_count(news_collection, {})
    return news_list, length


def delete_news_by_id(news_ids):
    """
    批量删除新闻
    :param news_ids:
    :return:
    """
    result = mongo_manager.remove_many(news_collection, {'_id': ObjectId(_id) for _id in news_ids})
    return result.acknowledged


def edit_one_new(new_id, data):
    """
    根据_id来编辑新闻
    :param new_id:
    :param data:
    :return:
    """
    data.pop('_id')
    data['update_time'] = datetime.now()
    result = mongo_manager.update_one(news_collection, {'_id': ObjectId(new_id)}, {"$set": data})
    return result.acknowledged
