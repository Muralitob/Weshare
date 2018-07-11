import Vue from 'vue'
import App from './App'
import router from './router'
import iView from 'iview';

Vue.config.productionTip = false

import 'iview/dist/styles/iview.css'
import './scss/variable.scss'
import './scss/media-queries.scss'
import './general/js/iviewComponent';

Vue.use(iView);

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})