import axios from "axios";
export default  {
  async talkto(types, data) {
    switch (types) {
      //创建聊天
      case "post":
      return axios.post("/api/chat/chat", data);
      //获取当前用户的聊天记录
      case "get":
        return axios.get("/api/chat/chat", {
          params: {
            target_uid: data
          }
        });
      //发消息
      case "put":
        return axios.put("/api/chat/chat", data)
      default:
        break;
    }
  },
};
