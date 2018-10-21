# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import request
from flask import jsonify

from database.users_db import requires_auth
from database import news_db

import utility

news = Blueprint("news", __name__, url_prefix='/api/news')


# restful-API
@news.route('/news', methods=['POST', 'GET', 'DELETE', 'PUT'])
@requires_auth
def news_functions():
    """
    POST创建一条新闻,
    GET获取全部新闻,
    DELETE批量删除新闻,
    PUT更新一条新闻内容
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()
        result = news_db.create_new_news(data)
        if result:
            return jsonify({"message": "创建新闻成功", "code": 301}), 200
        else:
            return jsonify({"message": "创建新闻失败", "code": 302}), 404
    elif request.method == 'GET':
        page = request.args.get('page')
        limit = request.args.get('limit')
        result, length = news_db.get_all_news(int(page), int(limit))
        return jsonify({"news": utility.convert_to_json(result), "total": length}), 200
    elif request.method == 'DELETE':
        data = request.get_json()
        news_ids = data['ids']
        result = news_db.delete_news_by_id(news_ids)
        if result:
            return jsonify({"message": "批量删除新闻成功", "code": 303}), 200
        else:
            return jsonify({"message": "批量删除新闻失败", "code": 304}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        new_id = data['_id']
        result = news_db.edit_one_new(new_id, data)
        if result:
            return jsonify({"message": "保存新闻成功", "code": 305}), 200
        else:
            return jsonify({"message": "保存新闻失败", "code": 306}), 404
