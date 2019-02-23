# encoding: utf-8
"""
__author__:cjhcw
"""
import os
from bson import ObjectId
from datetime import datetime

from core_manager.mongo_manager import mongo_manager

from utility import page_limit_skip

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


def get_goods(uid, page, limit):
    """
    获取商品列表
    :param uid:
    :param page:
    :param limit:
    :return:
    """
    query = {}
    skip, limit = page_limit_skip(limit, page)
    if uid:
        query = {"uid": uid}
    goods = list(mongo_manager.find_select(goods_collection, query, {"pic": 0}).skip(skip).limit(limit))
    # for good in goods:
    #     if 'good_url' in good:
    #         basepath = os.path.dirname(__file__)  # 当前文件所在路径
    #         good_url = basepath + 'static/uploads_goods_photo/' + good['good_url']
    #         good["good_url"] = good_url
    length = mongo_manager.find_count(goods_collection, {"uid": uid})
    return goods, length


def get_good_by_id(good_id):
    """
    获取当个商品的信息
    :param good_id: 商品id
    :return:
    """
    return mongo_manager.find_one(goods_collection, {"_id": ObjectId(good_id)})
