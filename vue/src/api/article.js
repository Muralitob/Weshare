import axios from "axios";
export default {
  /**用户登录 */
  async handleArticle(data) {
    return axios.post("/api/article/create_new_article", data);
  },
};
