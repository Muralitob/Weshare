import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@pages/HomePage'
import NewsPage from '@pages/News/NewsPage'
import NewsHome from '@pages/News/NewsHome'
import NewsArticle from '@pages/News/NewsArticle'
import MarketPage from '@pages/MarketPage'
import CommentPage from '@pages/Comment/CommentPage'
import SpacePage from '@pages/SpacePage'
import SpaceIndex from '@pages/SpacePage/SpaceIndex'
import SpaceArticle from '@pages/SpacePage/SpaceArticle'
import SpaceCollection from '@pages/SpacePage/SpaceCollection'
import SpaceHistory from '@pages/SpacePage/SpaceHistory'
import SpaceFan from '@pages/SpacePage/SpaceFan'
import SettingPage from '@pages/Setting'
import SettingInfo from '@pages/Setting/SettingInfo'
import SettingAvator from '@pages/Setting/SettingAvator'
import SettingAccount from '@pages/Setting/SettingAccount'
import NotFound from '@components/NotFound'
Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: {
        name: 'Home'
      }
    },
    {
      path: '/timeline',
      name: 'Home',
      component: CommentPage,
      meta: { 
        ifShow: true,
        requiresAuth: false
      }
    },
    {
      path: '/news',
      component: NewsHome,
      name: 'News',
      redirect: {name: 'NewList'},
      meta: {
        ifShow: true,
        requiresAuth: false
      },
      children: [
        {
          path: '/news/',
          name: 'NewsList',
          component: NewsPage,
          meta: {
            requiresAuth: false
          },
        },
        {
          path: '/news/:article_id',
          name: 'NewsArticle',
          meta: {
            requiresAuth: false
          },
          component: NewsArticle
        },
      ]
    },
    {
      path: '/commit',
      name: 'Commit',
      meta: { 
        ifShow: false,
        requiresAuth: false
      },
      children: [
        {
          path: '/commit/write',
          name: 'writeArticle',
          meta: { 
            requiresAuth: true
          },
        },
        {
          path: '/commit/history',
          name: 'historyArticle',
          meta: { 
            requiresAuth: true
          },
        },
        {
          path: '/commit/history',
          name: 'collectionArticle',
          meta: { 
            requiresAuth: true
          },
        },
      ]
    },
    {
      path: '/setting/:userId',
      name: 'setting',
      component: SettingPage,
      meta: { 
        requiresAuth: true
      },
      redirect: { name: 'info' },
      children: [
        {
          path: '/setting/:userId/info',
          name: 'info',
          meta: { 
            requiresAuth: true
          },
          component: SettingInfo
        },
        {
          path: '/setting/:userId/avator',
          name: 'avator',
          meta: { 
            requiresAuth: true
          },
          component: SettingAvator
        },
        {
          path: '/setting/:userId/account',
          name: 'info',
          meta: { 
            requiresAuth: true
          },
          component: SettingAccount
        },
        {
          path: '/setting/:userId/space',
          name: 'info',
          meta: { 
            requiresAuth: true
          },
          component: SettingInfo
        },
      ]
    },
    {
      path: '/space/:userId',
      name: 'Space',
      component: SpacePage,
      redirect: {
        name: 'index'
      },
      meta: {
        ifShow: false,
        requiresAuth: true
      },
      children: [
        {
          path: '/space/:userId/index',
          name: 'index',
          meta: { 
            requiresAuth: true
          },
          component: SpaceIndex,
        },
        {
          path: '/space/:userId/index/fan',
          name: 'fan',
          meta: { 
            requiresAuth: true
          },
          component: SpaceFan,
          children: [
            {
              path: '/space/:userId/index/fan/:tagID',
              meta: { 
                requiresAuth: true
              },
              name: 'follow_type',
            },
          ]
        },
        {
          path: '/space/:userId/collection',
          meta: { 
            requiresAuth: true
          },
          name: '我的收藏',
          component: SpaceCollection,
        },
        {
          path: '/space/:userId/history',
          name: '浏览记录',
          meta: { 
            requiresAuth: true
          },
          component: SpaceHistory
        },
        { 
          path: '/space/:userId/article',
          meta: { 
            requiresAuth: true
          },
          name: '我的文章',
          component: SpaceArticle
        },
      ]
    },
    {
      path: '/market',
      name: 'Market',
      component: MarketPage,
      meta: { 
        ifShow: true,
        requiresAuth: false
      }
    },
    {
      path: '/shop',
      name: 'Shop',
      component: HomePage,
      meta: { 
        ifShow: true,
        requiresAuth: false
      }
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})

function isLoggedIn() {
  let token = localStorage.getItem("jwt");
  if (token) {
    const payload = JSON.parse(window.atob(token.split(".")[1]));
    // 前端判断token是否过期，如果过期了访问时候会路由到login页面
    if (payload.exp > Date.now() / 1000) {
      return token;
    }
  } else {
    return false;
  }
}

router.beforeEach((to,from,next)=>{
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if(isLoggedIn()) {
      next()
    }else {
      next('/news')
    }
  }
  next()
})


export default router