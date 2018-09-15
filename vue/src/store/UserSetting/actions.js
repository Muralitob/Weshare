import * as types from "../types";
import router from "../../router";
import api from "../../api";
import crypto from 'crypto'
export default {
  //action 异步操作Mutation 让Mutation去改变state
  //用户登录
  UserLogin({ commit }, data) {
    const formDataMD5 = {
      account: data.account,
      pwd: setMd5(data.password)
    }
    console.log(formDataMD5);
    api.userLogin(formDataMD5).then(result => {
      if (result.data.code === 200) {
        commit(types.USER_LOGIN, result.data.token); //改变状态仓库
        router.replace({ path: "/" }); //跳到首页
      } else {
      }
    });
  },
  //用户注销
  UserLogOut({ commit }) {
    commit(types.USER_LOGOUT);
    router.replace({ path: "/" });
  },
  //用户注册
  UserRegist({ commit }, data) {
    const formDataMD5 = {
      account: data.account,
      pwd: setMd5(data.password)
    }
    console.log(formDataMD5)
    api.userRegist(formDataMD5).then(result => {
      if (result.data.code === 200) {
        // commit(types.USER_LOGIN, result.data.token); //改变状态仓库
        console.log('成功');
      } else {
      }
    });
  }
};

function setMd5(password){
  var md5 = crypto.createHash("sha1")
  let pw = '';
  md5.update(password)
  pw = md5.digest('hex')
  return pw;
}