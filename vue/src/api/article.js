import axios from "axios";
export default {
  /**用户登录 */
  async handleArticle(data) {
    return axios.post("/api/article/create_new_article", data);
  },
  /**获取用户个人文章,包括草稿 */
  async getArticles(category) {
    return axios.get("api/article/get_articles_by_uid",{
      params: {
        category
      }
    })
  },
  /**删除文章 data为文章_id数组 */
  async deleteArticles(data) {
    return axios.delete("api/article/delete_article_by_id",data)
  },
};
