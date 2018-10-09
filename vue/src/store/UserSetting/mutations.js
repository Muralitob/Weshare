import * as types from '../types'
export default{
    [types.USER_LOGIN](state,token){
        localStorage.setItem('jwt',token)
        state.token=token;
    },
    [types.USER_LOGOUT](state){
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
