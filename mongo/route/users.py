# encoding: utf-8
"""
__author__:cjhcw
"""
from flask import Blueprint, jsonify, request
import jwt
import os
from werkzeug.utils import secure_filename

from database import users_db
from core_manager.mongo_manager import mongo_manager
import utility

users = Blueprint("user", __name__, url_prefix='/api/user')


@users.route('/register', methods=['POST'])
def register():
    """
    注册用户
    :parameter
    account
    password
    nickname
    :return:
    """
    data = request.get_json()
    result = users_db.register(data)
    if result:
        return jsonify({"message": "注册成功", "code": 201}), 200
    else:
        return jsonify({"message": "注册失败", "code": 202}), 404


@users.route('/login', methods=['POST'])
def login():
    """
    登录(支持用户名、学号、邮箱登录)
    :parameter
    account
    password
    :return:
    """
    data = request.get_json()
    result = users_db.login(data)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"message": "登录失败", "code": 203}), 404


@users.route('/get_user_info', methods=['GET'])
@users_db.requires_auth
def get_user_info():
    """
    获取用户信息
    :return:
    """
    uid = request.args.get("uid")
    if not uid:
        token = request.headers.get('Authorization')
        data = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = data["uid"]
    result = users_db.get_user_info(int(uid))
    if result:
        return jsonify(utility.convert_to_json(result)), 200
    else:
        return jsonify({"message": "获取用户信息失败", "code": 204}), 404


@users.route('/edit_user_info', methods=['POST'])
@users_db.requires_auth
def edit_user_info():
    """
    修改用户信息
    :return:
    """
    data = request.get_json()
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    result = users_db.edit_user_info(int(token['uid']), data)
    if result:
        return jsonify({"message": "修改用户信息成功", "code": 205}), 200
    else:
        return jsonify({"message": "修改用户信息失败", "code": 206}), 404


# restful-API
# 别人也可以看到自己收藏的文章
@users.route('/collections', methods=['POST', 'DELETE', 'GET'])
@users_db.requires_auth
def collections_functions():
    """
    POST收藏文章,
    DELETE批量删除收藏的文章,
    GET获取uid下的collections收藏
    :return:
    """
    if request.method == 'GET':
        uid = request.args.get('uid')
        if not uid:
            token = request.headers.get('Authorization')
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        page = request.args.get('page')
        limit = request.args.get('limit')
        result, length = users_db.get_collections_by_uid(int(uid), page, int(limit))
        return jsonify({"collections": utility.convert_to_json(result), "total": length}), 200
    elif request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_id = data['_id']
        result = users_db.save_collection(int(token['uid']), article_id)
        if result:
            return jsonify({"message": "收藏文章成功", "code": 207}), 200
        else:
            return jsonify({"message": "收藏文章失败", "code": 208}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        article_ids = data['article_ids']
        result = users_db.delete_collections(int(token['uid']), article_ids)
        if result:
            return jsonify({"message": "删除收藏成功", "code": 209}), 200
        else:
            return jsonify({"message": "删除收藏失败", "code": 210}), 404


@users.route('/attention', methods=['POST', 'DELETE', 'GET'])
@users_db.requires_auth
def attention():
    """
    关注 取关 和关注列表
    :return:
    """
    if request.method == "POST":
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = int(token["uid"])
        attention_uid = request.get_json()["attention_uid"]
        result = users_db.add_attention(uid, int(attention_uid))
        if result:
            return jsonify({"message": "关注成功", "code": 211}), 200
        else:
            return jsonify({"message": "关注失败", "code": 212}), 404
    elif request.method == "DELETE":
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = int(token["uid"])
        attention_uid = request.get_json()["attention_uid"]
        result = users_db.delete_attention(uid, int(attention_uid))
        if result:
            return jsonify({"message": "取关成功", "code": 213}), 200
        else:
            return jsonify({"message": "取关失败", "code": 214}), 404
    elif request.method == "GET":
        token = request.headers.get('Authorization')
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = int(token["uid"])
        page = request.args.get("page")
        limit = request.args.get("limit")
        result, length = users_db.get_attentions(uid, int(page), int(limit))
        return jsonify({"attentions": utility.convert_to_json(result), "total": length}), 200


@users.route('/save_user_avatar', methods=["POST"])
@users_db.requires_auth
def save_user_avatar():
    """
    保存用户头像
    :return:
    """
    # 获取参数, 头像图片、用户
    token = request.headers.get('Authorization')
    token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
    uid = int(token["uid"])
    image_file = request.files.get("avatar")
    # 校验参数
    if image_file is None:
        # 表示用户没有上传头像
        return jsonify({"message": "未上传头像", "code": 215}), 404

    basepath = os.path.dirname(__file__)  # 当前文件所在路径
    upload_path = os.path.join(basepath, 'static/uploads_user_photos',
                               str(uid) + "_" + secure_filename(image_file.filename))
    image_file.save(upload_path)

    # 将文件名信息保存到数据库中
    r = mongo_manager.update_one("users", {"uid": uid},
                                 {"$set": {"avatar_url": str(uid) + "_" + image_file.filename}}).acknowledged
    if not r:
        return jsonify({"message": "保存头像信息失败", "code": 216}), 404

    return jsonify({"message": "保存头像成功"}), 200
