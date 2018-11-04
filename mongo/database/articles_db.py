# encoding: utf-8
"""
__author__:cjhcw
"""
from datetime import datetime
from core_manager.mongo_manager import mongo_manager

from bson import ObjectId

articles_collection = 'articles'
comments_collection = 'comments'
users_collection = 'users'
collcetions_collection = 'collections'
like_collection = 'like_articles'
like_comment_collection = 'like_comments'
article_history_collection = 'article_history'


def create_new_article(data):
    """
    新建文章
    :param data:
    :return:
    """
    data['create_time'] = datetime.now()
    data['update_time'] = datetime.now()
    data['like_num'] = 0
    data['read_num'] = 0
    user = mongo_manager.find_one(users_collection, {"uid": data["article"]["uid"]})
    data['article']['nickname'] = user['nickname']
    if not data['article']['nickname']:
        data['article']['nickname'] = user["account"]
    result = mongo_manager.save_one(articles_collection, data)
    return result.acknowledged


def get_articles_by_uid(uid, category, page, limit):
    """
    根据uid获取文章
    :param uid:
    :param category:
    :param page:
    :param limit:
    :return:
    """
    skip = (page - 1) * limit
    query = {'article.uid': uid, 'category': category}
    result = list(mongo_manager.find(articles_collection, query).skip(skip).limit(limit))
    length = mongo_manager.find_count(articles_collection, query)
    return result, length


def get_articles_by_id(article_id, uid):
    """
    根据_id获取文章
    :param article_id:
    :param uid:
    :return:
    """
    article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(article_id)})
    if uid:
        collection_length = list(
            mongo_manager.find(collcetions_collection, {'uid': uid, 'article_id': ObjectId(article_id)}))
        if collection_length:
            article['is_collection'] = True
        else:
            article['is_collection'] = False
        like_length = list(mongo_manager.find(like_collection, {'uid': uid, 'article_id': article['_id']}))
        if like_length:
            article['is_like'] = True
        else:
            article['is_like'] = False
    else:
        article['is_like'] = False
        article['is_collection'] = False
    return article


def edit_article_by_id(article):
    """
    根据id编辑文章
    :param article:
    :return:
    """
    _id = article.get('_id')
    if _id:
        result = mongo_manager.update_one(articles_collection, {'_id': _id}, {'$set': article})
        return result.acknowledged
    else:
        return False


def delete_article_by_id(article_ids):
    """
    批量删除文章
    :param article_ids:
    :return:
    """
    result = mongo_manager.remove_many(articles_collection, {'_id': ObjectId(_id) for _id in article_ids})
    return result.acknowledged


def like_article(article_id, add, uid):
    """
    文章点赞
    :param article_id:
    :param add: +1 点赞 -1 取消点赞
    :param uid:
    :return:
    """
    query = {'_id': ObjectId(article_id)}
    article = mongo_manager.find_one(articles_collection, query)
    if add == -1 and article['like_num'] == 0:
        return False
    elif add == -1 and article['like_num'] > 0:
        delete = mongo_manager.remove_one(like_collection,
                                          {"uid": uid, "article_id": ObjectId(article_id)}).acknowledged
        if not delete:
            return delete
    else:
        add_add = mongo_manager.save_one(like_collection, {"uid": uid, "article_id": ObjectId(article_id)}).acknowledged
        if not add_add:
            return add_add
    comment = {"$set": {'like_num': article['like_num'] + add}}
    result = mongo_manager.update_one(articles_collection, query, comment)
    return result.acknowledged


def read_article(article_id):
    """
    文章阅读数
    :param article_id:
    :return:
    """
    query = {'_id': ObjectId(article_id)}
    article = mongo_manager.find_one(articles_collection, query)
    comment = {"$set": {'read_num': article['read_num'] + 1}}
    result = mongo_manager.update_one(articles_collection, query, comment)
    return result.acknowledged


def get_real_articles(keyword, page, limit, uid):
    """
    获取category:real文章
    :param keyword:
    :param page:
    :param limit:
    :param uid
    :return:
    """
    query = {"category": "real"}
    if keyword:
        query['article.title'] = {'$regex': keyword}
    limit = int(limit)
    skip = (int(page) - 1) * limit
    result = list(mongo_manager.find(articles_collection, query).skip(skip).limit(limit).sort([("create_time", -1)]))
    if uid:
        for article in result:
            collection_length = list(
                mongo_manager.find(collcetions_collection, {'uid': uid, 'article_id': article['_id']}))
            if collection_length:
                article['is_collection'] = True
            else:
                article['is_collection'] = False
            like_length = list(mongo_manager.find(like_collection, {'uid': uid, 'article_id': article['_id']}))
            if like_length:
                article['is_like'] = True
            else:
                article['is_like'] = False
    else:
        for article in result:
            article['is_like'] = False
            article['is_collection'] = False
    length = mongo_manager.find_count(articles_collection, query)
    return result, length


def add_comment(parent_id, uid, content):
    """
    新增评论
    :param parent_id:
    :param uid:
    :param content:
    :return:
    """
    article = mongo_manager.find_one(articles_collection, {'_id': ObjectId(parent_id)})
    if article:
        is_first_comment = True
    else:
        is_first_comment = False
    user = mongo_manager.find_one(users_collection, {'uid': uid})
    comment = {'parent_id': ObjectId(parent_id), 'name': user['nickname'], 'content': content,
               'comment_time': datetime.now(),
               'is_first_comment': is_first_comment, 'like_num': 0}
    result = mongo_manager.save_one(comments_collection, comment)
    return result.acknowledged


def get_comments(article_id, page, limit, uid):
    """
    获取评论
    :param article_id:
    :param page:
    :param limit:
    :param uid:
    :return:
    """
    skip = (page - 1) * limit
    result = list(
        mongo_manager.find(comments_collection, {'parent_id': ObjectId(article_id)}).skip(skip).limit(limit).sort(
            [("comment_time", -1)]))
    for item in result:
        if uid:
            like_comment_length = list(
                mongo_manager.find(like_comment_collection, {"uid": uid, "comment": item['_id']}))
            if len(like_comment_length) == 1:
                item['is_like'] = True
            else:
                item['is_like'] = False
        else:
            item['is_like'] = False
        comments = list(mongo_manager.find(comments_collection, {'parent_id': item['_id']}))
        for comment in comments:
            if uid:
                like_next_comment_length = list(
                    mongo_manager.find(like_comment_collection, {"uid": uid, "comment": comment['_id']}))
                if len(like_next_comment_length) == 1:
                    comment['is_like'] = True
                else:
                    comment['is_like'] = False
            else:
                comment['is_like'] = False
        item['comments'] = comments
    length = mongo_manager.find_count(comments_collection, {'parent_id': ObjectId(article_id)})
    return result, length


def delete_comment(_id):
    """
    删除单条评论
    :param _id:
    :return:
    """
    return mongo_manager.remove_one(comments_collection, {'_id': ObjectId(_id)}).acknowledged


def edit_comment(_id, content):
    """
    编辑单条评论
    :param _id:
    :param content:
    :return:
    """
    query = {'_id': ObjectId(_id)}
    old_comment = mongo_manager.find_one(comments_collection, query)
    comment = {"$set": {'content': content, 'comment_time': datetime.now(), 'like_num': old_comment['like_num']}}
    result = mongo_manager.update_one(comments_collection, query, comment)
    return result.acknowledged


def like_comment(_id, add, uid):
    """
    点赞
    :param _id:
    :param add +1 点赞 -1 取消点赞
    :param uid
    :return:
    """
    query = {'_id': ObjectId(_id)}
    old_comment = mongo_manager.find_one(comments_collection, query)
    if add == -1 and old_comment['like_num'] == 0:
        return False
    elif add == -1 and old_comment['like_num'] > 0:
        delete = mongo_manager.remove_one(like_comment_collection, {"uid": uid, "comment": ObjectId(_id)})
        if not delete:
            return delete
    else:
        add_add = mongo_manager.save_one(like_comment_collection, {"uid": uid, "comment": ObjectId(_id)})
        if not add_add:
            return add_add
    comment = {"$set": {'like_num': old_comment['like_num'] + add}}
    result = mongo_manager.update_one(comments_collection, query, comment)
    return result.acknowledged


def add_article_history(article_id, uid):
    """
    添加浏览记录
    :param article_id:
    :param uid:
    :return:
    """
    result = mongo_manager.save_one(article_history_collection,
                                    {"article_id": ObjectId(article_id), "uid": uid, "create_time": datetime.now()})
    return result.acknowledged


def get_article_history(page, limit, uid):
    """
    获取用户浏览记录
    :param page:
    :param limit:
    :param uid:
    :return:
    """
    skip = (page - 1) * limit
    result = list(mongo_manager.find(article_history_collection, {"uid": uid}).skip(skip).limit(limit).sort(
        [("create_time", -1)]))
    articles_history = []
    for item in result:
        article = mongo_manager.find_one(articles_collection, {"_id": ObjectId(item["article_id"])})
        if article:
            articles_history.append(article)
    length = len(articles_history)
    return articles_history, length
