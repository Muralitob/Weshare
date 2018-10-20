# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import request
from flask import jsonify

from database.users_db import requires_auth
from database import articles_db

import utility
import jwt

articles = Blueprint("article", __name__, url_prefix='/api/article')


@articles.route('/create_new_article', methods=['POST'])
@requires_auth
def create_new_article():
    """
    新建文章
    :return:
    """
    data = request.get_json()
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    data['article']['uid'] = token['uid']
    result = articles_db.create_new_article(data)
    if result:
        if data['category'] == 'real':
            return jsonify({"code": 101}), 200
        elif data['category'] == 'fake':
            return jsonify({"code": 102}), 201
    else:
        if data['category'] == 'real':
            return jsonify({"code": 103}), 404
        elif data['category'] == 'fake':
            return jsonify({"code": 104}), 404


@articles.route('/get_articles_by_uid', methods=['GET'])
@requires_auth
def get_articles_by_uid():
    """
    根据uid获取文章
    :return:
    """
    token = request.headers.get('Authorization')
    data = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    category = request.args.get('category')
    page = request.args.get('page')
    limit = request.args.get('limit')
    result, length = articles_db.get_articles_by_uid(data['uid'], category, int(page), int(limit))
    return jsonify({"articles": utility.convert_to_json(result), "total": length}), 200


@articles.route('/edit_article_by_id', methods=['POST'])
@requires_auth
def edit_article_by_id():
    """
    根据article['id']编辑文章
    :return:
    """
    article = request.get_json()
    result = articles_db.edit_article_by_id(article)
    if result:
        return jsonify({"code": 106}), 200
    else:
        return jsonify({"code": 107}), 404


@articles.route('/delete_article_by_id', methods=['DELETE'])
@requires_auth
def delete_article_by_id():
    """
    批量删除文章
    :return:
    """
    data = request.get_json()
    article_ids = data['article_ids']
    result = articles_db.delete_article_by_id(article_ids)
    if result:
        return jsonify({"code": 108}), 200
    else:
        return jsonify({"code": 109}), 404


@articles.route('/get_real_articles', methods=['GET'])
def get_real_articles():
    """
    获取real文章
    :return:
    """
    page = request.args.get('page')
    limit = request.args.get('limit')
    result, length = articles_db.get_real_articles(page, limit)
    return jsonify({"articles": utility.convert_to_json(result), "total": length}), 200


@articles.route('/comment', methods=['POST', 'DELETE', 'PUT', 'GET'])
@requires_auth
def comments_functions():
    """
    POST新增评论,
    DELETE删除评论,
    PUT编辑评论,
    GET获取评论
    :return:
    """
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        data = request.get_json()
        parent_id = data['parent_id']
        content = data['content']
        result = articles_db.add_comment(parent_id, token['uid'], content)
        if result:
            return jsonify({"code": 110}), 200
        else:
            return jsonify({"code": 111}), 404
    elif request.method == 'DELETE':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        data = request.get_json()
        parent_id = data['parent_id']
        result = articles_db.delete_comment(parent_id, token['uid'])
        if result:
            return jsonify({"code": 112}), 200
        else:
            return jsonify({"code": 113}), 404
    elif request.method == 'PUT':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        data = request.get_json()
        parent_id = data['parent_id']
        content = data['content']
        result = articles_db.edit_comment(parent_id, token['uid'], content)
        if result:
            return jsonify({"code": 114}), 200
        else:
            return jsonify({"code": 115}), 404
    elif request.method == 'GET':
        pass


@articles.route('/like_comment', methods=['POST'])
@requires_auth
def like_comment():
    """
    评论点赞
    +1 点赞 -1 取消点赞
    :return:
    """
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    data = request.get_json()
    parent_id = data['parent_id']
    add = data['add']
    result = articles_db.like_comment(parent_id, token['uid'], int(add))
    if result:
        return jsonify({"code": 116}), 200
    else:
        return jsonify({"code": 117}), 404


@articles.route('/like_article', methods=['POST'])
@requires_auth
def like_article():
    """
    文章点赞
    +1 点赞 -1 取消点赞
    :return:
    """
    data = request.get_json()
    article_id = data['article_id']
    add = data['add']
    result = articles_db.like_article(article_id, int(add))
    if result:
        return jsonify({"code": 118}), 200
    else:
        return jsonify({"code": 119}), 404


@articles.route('/read_article', methods=['POST'])
@requires_auth
def read_article():
    """
    文章阅读数
    :return:
    """
    data = request.get_json()
    article_id = data['article_id']
    result = articles_db.read_article(article_id)
    if result:
        return jsonify({"code": 120}), 200
    else:
        return jsonify({"code": 121}), 404
