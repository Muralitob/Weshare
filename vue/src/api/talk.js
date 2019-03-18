import axios from "axios";
export default  {
  async talkto(data) {
    return axios.post("/api/user/login", data);
  },
};
