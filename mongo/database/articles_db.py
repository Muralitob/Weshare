# encoding: utf-8
"""
__author__:cjhcw
"""
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

articles_collection = 'articles'


def create_new_article(article, activeTab, tagLists, inputTag):
    """
    新建文章
    :param article:
    :param activeTab:
    :param tagLists:
    :param inputTag:
    :return:
    """
    title = article.get('title')
    content = article.get('content')
    uid = article.get('uid')
    result = mongo_manager.save_one(articles_collection,
                                    {'title': title, 'content': content, 'uid': int(uid), 'activeTab': activeTab,
                                     'tagLists': tagLists, 'inputTag': inputTag, 'create_time': datetime.utcnow(),
                                     'update_time': datetime.utcnow()})
    return result.acknowledged


def get_articles_by_uid(uid):
    """
    根据uid获取文章
    :param uid:
    :return:
    """
    result = list(mongo_manager.find(articles_collection, {'uid': int(uid)}))
    return result
