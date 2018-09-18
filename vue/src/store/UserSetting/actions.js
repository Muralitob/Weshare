import * as types from "../types";
import router from "../../router";
import api from "../../api";
import crypto from 'crypto'
export default {
  //action 异步操作Mutation 让Mutation去改变state
  //用户登录
  UserLogin({ commit }, { form , remember, that }) {
    const formDataMD5 = {
      account: form.account,
      pwd: setMd5(form.password)
    }
    api.userLogin(formDataMD5).then(({data}) => {
      if (data.code === 200) {
        commit(types.USER_LOGIN, data.message.token); //改变状态仓库
        that.$Message.info('欢迎回来!');
      } else if(data.code === 502) {
        // this.$Message.info('账号或密码错误!');
      } else if(data.code === 404) {
        // this.$Message.info('出问题了!');
      }
    });
  },
  //用户注销
  UserLogOut({ commit }) {
    commit(types.USER_LOGOUT);
    router.replace({ path: "/" });
  },
  //用户注册
  UserRegist({ commit }, obj) {
    const formDataMD5 = {
      account: obj.form.account,
      pwd: setMd5(obj.form.password)
    }
    api.userRegist(formDataMD5).then(result => {
      if (result.data.code === 200) {
        commit(types.SPIN_SHOW,'registSpinShow');
        setTimeout(function(){
          commit('SPIN_SHOW', 'registSpinShow')
          obj.this.$Notice.success({
            title: '注册提示',
            desc: '恭喜你注册成功:),赶快登陆吧！ '
          });
          commit('REGIST_SHOW')
        },3000)
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