# encoding: utf-8
"""
__author__:cjhcw
"""
from bson import ObjectId
from core_manager.mongo_manager import mongo_manager


class Like:
    like_collection = 'like_articles'
    like_comment_collection = 'like_comments'

    def __init__(self):
        pass

    @classmethod
    def query_like_article_by_uid_and_aid(cls, uid, article_id):
        """
        uid是否喜欢该article_id的文章
        :param uid:
        :param article_id:
        :return:
        """
        record = mongo_manager.find_one(cls.like_collection,
                                        {'uid': uid, 'article_id': ObjectId(article_id)})
        if record:
            return True
        return False

    @classmethod
    def query_like_comment_by_uid_and_comment(cls, uid, comment):
        """
        uid是否喜欢该comment的评论
        :param uid:
        :param comment:
        :return:
        """
        record = mongo_manager.find_one(cls.like_collection,
                                        {'uid': uid, 'article_id': comment})
        if record:
            return True
        return False

    @classmethod
    def find_count_like_article(cls, article_id):
        """
        查找该文章的喜欢数
        :param article_id:
        :return:
        """
        return mongo_manager.find_count(cls.like_collection,
                                        {"article_id": ObjectId(article_id)})
