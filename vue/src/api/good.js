import axios from "axios";
export default {
  /**发布闲置物品 */
  async realeaseUsed(types, data) {
    switch (types) {
      case "post":
      return axios.post("/api/goods/send_goods", data);
      case "delete": //删除评论
        return axios.delete("/api/goods/send_goods", {
          data
        });
      case "put":
        return axios.put("/api/goods/send_goods")
      default:
        break;
    }
  },
  async getUsedList(page, limit = 10, type, degree) {
    return axios.get("/api/goods/get_goods", {
      params: {
        page,
        limit,
        type,
        degree
      }
    })
  },
  async getGoodContent(good_id) {
    return axios.get("/api/goods/get_good_by_id", {
      params: {
        good_id
      }
    })
  },
  async changeGoodStatus(data) {
    return axios.put('/api/goods/change_good_status', data)
  }
};
