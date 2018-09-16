import axios from 'axios'
export default {
  /**用户登录 */
  userLogin(data) {
    return axios.post('/api/user/login', data)
  },
  userRegist(data) {
    return axios.post('/api/user/register', data)
  }
}