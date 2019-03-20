# encoding: utf-8
"""
__author__:cjhcw
"""
import jwt
from flask import Blueprint, jsonify, request, make_response

from database import users_db
from core_manager.mongo_manager import mongo_manager

from utility import convert_to_json

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
def get_user_info():
    """
    获取用户信息
    :return:
    """
    other_uid = request.args.get("uid")
    token = request.headers.get('Authorization')
    if token:
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = token['uid']
    else:
        uid = request.cookies.get('uid')
        if not uid:
            uid = None
    result = users_db.get_user_info(int(other_uid), int(uid))
    return jsonify(convert_to_json(result)), 200


@users.route('/get_me_info', methods=['GET'])
def get_me_info():
    """
    获取用户自己信息
    :return:
    """
    token = request.headers.get('Authorization')
    if token:
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = token["uid"]
    else:
        uid = request.cookies.get('uid')
    result = users_db.get_me_info(int(uid))
    return jsonify(convert_to_json(result)), 200


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
            if token:
                token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
                uid = token['uid']
            else:
                uid = request.cookies.get('uid')
        page = request.args.get('page')
        limit = request.args.get('limit')
        result, length = users_db.get_collections_by_uid(int(uid), page, limit)
        return jsonify({"collections": convert_to_json(result), "total": length}), 200
    elif request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        article_id = data['_id']
        result = users_db.save_collection(int(uid), article_id)
        if result:
            return jsonify({"message": "收藏文章成功", "code": 207}), 200
        else:
            return jsonify({"message": "收藏文章失败", "code": 208}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        article_ids = data['article_ids']
        result = users_db.delete_collections(int(uid), article_ids)
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
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        attention_uid = request.get_json()["attention_uid"]
        result = users_db.add_attention(int(uid), int(attention_uid))
        if result:
            return jsonify({"message": "关注成功", "code": 211}), 200
        else:
            return jsonify({"message": "关注失败", "code": 212}), 404
    elif request.method == "DELETE":
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        attention_uid = request.get_json()["attention_uid"]
        result = users_db.delete_attention(int(uid), int(attention_uid))
        if result:
            return jsonify({"message": "取关成功", "code": 213}), 200
        else:
            return jsonify({"message": "取关失败", "code": 214}), 404
    elif request.method == "GET":
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        page = request.args.get("page")
        limit = request.args.get("limit")
        result, length = users_db.get_attentions(int(uid), page, limit)
        return jsonify({"attentions": convert_to_json(result), "total": length}), 200


@users.route('/save_user_avatar', methods=["POST"])
@users_db.requires_auth
def save_user_avatar():
    """
    保存用户头像
    :return:
    """
    # 获取参数, 头像图片、用户
    token = request.headers.get('Authorization')
    if token:
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = token['uid']
    else:
        uid = request.cookies.get('uid')
    image_file = request.files.get("upload-avator")
    # 校验参数
    if image_file is None:
        # 表示用户没有上传头像
        return make_response(jsonify({"message": "未上传头像", "code": 215}), 404)

    # basepath = os.path.dirname(__file__)  # 当前文件所在路径
    # upload_path = os.path.join(basepath, 'static/uploads_user_photos',
    #                            uid + "_" + secure_filename(image_file.filename))
    # image_file.save(upload_path)

    import base64
    # 将文件名信息保存到数据库中
    bs4 = base64.b64encode(image_file.read())
    r = mongo_manager.update_one("users", {"uid": int(uid)},
                                 {"$set": {"avatar_base64": bs4}}).acknowledged
    if not r:
        return make_response(jsonify({"message": "保存头像信息失败", "code": 216}), 404)

    return make_response(jsonify({"message": "保存头像成功", "avatar_base64": bs4}), 200)


@users.route('/search_user', methods=["GET"])
@users_db.requires_auth
def search_user():
    """
    搜索用户
    :return:
    """
    keyword = request.args.get("keyword")
    users_list, total = users_db.search_user(keyword)
    return make_response(jsonify({"users": convert_to_json(users_list), "total": total}), 200)


@users.route('/reset_password_from_admin', methods=["POST"])
@users_db.requires_auth
def reset_password_from_admin():
    """
    管理员重置密码,支持批量重置
    {
        "uids":[数字类型,...]
    }
    :return:
    """
    token = request.headers.get('Authorization')
    data = request.get_json()
    result = users_db.reset_password_from_admin(token, data["uids"])
    if result:
        return jsonify({"message": "重置密码成功", "code": 217}), 200
    else:
        return jsonify({"message": "重置密码失败", "code": 218}), 404


@users.route('/user', methods=["DELETE", "PUT"])
@users_db.requires_auth
def user():
    """
    对用户的删除、更新操作,支持批量删除
    :return:
    """
    if request.method == "DELETE":
        data = request.get_json()
        result = users_db.delete_users(data["user_uids"])
        if result:
            return jsonify({"message": "删除用户成功", "code": 219}), 200
        else:
            return jsonify({"message": "删除用户失败", "code": 220}), 200
    elif request.method == "PUT":
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = users_db.edit_user_info(int(uid), data)
        if result:
            return jsonify({"message": "修改用户信息成功", "code": 205}), 200
        else:
            return jsonify({"message": "修改用户信息失败", "code": 206}), 404
