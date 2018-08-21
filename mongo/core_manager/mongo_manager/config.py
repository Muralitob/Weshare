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
