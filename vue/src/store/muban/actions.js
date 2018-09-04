import * as types from "../types";
import router from "../../router";
import api from "../../api";
export default {
  //action 异步操作Mutation 让Mutation去改变state
  //用户登录
  UserLogin({ commit }, data) {
    api.localLogin(data).then(result => {
      if (result.data.code === 200) {
        commit(types.USER_LOGIN, result.data.token); //改变状态仓库
        router.replace({ path: "/admin" });
      } else {
        MsgAlert(result.data.message);
      }
    });
  },
  //用户注销
  UserLogOut({ commit }) {
    commit(types.USER_LOGOUT);
    router.replace({ path: "/" });
  }
  //用户注册
};
