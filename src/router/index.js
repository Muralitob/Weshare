import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@pages/HomePage'
import NewsPage from '@pages/News/NewsPage'
import NewsHome from '@pages/News/NewsHome'
import NewsArticle from '@pages/News/NewsArticle'
import MarketPage from '@pages/MarketPage'
import CommentPage from '@pages/Comment/CommentPage'
import SettingPage from '@pages/SettingPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
<<<<<<< HEAD
      name: '首页',
      component: HomePage,
      meta: { 
        ifShow: true
      }
=======
      name: 'Home',
      component: HomePage
>>>>>>> 7b99a86b791b7e0c77db611d8fce4e45116e0bda
    },
    {
      path: '/news',
      component: NewsHome,
<<<<<<< HEAD
      name: '新闻资讯',
      meta: { 
        ifShow: true
      },
      redirect: {name:'新闻资讯'},
=======
      name: 'News',
      redirect: {name:'NewList'},
>>>>>>> 7b99a86b791b7e0c77db611d8fce4e45116e0bda
      children:[
        {
          path: '/news/',
          name: 'NewsList',
          component: NewsPage,
        },
        {
          path: '/news/:id',
          name: 'NewsArticle',
          component: NewsArticle
        },
      ]
    },
    {
      path: '/setting/:userId',
      name: 'Setting',
      component: SettingPage,
      meta: { 
        ifShow: false
      }
    },
    {
      path: '/market',
<<<<<<< HEAD
      name: '跳蚤市场',
      component: MarketPage,
      meta: { 
        ifShow: true
      }
    },
    {
      path: '/commit',
      name: '交流平台',
      component: CommentPage,
      meta: { 
        ifShow: true
      }
    },
    {
      path: '/shop',
      name: '创业板块',
      component: HomePage,
      meta: { 
        ifShow: true
      }
=======
      name: 'Market',
      component: MarketPage
    },
    {
      path: '/commit',
      name: 'Commit',
      component: CommentPage
    },
    {
      path: '/shop',
      name: 'Shop',
      component: HomePage
>>>>>>> 7b99a86b791b7e0c77db611d8fce4e45116e0bda
    }
  ]
})
