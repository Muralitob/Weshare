import * as types from "../types";
import router from "../../router";
import api from "../../api";
import crypto from 'crypto'
export default {
  //用户登录
  UserLogin({ commit }, { form , remember, that }) {
    const formDataMD5 = {
      account: form.account,
      pwd: setMd5(form.password)
    }
    api.userLogin(formDataMD5).then(({data}) => {
      if (data.code === 200) {
        commit(types.USER_LOGIN, data.message.token); //改变状态仓库
        that.$Spin.show();
        setTimeout(() => {
          that.$Spin.hide();
          router.push('/')
        that.$Message.info('欢迎回来!');
        }, 1000);
      } else if(data.code === 502) {
        // this.$Message.info('账号或密码错误!');
      } else if(data.code === 404) {
        // this.$Message.info('出问题了!');
      }
    });
  },
  //用户注销
  UserLogOut({ commit }, that) {
    commit(types.USER_LOGOUT);
    that.$Spin.show();
    setTimeout(() => {
      that.$Spin.hide();
      router.replace({ path: "/" });
      that.$Message.info('你已退出!');
    }, 1000);
    
  },
  //用户注册
  UserRegist({ commit }, { form , that }) {
    const formDataMD5 = {
      account: form.account,
      pwd: setMd5(form.password)
    }
    api.userRegist(formDataMD5).then(({data}) => {
      if (data.code === 200) {
        commit(types.SPIN_SHOW,'registSpinShow');
        setTimeout(function(){
          commit('SPIN_SHOW', 'registSpinShow')
          that.$Notice.success({
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