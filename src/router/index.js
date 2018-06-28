import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@pages/HomePage'
import NewsPage from '@pages/News/NewsPage'
import NewsHome from '@pages/News/NewsHome'
import NewsList from '@pages/News/NewsList'
import MarketPage from '@pages/MarketPage'
import CommentPage from '@pages/Comment/CommentPage'
import SettingPage from '@pages/SettingPage'

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
      component: NewsHome,
      name: '新闻资讯',
      redirect: {name:'新闻资讯'},
      children:[
        {
          path: '/news/',
          name: '新闻资讯',
          component: NewsPage,
        },
        {
          path: '/news/:id',
          name: '新闻首页',
          component: NewsList
        },
      ]
    },
    {
      path: '/setting/:userId',
      name: 'Setting',
      component: SettingPage,
      meta: { 
        notShow: false
      }
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
