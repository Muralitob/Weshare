# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint
from flask import jsonify, make_response, request, json
import utility

from database import articles_db

article = Blueprint("article", __name__, url_prefix='/api/article')


@article.route('/create_new_article', methods=['POST'])
def create_new_article():
    """
    新建文章
    :return:
    """
    data = request.get_json()
    result = articles_db.create_new_article(data)
    if result:
        if data['category'] == 'real':
            return jsonify({"message": 'create new article success', "code": 200}), 200
        elif data['category'] == 'fake':
            return jsonify({"message": 'create new fake article success', "code": 201}), 201
    else:
        if data['category'] == 'real':
            return jsonify({"message": 'create new article fail', "code": 200}), 200
        elif data['category'] == 'fake':
            return jsonify({"message": 'create new fake article fail', "code": 201}), 201


@article.route('/get_articles_by_uid', methods=['GET'])
def get_articles_by_uid():
    """
    根据uid获取文章
    :return:
    """
    uid = request.headers.get('uid')
    category = request.args.get('category')
    result = articles_db.get_articles_by_uid(uid, category)
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"message": 'get article fail', "code": 200}), 200


@article.route('/edit_article_by_id', methods=['POST'])
def edit_article_by_id():
    """
    根据article['id']编辑文章
    :return:
    """
    article = request.get_json()
    result = articles_db.edit_article_by_id(article)
    if result:
        return jsonify({"message": 'edit article success', "code": 200}), 200
    else:
        return jsonify({"message": 'edit article fail', "code": 200}), 200


@article.route('/delete_article_by_id', methods=['DELETE'])
def delete_article_by_id():
    """
    批量删除文章
    :return:
    """
    ids = request.get_json()
    result = articles_db.delete_article_by_id(ids)
    if result:
        return jsonify({"message": 'delete articles success', "code": 200}), 200
    else:
        return jsonify({"message": 'delete articles fail', "code": 200}), 200
