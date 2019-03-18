# encoding: utf-8
"""
__author__:cjhcw
"""
from bson import ObjectId
from core_manager.mongo_manager import mongo_manager


class Article:
    collection = "articles"

    def __init__(self, category, create_time, update_time, tagLists, like_num, read_num, article):
        self.category = category
        self.create_time = create_time
        self.update_time = update_time
        self.tagLists = tagLists
        self.like_num = like_num
        self.read_num = read_num
        self.article = article

    @classmethod
    def query_by_id(cls, _id):
        """
        根据类型来查找文章
        :param _id: 文章id
        :return:
        """
        return mongo_manager.find_one(cls.collection, {"_id": ObjectId(_id)})

    @classmethod
    def save(cls, article):
        """
        保存文章
        :param article: 文章实例
        :return:
        """
        return mongo_manager.save_one(cls.collection, article).acknowledged

    @classmethod
    def update(cls, _id, data):
        """
        修改文章
        :param _id 文章id
        :param data: 文章修改的内容
        :return:
        """
        return mongo_manager.update_one(cls.collection,
                                        {"_id": ObjectId(_id)}, {"$set": data}).acknowledged

    @classmethod
    def delete(cls, ids):
        """
        删除文章
        :param ids: 类型list 文章id
        :return:
        """
        return mongo_manager.remove_many(cls.collection,
                                         {'_id': {"$in": [ObjectId(_id) for _id in ids]}}).acknowledged

    @classmethod
    def find_count(cls, query):
        """
        查询满足条件的文章数量
        :param query:
        :return:
        """
        return mongo_manager.find_count(cls.collection, query)
