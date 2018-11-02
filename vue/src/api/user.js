import axios from "axios";
export default {
  /**用户登录 */
  async userLogin(data) {
    return axios.post("/api/user/login", data);
  },
  async userRegist(data) {
    return axios.post("/api/user/register", data);
  },
  async getUserInfo() {
    return axios.get("/api/user/get_user_info");
  },
  async editUserInfo(data) {
    return axios.post("/api/user/edit_user_info", data);
  },
  /**收藏文章方法 restful-api */
  async collectionFun(types, data, page, limit = 10) {
    switch (types) {
      case "post": //收藏文章
        console.log(data);
        return axios.post("/api/user/collections", {
          _id: data
        });
      case "delete": //取消收藏
        return axios.delete("/api/user/collections", {
          data
        });
      case "get": //获取收藏列表
        return axios.get("/api/user/collections", {
          params: {
            page,
            limit,
          }
        });
      default:
        break;
    }
  },
};
