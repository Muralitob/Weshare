import axios from "axios";
export default {
  /**用户登录 */
  async handleArticle(data) {
    return axios.post("/api/article/create_new_article", data);
  },
  /**获取用户个人文章,包括草稿 */
  async getArticles(category, page, limit = 10) {
    return axios.get("/api/article/get_articles_by_uid", {
      params: {
        category,
        page,
        limit
      }
    });
  },
  /**删除文章 data为文章_id数组 */
  async deleteArticles(data) {
    return axios.delete("/api/article/delete_article_by_id", {
      data
    });
  },
  /**获取所有的文章，用户首页显示 */
  async getAllArticles(page, limit = 10) {
    return axios.get("/api/article/get_real_articles", {
      params: {
        page,
        limit
      }
    });
  },
  /**根据文章id获取文章详情 */
  async getArticleById(_id) {
    return axios.get("/api/article/get_articles_by_id", {
      params: {
        _id
      }
    });
  },
  /**文章回复 */
  async commentArticle(types, data, page, limit = 10) {
    switch (types) {
      case "post": //新增评论
        console.log(data);
        return axios.post("/api/article/comment", data);
      case "delete": //删除评论
        return axios.delete("/api/article/comment", {
          data
        });
      case "put":
        // return axios.put("/api/article/get_articles_by_id")
        break;
      case "get": //获取评论
        return axios.get("/api/article/comment", {
          params: {
            page,
            limit,
            article_id: data
          }
        });
      default:
        break;
    }
  },
  //修改文章浏览数
  async countArticle(data) {
    return axios.post("/api/article/read_article", {
      article_id: data
    });
  },
  //评论点赞 add: 1 +1  -1 -1
  async addLikeComment(add, _id) {
    return axios.post("/api/article/like_comment", {
      add,
      _id
    });
  },
  //文章点赞 add: 1 +1  -1 -1
  async addLikeArticle(add, _id) {
    return axios.post("/api/article/like_comment", {
      add,
      _id
    });
  },
  async historyFunction(type, data, page, limit = 10 ) {
    if (type === "post") {
      return axios.post("/api/article/article_history", {
        article_id: data
      });
    } else if (type === "get") {
      return axios.get("/api/article/article_history", {
        params: {
          page,
          limit,
        }
      });
    }
  }
};
