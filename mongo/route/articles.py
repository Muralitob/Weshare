# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint, request, jsonify

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
    data['article']['uid'] = int(token['uid'])
    result = articles_db.create_new_article(data)
    if result:
        if data['category'] == 'real':
            return jsonify({"message": "发布文章成功", "code": 101}), 200
        elif data['category'] == 'fake':
            return jsonify({"message": "草稿箱保存成功", "code": 102}), 201
    else:
        if data['category'] == 'real':
            return jsonify({"message": "发布文章失败", "code": 103}), 404
        elif data['category'] == 'fake':
            return jsonify({"message": "草稿箱保存失败", "code": 104}), 404


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
    result, length = articles_db.get_articles_by_uid(int(data['uid']), category, page, int(limit))
    return jsonify({"articles": utility.convert_to_json(result), "total": length}), 200


@articles.route('/get_articles_by_id', methods=['GET'])
# @requires_auth
def get_articles_by_id():
    """
    根据_id获取文章
    :return:
    """
    token = request.headers.get('Authorization')
    if token:
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = int(token['uid'])
    else:
        uid = None
    article_id = request.args.get('_id')
    result = articles_db.get_articles_by_id(article_id, uid)
    if result:
        return jsonify({"articles": utility.convert_to_json(result)}), 200
    else:
        return jsonify({"message": "获取文章失败", "code": 105}), 404


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
        return jsonify({"message": "保存文章成功", "code": 106}), 200
    else:
        return jsonify({"message": "保存文章失败", "code": 107}), 404


@articles.route('/delete_article_by_id', methods=['DELETE'])
@requires_auth
def delete_article_by_id():
    """
    批量删除文章
    :return:
    """
    data = request.get_json()
    result = articles_db.delete_article_by_id(data)
    if result:
        return jsonify({"message": "删除文章成功", "code": 108}), 200
    else:
        return jsonify({"message": "删除文章失败", "code": 109}), 404


@articles.route('/get_real_articles', methods=['GET'])
def get_real_articles():
    """
    获取real文章 支持关键字搜索
    :return:
    """
    tag = request.args.get("tag")
    keyword = request.args.get('keyword')
    page = request.args.get('page')
    limit = request.args.get('limit')
    uid = request.args.get('uid')
    if not uid:
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = token['uid']
    result, length = articles_db.get_real_articles(tag, keyword, page, int(limit), int(uid))
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
        result = articles_db.add_comment(parent_id, int(token['uid']), content)
        if result:
            return jsonify({"message": "新增评论成功", "code": 110}), 200
        else:
            return jsonify({"message": "新增评论失败", "code": 111}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        _id = data['_id']
        result = articles_db.delete_comment(_id)
        if result:
            return jsonify({"message": "删除评论成功", "code": 112}), 200
        else:
            return jsonify({"message": "删除评论失败", "code": 113}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        _id = data['_id']
        content = data['content']
        result = articles_db.edit_comment(_id, content)
        if result:
            return jsonify({"message": "编辑评论成功", "code": 114}), 200
        else:
            return jsonify({"message": "编辑评论失败", "code": 115}), 404
    elif request.method == 'GET':
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = int(token['uid'])
        else:
            uid = None
        page = request.args.get('page')
        limit = request.args.get('limit')
        article_id = request.args.get('article_id')
        result, length = articles_db.get_comments(article_id, page, int(limit), uid)
        return jsonify({"comments": utility.convert_to_json(result), "total": length}), 200


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
    _id = data['_id']
    add = data['add']
    result = articles_db.like_comment(_id, int(add), int(token['uid']))
    if result:
        if add == 1:
            return jsonify({"message": "点赞成功", "code": 1161}), 200
        else:
            return jsonify({"message": "取消点赞", "code": 1162}), 200
    else:
        return jsonify({"message": "点赞/取消点赞失败", "code": 117}), 404


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
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = articles_db.like_article(article_id, add, int(token['uid']))
    if result:
        if add == 1:
            return jsonify({"message": "点赞成功", "code": 1181}), 200
        else:
            return jsonify({"message": "取消点赞", "code": 1182}), 200
    else:
        return jsonify({"message": "点赞/取消点赞失败", "code": 119}), 404


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
        return jsonify({"message": "阅读数+1", "code": 120}), 200


@articles.route('/article_history', methods=['GET', 'POST'])
@requires_auth
def article_history():
    """
    文章浏览记录
    :return:
    """
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        data = request.get_json()
        article_id = data['article_id']
        result = articles_db.add_article_history(article_id, int(token['uid']))
        if result:
            return jsonify({"message": "新增浏览记录成功", "code": 121}), 200
        else:
            return jsonify({"message": "新增浏览记录失败", "code": 122}), 404
    elif request.method == 'GET':
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        page = request.args.get('page')
        limit = request.args.get('limit')
        result, length = articles_db.get_article_history(page, int(limit), int(token['uid']))
        return jsonify({"article_history": utility.convert_to_json(result), "total": length}), 200
