import Vue from 'vue'
import Vuex from 'vuex'
import UserSetting from './UserSetting'
import Menu from './Menu'
Vue.use(Vuex);
const store = new Vuex.Store({
  modules: {
    UserSetting,
    Menu,
  }
})
export default store