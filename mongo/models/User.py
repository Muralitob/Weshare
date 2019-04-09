# encoding: utf-8
"""
__author__:cjhcw
"""
from core_manager.mongo_manager import mongo_manager


class User:
    collection = "users"

    def __init__(self, account, pwd, level, uid, major, nickname, birthday, sign, branch, sex, register_time,
                 login_time):
        self.account = account
        self.pwd = pwd
        self.level = level
        self.uid = uid
        self.major = major
        self.nickname = nickname
        self.birthday = birthday
        self.sign = sign
        self.branch = branch
        self.sex = sex
        self.register_time = register_time
        self.login_time = login_time

    @classmethod
    def query_one(cls, account):
        """
        根据账号查询用户
        :param account: 用户账号
        :return:
        """
        return mongo_manager.find_one(cls.collection,
                                      {"account": account})

    @classmethod
    def query_one_by_uid(cls, uid):
        """
        根据用户ID查询用户
        :param uid: 用户ID
        :return:
        """
        return mongo_manager.find_one(cls.collection,
                                      {"uid": uid})

    @classmethod
    def update_one(cls, account, data):
        """
        查询账号并对此账号做修改
        :param account: 用户账号
        :param data: 修改内容
        :return:
        """
        return mongo_manager.update_one(cls.collection,
                                        {"account": account},
                                        {"$set": data}).acknowledged

    @classmethod
    def update_one_by_uid(cls, uid, data):
        """
        查询账号并对此账号做修改
        :param uid: 用户id
        :param data: 修改内容
        :return:
        """
        return mongo_manager.update_one(cls.collection,
                                        {"account": uid},
                                        {"$set": data}).acknowledged

    @classmethod
    def save_one(cls, data):
        """
        保存用户
        :param data: 用户信息
        :return:
        """
        return mongo_manager.save_one(cls.collection, data).acknowledged
