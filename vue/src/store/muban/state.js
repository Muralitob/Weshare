// 各种Store
export default {
  token: isLoggedIn() || null,
  progress: 0,
  headline: ""
  // 每次刷新页面或者再次访问的时候都会重新渲染状态,
  // 这里相当于给每次刷新重新设置初始值
};