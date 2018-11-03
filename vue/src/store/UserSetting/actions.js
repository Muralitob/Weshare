import * as types from "../types";
import router from "../../router";
import api from "../../api";
import crypto from "crypto";
import VueCookie from "vue-cookie";
import { Message, Spin } from "iview";
export default {
  //用户登录
  UserLogin({ commit }, { form, remember, that }) {
    const formDataMD5 = {
      account: form.account,
      pwd: setMd5(form.password)
    };
    api
      .userLogin(formDataMD5)
      .then(({ data }) => {
        console.log("登录返回信息:", data);
        if (data.code === 200) {
          commit(types.USER_LOGIN, {
            token: data.token,
            remember
          } ); //改变状态仓库
          if (remember) {
            VueCookie.set("uid", data.uid, 30 * 60);
          } else {
            VueCookie.set("uid", data.uid, "0");
          }
          that.$Spin.show();
          api.getUserInfo(data.uid).then(({ data }) => {
            commit(types.USER_INFO, data);
          });
          setTimeout(() => {
            that.$Spin.hide();
            router.push("/timeline/");
            that.$Message.info("欢迎回来!");
          }, 1000);
        }
      })
      .catch(err => {
        if (err.code === 203) {
          console.log(err);
          that.$Spin.show();
          setTimeout(() => {
            that.$Spin.hide();
            router.push("/");
            that.$Message.error("登录出错!请与管理员联系");
          }, 1000);
        } else if (data.code === 502) {
          this.$Message.error("账号或密码错误!请重新输入一遍");
        }
      });
  },
  //用户注销
  UserLogOut({ commit }, that) {
    commit(types.USER_LOGOUT);
    that.$Spin.show();
    setTimeout(() => {
      that.$Spin.hide();
      router.replace({ path: "/timeline/" });
      that.$Message.info("你已退出!");
    }, 1000);
  },
  //用户注册
  UserRegist({ commit }, { form, that }) {
    const formDataMD5 = {
      account: form.account,
      pwd: setMd5(form.password)
    };
    api
      .userRegist(formDataMD5)
      .then(({ data }) => {
        console.log(data);
        if (data.code === 201) {
          commit(types.SPIN_SHOW, "registSpinShow");
          setTimeout(function() {
            commit("SPIN_SHOW", "registSpinShow");
            // that.$Message.info('注册成功!');
            that.$Message.success({
              title: "注册提示",
              desc: "恭喜你注册成功:),赶快登陆吧！ "
            });
            commit("REGIST_SHOW");
          }, 3000);
        } else {
        }
      })
      .catch(err => {
        console.log(err);
      });
  },
  PromptReLogin({ commit }) {
    commit(types.USER_LOGOUT);
    router.replace({ path: "/" });
    Message.error("错误!请重新登录");
  }
};

function setMd5(password) {
  var md5 = crypto.createHash("sha1");
  let pw = "";
  md5.update(password);
  pw = md5.digest("hex");
  return pw;
}
