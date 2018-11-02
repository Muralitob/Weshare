import Vue from "vue";
import App from "./App";
import router from "./router";
import iView from "iview";
import VueInsProgressBar from "vue-ins-progress-bar";
import store from "./store/index";
import axios from "axios";
import VueCookie from "vue-cookie";
import VueQuillEditor from "vue-quill-editor";
import VueStar from "vue-star";
Vue.config.productionTip = false;

import "iview/dist/styles/iview.css";
import "./scss/variable.scss";
import "./scss/media-queries.scss";
import "./general/js/iviewComponent";
import "../my-theme/index.less";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

//每个请求都带上token
axios.interceptors.request.use(
  config => {
    if (store.state.UserSetting.token) {
      config.headers.Authorization = `token ${store.state.UserSetting.token}`;
    }
    return config;
  },
  err => {
    return Promise.reject(err);
  }
);

axios.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response) {
      switch (error.response.status) {
        case 401:
          // 返回 401 清除token信息并跳转到登录页面
          Message.error("错误!请重新登录");
          store.dispatch("PromptReLogin");
      }
    }
    return Promise.reject(error.response.data); // 返回接口返回的错误信息
  }
);
const options = {
  position: "fixed",
  show: true,
  height: "3px"
};

Vue.component("VueStar", VueStar);
Vue.use(VueInsProgressBar, options);
Vue.use(iView);
Vue.use(VueCookie);
Vue.use(VueQuillEditor);

new Vue({
  el: "#app",
  router,
  store,
  components: { App },
  template: "<App/>"
});
