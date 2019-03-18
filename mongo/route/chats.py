# encoding: utf-8
"""
__author__:cjhcw
"""
from flask_restplus import Resource
from restplus import api
from flask import request, jsonify, make_response

import jwt

from database.users_db import requires_auth
from database import chats_db

from utility import convert_to_json

chats = api.namespace('api/chat', description="chat with somebody")


@chats.route('/chat')
class Chat(Resource):

    @requires_auth
    def post(self):
        """
        创建聊天
        {"to":uid,"msg":"..."}
        :return:
        """
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = chats_db.add_new_chat(data, int(uid))
        if result:
            return make_response(jsonify({"message": "新建聊天成功", "code": 501}), 200)
        else:
            return make_response(jsonify({"message": "新建聊天失败", "code": 502}), 200)

    @requires_auth
    def get(self):
        """
        获取当前用户的聊天记录
        :return:
        """
        token = request.headers.get('Authorization')
        target = request.args.get("target_uid")
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = chats_db.get_record_by_uid(int(uid), int(target))
        return make_response(jsonify(convert_to_json(result)))

    @requires_auth
    def put(self):
        """
        发消息
        {"to":uid,"msg":"..."}
        :return:
        """
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = chats_db.add_new_msg(data, int(uid))
        if result:
            return make_response(jsonify({"message": "添加聊天成功", "code": 503}), 200)
        else:
            return make_response(jsonify({"message": "添加聊天失败", "code": 504}), 200)
