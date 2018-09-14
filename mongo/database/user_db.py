# encoding: utf-8
"""
__author__:cjhcw
"""

from core_manager.mongo_manager import mongo_manager


def register(username, password):
    user = mongo_manager.find_one('users', {'username': username})
    if user:
        return False
    else:
        return mongo_manager.save_one('users', {'username': username, 'password': password})
