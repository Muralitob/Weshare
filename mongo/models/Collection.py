# encoding: utf-8
"""
__author__:cjhcw
"""
from bson import ObjectId
from core_manager.mongo_manager import mongo_manager


class Collection:
    collection = "collections"

    def __init__(self):
        pass

    @classmethod
    def query_collection_by_uid_and_aid(cls, uid, article_id):
        """
        uid是否收藏该article_id的文章
        :param uid:
        :param article_id:
        :return:
        """
        record = mongo_manager.find_one(cls.collection,
                                        {'uid': uid, 'article_id': ObjectId(article_id)})
        if record:
            return True
        return False

    @classmethod
    def find_count_collection(cls, article_id):
        """
        查找该文章的收藏
        :param article_id:
        :return:
        """
        return mongo_manager.find_count(cls.collection,
                                        {"article_id": ObjectId(article_id)})
