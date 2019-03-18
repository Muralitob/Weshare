# encoding: utf-8
"""
__author__:cjhcw
"""
import os
from bson import ObjectId

from core_manager.mongo_manager import mongo_manager
from models.User import User
# from models.redis_cache import redis_cache

from utility import page_limit_skip, get_this_time, get_object, get_word_escape

goods_collection = "goods"


def add_send_good(uid, data):
    """
    添加商品
    :param uid:
    :param data:
    :return:
    """
    user = User.query_one_by_uid(uid)
    data['user'] = user
    data['uid'] = uid
    data['release_time'] = get_this_time()
    new_good = mongo_manager.save_one(goods_collection, data)
    # if new_good.acknowledged:
    #     redis_cache.create_good_info_cache(new_good.inserted_id, data)
    return new_good.acknowledged


def delete_send_goods(goods_list):
    """
    删除商品
    :param goods_list:
    :return:
    """
    # redis_cache.delete_goods_cache(goods_list)
    return mongo_manager.remove_many(goods_collection,
                                     {"_id": {"$in": [ObjectId(_id) for _id in goods_list]}}).acknowledged


def edit_send_goods(data):
    """
    编辑商品
    :param data:
    :return:
    """
    _id = data['_id']
    data.pop('_id')
    return mongo_manager.update_one(goods_collection,
                                    {"_id": _id}, {"$set": data}).acknowledged


def get_goods(keyword, good_type, degree, page, limit):
    """
    获取商品列表
    :param keyword:
    :param good_type:
    :param degree:
    :param page:
    :param limit:
    :return:
    """
    query = {}
    skip, limit = page_limit_skip(limit, page)
    if keyword:
        query["title"] = {"$regex": get_word_escape(keyword)}
    if good_type:
        query["type"] = good_type
    if degree:
        query["degree"] = int(degree)
    goods = list(mongo_manager.find_select(goods_collection, query,
                                           {"pic": 0}).skip(skip).limit(limit))
    length = mongo_manager.find_count(goods_collection, query)
    return goods, length


def get_goods_by_uid(uid, keyword, good_type, degree, page, limit):
    """
    获取用户自己的商品列表
    :param uid:
    :param keyword:
    :param good_type:
    :param degree:
    :param page:
    :param limit:
    :return:
    """
    query = {}
    skip, limit = page_limit_skip(limit, page)
    if uid:
        query["uid"] = uid
    if keyword:
        query["title"] = {"$regex": get_word_escape(keyword)}
    if good_type:
        query["type"] = good_type
    if degree:
        query["degree"] = int(degree)
    goods = list(mongo_manager.find_select(goods_collection, query,
                                           {"pic": 0}).skip(skip).limit(limit))
    length = mongo_manager.find_count(goods_collection, query)
    return goods, length


def get_good_by_id(good_id):
    """
    获取当个商品的信息
    :param good_id: 商品id
    :return:
    """
    # good = redis_cache.get_redis_info("goods:info:" + str(good_id))
    # if not good:
    good = get_object(goods_collection, good_id)
    user = User.query_one_by_uid(good["uid"])
    good["user"] = user
    return good
