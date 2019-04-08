# encoding: utf-8
"""
__author__:cjhcw
"""

from core_manager.mongo_manager import mongo_manager
from bson import ObjectId
from models.User import User

if __name__ == '__main__':
    # users = mongo_manager.find('users', {})
    # for item in users:
    #     mongo_manager.update_one('users', {'_id': item['_id']}, {"$set": {'nickname': item['account']}})
    # print User.query_one("cwt")
    # articles = list(mongo_manager.find("goods", {}))
    # for item in articles:
    #     r = mongo_manager.update_one("goods", {"_id": item["_id"]},
    #                                  {"$unset": {"user": 0}})
    #     print r.acknowledged
    # print list(mongo_manager.find("chats", {"$and": [{"relations": 101, }, {"relations": 109, }]}))
    # pwd = "cjhcw19960920"
    # import hashlib
    #
    # import md5
    #
    # m1 = md5.new()
    # m1.update(pwd)
    # print m1.hexdigest()
    # m2 = hashlib.md5()
    # m2.update(pwd)
    # print m2.hexdigest()
    # aa77aa4d02340cb0ac757e1ed84d68d73667f16d
    r = mongo_manager.update_many("goods", {}, {"$set": {"status": 0}})
    print r.acknowledged
    pass
