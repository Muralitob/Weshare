# encoding: utf-8
"""
__author__:cjhcw
"""
import os
from flask import Blueprint, request, jsonify, make_response
from core_manager.mongo_manager import mongo_manager
from werkzeug.utils import secure_filename

from database.users_db import requires_auth
from database import goods_db
import jwt
import utility

goods = Blueprint("goods", __name__, url_prefix='/api/goods')


@goods.route('/send_goods', methods=['POST', 'DELETE', 'PUT'])
@requires_auth
def send_goods():
    """
    POST
    DELETE
    PUT
    :return:
    """
    if request.method == 'POST':
        data = request.get_json()
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
        result = goods_db.add_send_good(int(uid), data)
        if result:
            return jsonify({"message": "添加商品成功", "code": 401}), 200
        else:
            return jsonify({"message": "添加商品失败", "code": 402}), 404
    elif request.method == 'DELETE':
        data = request.get_json()
        goods_list = data['goods_list']
        result = goods_db.delete_send_goods(goods_list)
        if result:
            return jsonify({"message": "删除商品成功", "code": 403}), 200
        else:
            return jsonify({"message": "删除商品失败", "code": 404}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        result = goods_db.edit_send_goods(data)
        if result:
            return jsonify({"message": "编辑商品成功", "code": 405}), 200
        else:
            return jsonify({"message": "编辑商品失败", "code": 406}), 404


@goods.route('/get_goods', methods=["GET"])
def get_goods():
    """

    :return:
    """
    page = request.args.get("page")
    limit = request.args.get("limit")
    uid = request.args.get("uid")
    if not uid:
        token = request.headers.get('Authorization')
        if token:
            token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
            uid = token['uid']
        else:
            uid = request.cookies.get('uid')
            if not uid:
                uid = None
    goods, length = goods_db.get_goods(int(uid), page, int(limit))
    return jsonify({"goods": utility.convert_to_json(goods), "total": length}), 200


@goods.route('/save_good_photo', methods=['POST'])
@requires_auth
def save_good_photo():
    """
    保存商品图片
    :return:
    """
    token = request.headers.get('Authorization')
    if token:
        token = jwt.decode(token[6:], 'secret', algorithms=['HS256'])
        uid = token['uid']
    else:
        uid = request.cookies.get('uid')
    image_file = request.files.get("file")
    # 校验参数
    if image_file is None:
        # 表示用户没有上传商品照片
        return make_response(jsonify({"message": "未上传商品照片", "code": 407}), 404)

    # basepath = os.path.dirname(__file__)  # 当前文件所在路径
    # upload_path = os.path.join(basepath, 'static/uploads_goods_photo',
    #                            uid + "_" + secure_filename(image_file.filename))
    # image_file.save(upload_path)

    import base64
    # 将文件名信息保存到数据库中
    r = mongo_manager.save_one("goods", {"uid": int(uid), "good_base64": base64.b64encode(image_file.read())})
    if not r:
        return make_response(jsonify({"message": "保存商品照片失败", "code": 408}), 404)

    return make_response(jsonify({"message": "保存商品照片成功", "good_id": str(r.inserted_id)}), 200)
