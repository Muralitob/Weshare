import axios from "axios";
export default {
  /**用户登录 */
  async handleArticle(data) {
    return axios.post("/api/article/create_new_article", data);
  },
  async getArticles(category) {
    return axios.get("api/article/get_articles_by_uid",{
      params: {
        category
      }
    })
  }
};
