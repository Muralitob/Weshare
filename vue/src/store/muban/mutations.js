import * as types from '../types'
export default{
    [types.USER_LOGIN](state,token){
        localStorage.setItem('jwt',token)
        state.token=token;
    },
    [types.USER_LOGOUT](state){
        localStorage.removeItem('jwt');
        state.token = null;
    }
}
