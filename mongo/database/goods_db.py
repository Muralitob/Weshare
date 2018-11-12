# encoding: utf-8
"""
__author__:cjhcw
"""
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId

users_collection = "users"
goods_collection = "goods"


def add_send_good(uid, data):
    """
    添加商品
    :param uid:
    :param data:
    :return:
    """
    user = mongo_manager.find_one(users_collection, {"uid": uid})
    data['user'] = user
    data['uid'] = uid
    return mongo_manager.save_one(goods_collection, data).acknowledged


def delete_send_goods(goods_list):
    """
    删除商品
    :param goods_list:
    :return:
    """
    return mongo_manager.remove_many(goods_collection, {"_id": ObjectId(_id) for _id in goods_list})


def edit_send_goods(data):
    """
    编辑商品
    :param data:
    :return:
    """
    _id = data['_id']
    data.pop('_id')
    return mongo_manager.update_one(goods_collection, {"_id": _id}, {"$set": data})
