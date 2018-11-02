// 各种Store
import VueCookie from 'vue-cookie'
export default {
  token: isLoggedIn() || null,
  UserId: VueCookie.get('uid') || null ,
  progress: 0,
  headline: "",
  registSpinShow: false,
  RegistShow: false,
  LoginShow: false,
  userInfo: {}
};

function isLoggedIn() {
  let token = VueCookie.get('jwt')  || localStorage.getItem("jwt");
  if (token) {
    const payload = JSON.parse(window.atob(token.split(".")[1]));
    console.log(payload)
    // // 前端判断token是否过期，如果过期了访问时候会路由到login页面
    // if (payload.exp > Date.now() / 1000) {
    //   return token;
    // }
    return token;
  } else {
    return false;
  }
}
