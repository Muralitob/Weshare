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
import SpaceFollow from '@pages/SpacePage/SpaceFollow'
import SpaceFans from '@pages/SpacePage/SpaceFans'
import NotFound from '@components/NotFound'
Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/timeline',
      name: 'Home',
      component: CommentPage,
      meta: { 
        ifShow: true
      }
    },
    {
      path: '/news',
      component: NewsHome,
      name: 'News',
      redirect: {name: 'NewList'},
      meta: {
        ifShow: true
      },
      children: [
        {
          path: '/news/',
          name: 'NewsList',
          component: NewsPage,
        },
        {
          path: '/news/:article_id',
          name: 'NewsArticle',
          component: NewsArticle
        },
      ]
    },
    {
      path: '/commit',
      name: 'Commit',
      meta: { 
        ifShow: false
      },
      children: [
        {
          path: '/commit/write',
          name: 'writeArticle',
        },
        {
          path: '/commit/history',
          name: 'historyArticle',
        },
        {
          path: '/commit/history',
          name: 'collectionArticle',
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
        ifShow: false
      },
      children: [
        {
          path: '/space/:userId/index',
          name: 'index',
          component: SpaceIndex,
        },
        {
          path: '/space/:userId/index/fan',
          name: 'fan',
          component: SpaceFan,
          children: [
            {
              path: '/space/:userId/index/fan/follow',
              name: 'follow',
              component: SpaceFollow
            },
            {
              path: '/space/:userId/index/fan/fans',
              name: 'fans',
              component: SpaceFans
            }
          ]
        },
        {
          path: '/space/:userId/collection',
          name: '我的收藏',
          component: SpaceCollection,
        },
        {
          path: '/space/:userId/history',
          name: '浏览记录',
          component: SpaceHistory
        },
        {
          path: '/space/:userId/article',
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
        ifShow: true
      }
    },
    {
      path: '/shop',
      name: 'Shop',
      component: HomePage,
      meta: { 
        ifShow: true
      }
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})

router.beforeEach((to,from,next)=>{
  if(to.path==='/') {
    next('/timeline')
  }
  next()
})


export default router