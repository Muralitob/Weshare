import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview';
import VueInsProgressBar from 'vue-ins-progress-bar'
import store from './store/index';

Vue.config.productionTip = false

import 'iview/dist/styles/iview.css'
import './scss/variable.scss'
import './scss/media-queries.scss'
import './general/js/iviewComponent';
import '../my-theme/index.less';

const options = {
  position: 'fixed',
  show: true,
  height: '3px'
}

Vue.use(VueInsProgressBar, options)
Vue.use(iView);

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})