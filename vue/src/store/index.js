import Vue from 'vue'
import Vuex from 'vuex'
import UserSetting from './UserSetting'
Vue.use(Vuex);
const store = new Vuex.Store({
  modules: {
    UserSetting,
  }
})
export default store