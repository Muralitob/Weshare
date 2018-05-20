import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@pages/HomePage'
import NewsPage from '@pages/NewsPage'
import MarketPage from '@pages/MarketPage'
import CommentPage from '@pages/CommentPage'
Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: '首页',
      component: HomePage
    },
    {
      path: '/news',
      name: '新闻资讯',
      component: NewsPage
    },
    {
      path: '/market',
      name: '跳蚤市场',
      component: MarketPage
    },
    {
      path: '/commit',
      name: '交流平台',
      component: CommentPage
    },
    {
      path: '/shop',
      name: '创业板块',
      component: HomePage
    }
  ]
})
