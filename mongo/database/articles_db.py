# encoding: utf-8
"""
__author__:cjhcw
"""
from bson import ObjectId

from core_manager.mongo_manager import mongo_manager
from models.User import User
from models.Article import Article
from models.Collection import Collection
from models.Like import Like

from utility import page_limit_skip, get_this_time

articles_collection = 'articles'
comments_collection = 'comments'
collcetions_collection = 'collections'
like_collection = 'like_articles'
like_comment_collection = 'like_comments'
article_history_collection = 'article_history'
announcements_collection = 'announcements'


def create_new_article(data):
    """
    新建文章
    :param data:
    :return:
    """
    data['create_time'] = get_this_time()
    data['update_time'] = get_this_time()
    data['like_num'] = 0
    data['read_num'] = 0
    user = User.query_one_by_uid(data["article"]["uid"])
    data['article']['nickname'] = user['nickname']
    # if not data['article']['nickname']:
    #     data['article']['nickname'] = user["account"]
    return Article.save(data)


def get_articles_by_uid(uid, category, page, limit):
    """
    根据uid获取文章
    :param uid:
    :param category:
    :param page:
    :param limit:
    :return:
    """
    skip, limit = page_limit_skip(limit, page)
    query = {'article.uid': uid, 'category': category}
    result = list(
        mongo_manager.find(articles_collection, query).skip(skip).limit(limit).sort([("update_time", -1)]))
    length = Article.find_count(query)
    return result, length


def get_articles_by_id(article_id, uid):
    """
    根据_id获取文章
    :param article_id:
    :param uid:
    :return:
    """
    article = Article.query_by_id(article_id)
    if uid:
        article['is_collection'] = Collection.query_collection_by_uid_and_aid(uid, article_id)
        article['is_like'] = Like.query_like_article_by_uid_and_aid(uid, article_id)
    else:
        article['is_like'] = False
        article['is_collection'] = False
    article["col_num"] = Collection.find_count_collection(article_id)
    article["like_num"] = Like.find_count_like_article(article_id)
    return article


def edit_article_by_id(article):
    """
    根据id编辑文章
    :param article:
    :return:
    """
    _id = article.get('_id')
    article['update_time'] = get_this_time()
    if _id:
        return Article.update(_id, article)
    return False


def delete_article_by_id(article_ids):
    """
    批量删除文章
    :param article_ids:
    :return:
    """
    return Article.delete(article_ids)


def like_article(article_id, add, uid):
    """
    文章点赞
    :param article_id:
    :param add: +1 点赞 -1 取消点赞
    :param uid:
    :return:
    """
    article = Article.query_by_id(article_id)
    if add == -1 and article['like_num'] == 0:
        return False
    elif add == -1 and article['like_num'] > 0:
        delete = mongo_manager.remove_one(like_collection,
                                          {"uid": uid, "article_id": ObjectId(article_id)}).acknowledged
        if not delete:
            return delete
    else:
        add_add = mongo_manager.save_one(like_collection,
                                         {"uid": uid, "article_id": ObjectId(article_id)}).acknowledged
        if not add_add:
            return add_add
    return Article.update(article_id, {'like_num': article['like_num'] + add})


def read_article(article_id):
    """
    文章阅读数
    :param article_id:
    :return:
    """
    article = Article.query_by_id(article_id)
    return Article.update(article_id, {'read_num': article['read_num'] + 1})


def get_real_articles(tag, keyword, page, limit, uid):
    """
    获取category:real文章
    :param tag:
    :param keyword:
    :param page:
    :param limit:
    :param uid:
    :return:
    """
    query = {"category": "real"}
    if tag:
        query["tagLists"] = tag
    if keyword:
        query['article.title'] = {'$regex': keyword}
    skip, limit = page_limit_skip(limit, page)
    result = list(mongo_manager.find(articles_collection,
                                     query).skip(skip).limit(limit).sort([("create_time", -1)]))
    if uid:
        for article in result:
            if uid:
                article['is_collection'] = Collection.query_collection_by_uid_and_aid(uid, article["_id"])
                article['is_like'] = Like.query_like_article_by_uid_and_aid(uid, article["_id"])
            else:
                article['is_like'] = False
                article['is_collection'] = False
            article["col_num"] = Collection.find_count_collection(article["_id"])
            article["like_num"] = Like.find_count_like_article(article["_id"])
    else:
        for article in result:
            article['is_like'] = False
            article['is_collection'] = False
            article["col_num"] = Collection.find_count_collection(article["_id"])
            article["like_num"] = Like.find_count_like_article(article["_id"])
    length = Article.find_count(query)
    return result, length


def add_comment(parent_id, uid, content):
    """
    新增评论
    :param parent_id:
    :param uid:
    :param content:
    :return:
    """
    article = Article.query_by_id(parent_id)
    if article:
        is_first_comment = True
    else:
        is_first_comment = False
    user = User.query_one_by_uid(uid)
    comment = {'parent_id': ObjectId(parent_id),
               'name': user['nickname'],
               'content': content,
               'comment_time': get_this_time(),
               'is_first_comment': is_first_comment,
               'like_num': 0}
    return mongo_manager.save_one(comments_collection, comment).acknowledged


def get_comments(article_id, page, limit, uid):
    """
    获取评论
    :param article_id:
    :param page:
    :param limit:
    :param uid:
    :return:
    """
    skip, limit = page_limit_skip(limit, page)
    result = list(
        mongo_manager.find(comments_collection, {'parent_id': ObjectId(article_id)}).skip(skip).limit(limit).sort(
            [("comment_time", -1)]))
    for item in result:
        item["comments"] = get_comments_from_front(uid, item["_id"])
    length = mongo_manager.find_count(comments_collection, {'parent_id': ObjectId(article_id)})
    return result, length


def get_comments_from_front(uid, comment_id):
    """
    递归获取所有相关评论
    :param uid:
    :param comment_id:
    :return:
    """
    next_comments = list(mongo_manager.find(comments_collection, {"parent_id": comment_id}))
    if next_comments:
        for item in next_comments:
            if uid:
                item['is_like'] = Like.query_like_comment_by_uid_and_comment(uid, item["_id"])
            else:
                item['is_like'] = False
            item["comments"] = get_comments_from_front(uid, item["_id"])
        return next_comments
    return []


def delete_comment(_id):
    """
    删除单条评论
    :param _id:
    :return:
    """
    return mongo_manager.remove_one(comments_collection,
                                    {'_id': ObjectId(_id)}).acknowledged


def edit_comment(_id, content):
    """
    编辑单条评论
    :param _id:
    :param content:
    :return:
    """
    query = {'_id': ObjectId(_id)}
    old_comment = mongo_manager.find_one(comments_collection, query)
    comment = {"$set": {'content': content,
                        'comment_time': get_this_time(),
                        'like_num': old_comment['like_num']}}
    return mongo_manager.update_one(comments_collection, query, comment).acknowledged


def like_comment(_id, add, uid):
    """
    点赞
    :param _id:
    :param add: +1 点赞 -1 取消点赞
    :param uid:
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
    return mongo_manager.update_one(comments_collection, query, comment).acknowledged


def add_article_history(article_id, uid):
    """
    添加浏览记录
    :param article_id:
    :param uid:
    :return:
    """
    top_history = list(mongo_manager.find(article_history_collection, {"uid": uid}).sort([("create_time", -1)]))
    if top_history and top_history[0].get("article_id") == ObjectId(article_id):
        return True
    else:
        return mongo_manager.save_one(article_history_collection,
                                      {"article_id": ObjectId(article_id), "uid": uid,
                                       "create_time": get_this_time()}).acknowledged


def get_article_history(page, limit, uid):
    """
    获取用户浏览记录
    :param page:
    :param limit:
    :param uid:
    :return:
    """
    skip, limit = page_limit_skip(limit, page)
    result = list(mongo_manager.find(article_history_collection,
                                     {"uid": uid}).skip(skip).limit(limit).sort([("create_time", -1)]))
    articles_history = []
    for item in result:
        article = Article.query_by_id(item["article_id"])
        if article:
            articles_history.append(article)
    length = mongo_manager.find_count(article_history_collection, {"uid": uid})
    return articles_history, length


def get_announcements(page, limit):
    """
    获取公告
    :param page:
    :param limit:
    :return:
    """
    skip, limit = page_limit_skip(limit, page)
    announcements = list(mongo_manager.find_skip_limit(announcements_collection, {}, skip, limit))
    count = mongo_manager.find_count(announcements_collection, {})
    return announcements, count


def edit_announcement(data):
    """
    编辑公告
    :param data:
    :return:
    """
    data["update_time"] = get_this_time()
    return mongo_manager.update_one(announcements_collection,
                                    {"_id": ObjectId(data.pop("_id"))}, {"$set": data}).acknowledged


def delete_announcements(_ids):
    """
    批量删除公告
    :param _ids:
    :return:
    """
    return mongo_manager.remove_many(announcements_collection,
                                     {"_id": ObjectId(_id) for _id in _ids}).acknowledged


def add_announcement(data):
    """
    新增公告
    :param data:
    :return:
    """
    data["update_time"] = get_this_time()
    data["create_time"] = get_this_time()
    return mongo_manager.save_one(announcements_collection, data).acknowledged


def get_hot_articles(uid):
    """
    获取热门文章top10
    :param uid:
    :return:
    """
    query = {"category": "real"}
    result = list(
        mongo_manager.find(articles_collection, query).sort([("like_num", -1)]).limit(10))
    if uid:
        for article in result:
            if uid:
                article['is_collection'] = Collection.query_collection_by_uid_and_aid(uid, article["_id"])
                article['is_like'] = Like.query_like_article_by_uid_and_aid(uid, article["_id"])
            else:
                article['is_like'] = False
                article['is_collection'] = False
            article["col_num"] = Collection.find_count_collection(article["_id"])
            article["like_num"] = Like.find_count_like_article(article['_id'])
    else:
        for article in result:
            article['is_like'] = False
            article['is_collection'] = False
            article["col_num"] = Collection.find_count_collection(article["_id"])
            article["like_num"] = Like.find_count_like_article(article['_id'])
    return result
