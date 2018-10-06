# encoding: utf-8
"""
__author__:cjhcw
"""
import time
import jwt
import requests
import simplejson as json
from bson import ObjectId
from flask import request
from datetime import datetime, timedelta
from uuid import getnode as get_mac

from core_manager.mongo_manager import mongo_manager

ts = time.time()
utc_offset = (datetime.fromtimestamp(ts) -
              datetime.utcfromtimestamp(ts)).total_seconds()
UTC_ZONE = int(utc_offset / 3600)
UTC_HOURS = 24 - UTC_ZONE
Station_Type = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}
Station_Type_IDs = {
    'A': [1],
    'B': [2],
    'C': [3],
    'D': [4],
    'E': [5, 6, 7, 8, 9, 0]
}


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime):
            time_str = str(o)
            # append microsecond string, because it will be removed when
            # microsecond equal to 0
            if o.microsecond == 0:
                time_str += '.000000'
            return time_str
        return json.JSONEncoder.default(self, o)


def json_load(json_string):
    json_obj = json.loads(json_string)
    return json_obj


# convert bson to json
# 将ObjectId去除，用于Restful API传递
def convert_to_json(bson_obj):
    new_json_obj = JSONEncoder(ignore_nan=True).encode(bson_obj)
    new_json_obj = json_load(new_json_obj)
    return new_json_obj


# 获取ObjectId的实例内容
def get_object(collection, object_id):
    return mongo_manager.find_one(collection, {"_id": ObjectId(object_id)})


def get_element(collection, key, value):
    try:
        value = ObjectId(value)
    except:
        # print "no object id", value
        pass
    element = mongo_manager.find_one(collection, {key: value})
    return element


# 将string转成datetime
def convert_string_to_date(timestamp):
    if isinstance(timestamp, datetime):
        return timestamp
    timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
    utc_offset = datetime.utcnow() - datetime.now()
    timestamp = timestamp + utc_offset
    return timestamp


# 处理前端传来的日期时间格式
def format_date_time(timestring):
    formatted_time = datetime.strptime(timestring, '%Y-%m-%d %H:%M:%S.%f' + 'Z')
    return formatted_time


# def filter_help(x):
#     x = str(x)
#     if get_mac() == 14131534867685L:
#         # if platform.dist()[0] == 'centos':
#         url = 'http://60.190.248.2:9005/api/RealTimeValue/%s' % [x]
#         response = eval(requests.get(url).content)
#         print("res1", response)
#     else:
#         url = "http://122.224.116.44:3080/app/get_points_data?point_ids=%s" % [x]
#         response = eval(eval(requests.get(url).content)["response"])
#         print("res2", response)
#     if len(response) > 0:
#         return response[0]
#     else:
#         # HACK when no value response, let it be ZERO
#         return {"id": str(x), "value": 0}


def check_token():
    token = request.headers.get('Authorization')
    # return make_response(jsonify({'data': 'no auth'}), 403)
    if not token:
        return False
    data = jwt.decode(token, 'secret', algorithms=['HS256'])
    # print 'check_token', data, len(data)
    return data


def utc_today_beginning(timestamp):
    if UTC_HOURS == 24:
        return timestamp.replace(hour=16, minute=0, second=0, microsecond=0)
    if timestamp.hour < UTC_HOURS:
        timestamp = (timestamp - timedelta(days=1)).replace(hour=UTC_HOURS,
                                                            minute=0, second=0,
                                                            microsecond=0)
    else:
        timestamp = timestamp.replace(hour=UTC_HOURS, minute=0, second=0,
                                      microsecond=0)
    return timestamp


def utc_month_beginning(start_time, end_time):
    end_days = []
    cur_year = end_time.year
    for i in range(1, 13):
        end_days.append(datetime(cur_year, i, 1, 0, 0, 0) - timedelta(hours=UTC_ZONE))
    end_days.append(datetime(cur_year + 1, 1, 1, 0, 0, 0) - timedelta(hours=UTC_ZONE))
    for j in range(len(end_days)):
        if end_days[j] <= start_time < end_days[j + 1]:
            begin = j
        if end_days[j] <= end_time < end_days[j + 1]:
            end = j
    return end_days[begin:end + 1]


# 将MongoDB中的时间 "22-9月 -17" 变为格式化的 "20170922 00:00:00"
def str_json_to_date(date_string, date_string_format):
    # datetime.strptime("01-27-2012","%m-%d-%Y").strftime('%m/%d/%Y %H:%M:%S')
    # key = str(date_string.encode('utf-8').split('-'))
    date_string = filter(str.isdigit, date_string.encode('utf-8'))
    date_string = datetime.strptime(date_string, date_string_format)
    return date_string.strftime('%Y%m%d %H:%M:%S')


# 检查非时间格式字符串中是否含有中文字符
def check_contain_chinese(check_str):
    if not isinstance(check_str, datetime):
        for ch in check_str.encode('utf-8').decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
    return False


def get_this_time():
    # this_time = datetime.now().strftime("%Y%m%d %H:%M:%S")
    # 获取当前的 UTC时间 -- datetime类型值
    return datetime.utcnow()


def datetime_to_format_str(timestamp):
    # 省动环接口 utc时间戳转为字符串 协议定义：
    # datetime(2017, 1, 2, 12, 23, 40) --》 localTimeZone("20170102 20:23:40")
    utc_offset = datetime.now() - datetime.utcnow()
    timestamp += utc_offset
    return timestamp.strftime('%Y%m%d %H:%M:%S')


def format_str_to_datetime(date_string):
    # 省动环接口 字符串转换为时间格式，入库：
    # string："20170102 12:23:40"  --> datetime(2017, 1, 2, 6, 23, 40)
    if isinstance(date_string, datetime):
        return date_string
    else:
        if date_string:
            try:
                date_str = datetime.strptime(date_string, '%Y%m%d %H:%M:%S')
            except ValueError:
                date_str = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
            if date_str.year == 1:
                return date_str
            utc_offset = datetime.utcnow() - datetime.now()
            timestamp = date_str + utc_offset
            return timestamp
        else:
            return None


def int_to_hex_string_4b(a):
    n = hex(a)[2:]
    while len(n) < 4:
        n = '0' + n
    n = n.upper()
    return n


def get_this_hour_string(hour=False):
    # for 铁塔接口，文件名加时间戳定义
    if not hour:
        return datetime.now().strftime('%Y%m%d')
    return datetime.now().strftime('%Y%m%d%H')


def insert_many(collection, json_list):
    mongo_manager.insert_many(collection, json_list)


def translate_station_type(station_type=None, type_id=None):
    if station_type:
        # 传入1个或多个局站类型的字符(A,B,C,D,E)，通过转换，变为整型的TYPE_ID
        join_list = []
        if isinstance(station_type, list):
            for i in station_type:
                if i in Station_Type.values():
                    join_list += Station_Type_IDs[i]
            return join_list
        else:
            if station_type in Station_Type.values():
                print
                station_type
                join_list += Station_Type_IDs[station_type]
            return join_list
    if type_id:
        # 局站类型要进行分类判断  5-10都是其他, A,B,C,D类局站分别对应数字顺序
        if type_id in [1, 2, 3, 4, 5]:
            return Station_Type[type_id]
        else:
            return Station_Type[5]


def get_next_seq_big_id(table_name):
    try:
        one = mongo_manager.find_select_sort_limit(table_name, {}, {"ID": 1},
                                                   [('ID', -1)], 1)
        if one:
            return one[0]["ID"] + 1
        else:
            return 1
    except:
        return 1


def get_query_by_level(level, area_name=None, aid=None, net_type=None):
    query = {}
    if aid:
        query["AID"] = int(aid)
    else:
        if area_name:
            query = {"parents." + level: area_name}
        if level == "province":
            query = {"parents": {"$exists": True}}

    if net_type:
        query["NETTYPE"] = int(net_type)

    return query


def null_device_type_zero_count(device_type_counts):
    # 封装好的方法，去在aggregate的结果中加上未统计到的设备类型，以及其统计数目0
    # 现与告警设备类型统计，与资源设备类型统计 相关联。
    device_type_ids = [k["_id"] for k in device_type_counts]
    device_types = mongo_manager.aggregate("device_type", [{"$group": {
        "_id": "$_id", "count": {"$sum": 0},
        "device_type": {"$push": "$$ROOT"}}}])
    for i in device_types:
        if i["_id"] not in device_type_ids:
            device_type_counts.append(i)
    return device_type_counts


def page_limit_skip(limit=None, page=None):
    if not limit or limit == '':
        limit = 10
    if not page or page == '':
        page = 1
    skip_d = (int(page) - 1) * int(limit)
    return skip_d


def percentage_calculate(divisor_a, divisor_b, bit=None):
    """
    百分比计算 = str((divisor_a / divisor_b ) * 100) %
    :param divisor_a: 被除数
    :param divisor_b: 除数
    :param bit: 保留数位精度，默认小数点后4位
    :return:
    """
    if bit:
        bit = int(bit)
    else:
        bit = 4
    if divisor_b == 0:
        return "0.0%"
    else:
        value = round(float(divisor_a) / divisor_b, bit) * 100
        return str(value) + '%'
