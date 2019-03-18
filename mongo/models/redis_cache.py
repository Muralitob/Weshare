# # -*- coding: UTF-8 -*-
# """
# author: cjhcw
# """
# import pickle
# import redis
# from redis import StrictRedis, ConnectionError
# from core_manager.mongo_manager import config
# from celery import Celery
#
# celery = Celery("redis_cache", broker=config.CONNECT_URI())
# # redis的默认参数(host， port, db)其中db为定义redis database的数量
# redis_kwargs = {
#     "host": config.get_REDIS_HOST(),
#     "port": config.get_REDIS_PORT(),
#     "db": config.get_REDIS_CACHE_DB()
# }
#
#
# class RedisCacheData(object):
#     redis_conn = None
#
#     def __init__(self):
#         rs = redis.Redis(host=config.get_REDIS_HOST(),
#                          port=config.get_REDIS_PORT(),
#                          db=config.get_REDIS_CACHE_DB())
#         try:
#             rs.ping()
#             self.redis_conn = StrictRedis(**redis_kwargs)
#         except ConnectionError:
#             self.redis_conn = None
#
#     def delete(self, key):
#         # 删除key缓存在redis中的信息
#         self.redis_conn.delete(key)
#
#     # @celery.task
#     def create_good_info_cache(self, good_id, good_info):
#         if not self.redis_conn:
#             return None
#         info = pickle.dumps(good_info)
#         self.redis_conn.setex("goods:info:" + str(good_id), config.get_REDIS_USER_MAINTAIN_TIME(), info)
#
#     # @celery.task
#     def delete_goods_cache(self, goods_list):
#         for item in goods_list:
#             self.redis_conn.delete("goods:info:" + str(item))
#
#     def exists_redis(self, key):
#         return self.redis_conn.exists(key)
#
#     def get_redis_info(self, key):
#         if not self.redis_conn:
#             return None
#         # 获取redis中缓存的信息，这里的查询，传入的参数必须加前缀
#         value = self.redis_conn.get(key)
#         return pickle.loads(value) if value else None
#
#     # @celery.task
#     def create_redis_info_cache(self, key, value):
#         new_message = pickle.dumps(value)
#         self.redis_conn.setex(key, 300, new_message)
#
#     # redis中的hash存储
#     def update_redis_hash_info(self, key, hkey, value):
#         new_message = pickle.dumps(value)
#         self.redis_conn.hset(key, hkey, new_message)
#
#     def get_redis_hash(self, key, hkey):
#         message = self.redis_conn.hget(key, hkey)
#         new_message = pickle.loads(message)
#         return new_message
#
#     def exists_redis_hash(self, key, hkey):
#         res = self.redis_conn.hexists(key, hkey)
#         if res:
#             return res
#         else:
#             return None
#
#
# redis_cache = RedisCacheData()
