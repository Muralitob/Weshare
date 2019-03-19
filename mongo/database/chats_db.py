# encoding: utf-8
"""
__author__:cjhcw
"""
from core_manager.mongo_manager import mongo_manager

from utility import get_this_time

chats_collection = "chats"


def add_new_chat(data, uid):
    """
    新建聊天
    :param data:
    :param uid:
    :return:
    """
    data.update({"from": uid, "time": get_this_time()})
    chat = {
        "relations": [uid, int(data["to"])],
        "content": [data]
    }
    record = mongo_manager.find_one(chats_collection,
                                    {"$and": [{"relations": uid}, {"relations": data["to"]}]})
    if record:
        record["content"].append(data)
        record.pop("relations")
        return mongo_manager.update_one(chats_collection, {"_id": record.pop("_id")},
                                        {"$set": record}).acknowledged
    else:
        return mongo_manager.save_one(chats_collection, chat).acknowledged


def get_record_by_uid(uid, target):
    """
    用户记录
    :param uid:
    :param target:
    :return:
    """
    query = {"relations": {"$in": [uid]}}
    if target:
        target = int(target)
        query = {"$and": [{"relations": uid}, {"relations": target}]}
        record = mongo_manager.find_one(chats_collection, query)
        if not record:
            chat = {
                "relations": [uid, target],
                "content": []
            }
            _id = mongo_manager.save_one(chats_collection, chat).inserted_id
            return mongo_manager.find_one(chats_collection, {"_id": _id})
        else:
            return record
    records = list(mongo_manager.find(chats_collection, query))
    return records


def add_new_msg(data, uid):
    """
    后续聊天
    :param data:
    :param uid:
    :return:
    """
    data.update({"from": uid, "time": get_this_time()})
    record = mongo_manager.find_one(chats_collection,
                                    {"$and": [{"relations": uid}, {"relations": data["to"]}]})
    record["content"].append(data)
    record.pop("relations")
    return mongo_manager.update_one(chats_collection, {"_id": record.pop("_id")},
                                    {"$set": record}).acknowledged
