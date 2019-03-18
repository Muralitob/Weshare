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
    articles = list(mongo_manager.find("goods", {}))
    for item in articles:
        r = mongo_manager.update_one("goods", {"_id": item["_id"]},
                                     {"$unset": {"user": 0}})
        print r.acknowledged
    pass
