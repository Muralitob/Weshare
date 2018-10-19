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


@news.route('/news', methods=['POST', 'GET', 'DELETE'])
@requires_auth
def news():
    """
    创建一条新闻,获取新闻,批量删除新闻
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()
        result = news_db.create_new_news(data)
        if result:
            return jsonify({"code": 301}), 200
        else:
            return jsonify({"code": 302}), 200
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
            return jsonify({"code": 303}), 200
        else:
            return jsonify({"code": 304}), 200


@news.route('/edit_one_new', methods=['POST'])
@requires_auth
def edit_one_new():
    """
    编辑一条新闻
    :return:
    """
    data = request.get_json()
    new_id = data['_id']
    result = news_db.edit_one_new(new_id, data)
    if result:
        return jsonify({"code": 305}), 200
    else:
        return jsonify({"code": 306}), 200
