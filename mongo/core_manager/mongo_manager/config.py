# -*- code:utf-8 -*-
"""
__author__:cjhcw
"""
import os
import ConfigParser

config = ConfigParser.ConfigParser()

config_url = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')

config.read(config_url)

mongo = 'weshare'
redis = 'redis'
redis_host = 'HOST_LOCAL'


def getMongoHost():
    return config.get(mongo, 'HOST')


def getMongoUser():
    return config.get(mongo, 'USER')


def getMongoPass():
    return config.get(mongo, 'PASS')


def getMongoDB():
    return config.get(mongo, 'DB')


def getNamedQuery(name):
    return config.get('NAMED_QUERY', name)


def getNamedReturn(name):
    return config.get('NAMED_RETURN', name)


def getActiveInterface(name):
    return config.get('ACTIVE_INTERFACE', name)


def CONNECT_URI():
    username = getMongoUser()
    password = getMongoPass()
    host = getMongoHost()
    database = getMongoDB()
    return "mongodb://" + username + ":" + password + "@" + host + "/" + \
           database + "?readPreference=secondaryPreferred"


def get_REDIS_HOST():
    return config.get(redis, redis_host)


def get_REDIS_PORT():
    return config.get(redis, 'PORT')


def get_REDIS_CACHE_DB():
    return config.get(redis, 'CACHE_USER_INFO_DB')


def get_REDIS_USER_MAINTAIN_TIME():
    return config.get(redis, 'USER_STATUS_MAINTAIN_TIME')
