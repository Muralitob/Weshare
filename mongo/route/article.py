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
    result = articles_db.create_new_article(data['article'], data['activeTab'], data['tagLists'], data['inputTag'])
    if result:
        return jsonify({"message": 'create new article success', "code": 200}), 200
    else:
        return jsonify({"message": 'create new article fail', "code": 200}), 200


@article.route('/get_articles_by_uid', methods=['GET'])
def get_articles_by_uid():
    """
    根据uid获取文章
    :return:
    """
    uid = request.args.get('uid')
    result = articles_db.get_articles_by_uid(uid)
    print(result)
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"message": 'get article fail', "code": 200}), 200
