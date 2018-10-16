# encoding: utf-8
"""
__author__:cjhcw
"""

from core_manager.mongo_manager import config
from pymongo import MongoClient

client = MongoClient(config.getMongoHost())
db = client[config.getMongoDB()]
db.authenticate(config.getMongoUser(), config.getMongoPass())


def find(collection_str, json_str):
    collection = db[collection_str]
    return collection.find(json_str)


def find_select_sort_limit(collection_str, json_str, select_str, sort_str, limit):
    collection = db[collection_str]
    # return collection.find(eval(json_str))
    return collection.find(json_str, select_str).sort(sort_str).limit(limit)


def find_sort_skip_limit(collection_str, json_str, sort_str, skip, limit):
    collection = db[collection_str]
    return collection.find(json_str).sort(sort_str).skip(skip).limit(limit)


def find_select(collection_str, json_str, select_str):
    collection = db[collection_str]
    return collection.find(json_str, select_str)


def find_limit(collection_str, json_str, limit):
    collection = db[collection_str]
    return collection.find(json_str).limit(limit)


def find_skip_limit(collection_str, json_str, skip, limit):
    collection = db[collection_str]
    return collection.find(json_str).skip(skip).limit(limit)


def find_select_skip_limit(collection_str, json_str, select_str, skip, limit):
    collection = db[collection_str]
    return collection.find(json_str, select_str).skip(skip).limit(limit)


def find_one(collection_str, json_str):
    collection = db[collection_str]
    return collection.find_one(json_str)


def find_sort(collection_str, json_str, sort_str):
    collection = db[collection_str]
    return collection.find(json_str).sort(sort_str)


def remove_one(collection_str, json_str):
    collection = db[collection_str]
    return collection.delete_one(json_str)


def save_one(collection_str, json_str):
    collection = db[collection_str]
    return collection.insert_one(json_str)


def save(collection_str, json_str):
    collection = db[collection_str]
    return collection.save(json_str)


def update_one(collection_str, find_json_str, update_json_str, upsert=False):
    # 新增upsert字段，可以在查询的时候，判断有无，然后硬更新。
    collection = db[collection_str]
    return collection.update_one(find_json_str, update_json_str, upsert)


def find_one_and_update(collection_str, find_json_str, update_json_str,
                        kwargs):
    collection = db[collection_str]
    return collection.find_one_and_update(find_json_str, update_json_str,
                                          return_document=kwargs)


def update_many(collection_str, find_json_str, update_json_str):
    collection = db[collection_str]
    return collection.update_many(find_json_str, update_json_str)


def create_one(collection_str, json_str):
    collection = db[collection_str]
    return collection.save(json_str, manipulate=False)


def count(collection_str, json_str):
    collection = db[collection_str]
    return collection.count(json_str)


def distinct(collection_str, json_str, field_str):
    collection = db[collection_str]
    return collection.distinct(field_str, json_str)


def find_count(collection_str, json_str):
    collection = db[collection_str]
    return collection.find(json_str).count()


def url():
    username = config.getMongoUser()
    password = config.getMongoPass()
    host = config.getMongoHost()
    database = config.getMongoDB()
    return "mongodb://" + username + ":" + password + "@" + host + "/" + database


def aggregate(collection_str, pipeline):
    collection = db[collection_str]
    return collection.aggregate(pipeline)


def insert_many(collection_str, pipeline):
    collection = db[collection_str]
    return collection.insert(pipeline)


def map_reduce(collection_str, map_func, reduce_func, out_place):
    collection = db[collection_str]
    return collection.map_reduce(map_func, reduce_func, out_place)


def find_projection(collection_str, json_str, projection_str):
    collection = db[collection_str]
    return collection.find(json_str, projection=projection_str)


def remove_many(collection_str, json_str):
    collection = db[collection_str]
    return collection.delete_many(json_str)
