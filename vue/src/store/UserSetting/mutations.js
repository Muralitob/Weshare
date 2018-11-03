import * as types from '../types'
import VueCookie from 'vue-cookie'
export default{
    [types.USER_LOGIN](state,obj){
        if(obj.remember) {
            localStorage.setItem('jwt',obj.token)
        }else {
            VueCookie.set('jwt', obj.token, '0');
        }
        state.token=obj.token;
    },
    [types.USER_LOGOUT](state){
        VueCookie.delete("uid");
        localStorage.removeItem('jwt');
        state.token = null;
    },
    [types.SPIN_SHOW](state,spin){
        state[spin] = !state[spin]
    },
    [types.REGIST_SHOW](state){
        state.RegistShow = !state.RegistShow
    },
    [types.LOGIN_SHOW](state){
        state.LoginShow = !state.LoginShow
    },
    [types.USER_INFO](state,data) {
        state.userInfo = data
    }
}
