# encoding: utf-8
"""
__author__:cjhcw
"""
import os
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId
from utility import page_limit_skip
from datetime import datetime

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
    data['release_time'] = datetime.now()
    good_id = data.pop("good_id")
    return mongo_manager.update_one(goods_collection, {"_id": ObjectId(good_id)}, {"$set": data},
                                    upsert=True).acknowledged


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


def get_goods(uid, page, limit):
    """
    获取商品列表
    :param uid:
    :param page:
    :param limit:
    :return:
    """
    skip = page_limit_skip(limit, page)
    goods = list(mongo_manager.find(goods_collection, {"uid": uid}).skip(skip).limit(limit))
    for good in goods:
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        good_url = basepath + 'static/uploads_goods_photo/' + good['good_url']
        good["good_url"] = good_url
    length = mongo_manager.find_count(goods_collection, {"uid": uid})
    return goods, length
