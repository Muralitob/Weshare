import Vue from "vue";
import Router from "vue-router";
import VueCookie from "vue-cookie";
import HomePage from "@pages/HomePage";
import NewsPage from "@pages/News/NewsPage";
import NewsHome from "@pages/News/NewsHome";
import NewsArticle from "@pages/News/NewsArticle";
import UsedPage from "@pages/Used/UsedPage";
import UsedHome from "@pages/Used/UsedHome";
import UsedDetail from '@pages/Used/UsedDetail'
import UsedRelease from '@pages/Used/UsedRelease.vue'
import CommentPage from "@pages/Comment/CommentPage";
import SpacePage from "@pages/SpacePage";
import SpaceIndex from "@pages/SpacePage/SpaceIndex";
import SpaceArticle from "@pages/SpacePage/SpaceArticle";
import SpaceCollection from "@pages/SpacePage/SpaceCollection";
import SpaceHistory from "@pages/SpacePage/SpaceHistory";
import SpaceFan from "@pages/SpacePage/SpaceFan";
import SettingPage from "@pages/Setting";
import SettingInfo from "@pages/Setting/SettingInfo";
import SettingAvator from "@pages/Setting/SettingAvator";
import SettingAccount from "@pages/Setting/SettingAccount";
import WriteArticle from "@pages/Commit/WriteArticle";
import Commit from "@pages/Commit";
import WeArticle from "@components/WeArticle.vue";
import CommentHome from "@pages/Comment/CommentHome.vue";
import NotFound from "@components/NotFound";
import { Message } from "iview";
import store from "../store/index";
import article from "../api/article";
import api from '../api';
Vue.use(Router);

const router = new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      meta: {
        requiresAuth: false
      }
    },
    {
      path: "/timeline",
      name: "Home",
      component: CommentHome,
      meta: {
        ifShow: true,
        requiresAuth: false
      },
      redirect: {
        name: 'commentPage'
      },
      children: [
        {
          path: "/timeline",
          name: "commentPage",
          component: CommentPage,
          meta: {
            requiresAuth: false
          }
        },
        {
          path: "/timeline/:com_id",
          name: "commentArticle",
          meta: {
            requiresAuth: false
          },
          component: WeArticle
        }
      ]
    },
    {
      path: "/news",
      component: NewsHome,
      name: "News",
      redirect: { name: "NewList" },
      meta: {
        ifShow: true,
        requiresAuth: false
      },
      children: [
        {
          path: "/news/",
          name: "NewsList",
          component: NewsPage,
          meta: {
            requiresAuth: false
          }
        },
        {
          path: "/news/:com_id",
          name: "NewsArticle",
          meta: {
            requiresAuth: false
          },
          component: WeArticle
        }
      ]
    },
    {
      path: "/commit",
      name: "Commit",
      meta: {
        ifShow: false,
        requiresAuth: false
      },
      component: Commit,
      children: [
        {
          path: "/commit/write",
          name: "writeArticle",
          meta: {
            requiresAuth: true
          },
          component: WriteArticle
        },
        {
          path: "/commit/history",
          name: "historyArticle",
          meta: {
            requiresAuth: true
          }
        },
        {
          path: "/commit/collection",
          name: "collectionArticle",
          meta: {
            requiresAuth: true
          }
        }
      ]
    },
    {
      path: "/setting/:userId",
      name: "setting",
      component: SettingPage,
      meta: {
        requiresAuth: true
      },
      redirect: { name: "info" },
      children: [
        {
          path: "/setting/:userId/info",
          name: "info",
          meta: {
            requiresAuth: true
          },
          component: SettingInfo
        },
        {
          path: "/setting/:userId/avator",
          name: "avator",
          meta: {
            requiresAuth: true
          },
          component: SettingAvator
        },
        {
          path: "/setting/:userId/account",
          name: "info",
          meta: {
            requiresAuth: true
          },
          component: SettingAccount
        },
        {
          path: "/setting/:userId/space",
          name: "info",
          meta: {
            requiresAuth: true
          },
          component: SettingInfo
        }
      ]
    },
    {
      path: "/space/:userId",
      name: "Space",
      component: SpacePage,
      redirect: {
        name: "index"
      },
      meta: {
        ifShow: false,
        requiresAuth: true
      },
      children: [
        {
          path: "/space/:userId/index",
          name: "index",
          meta: {
            requiresAuth: true
          },
          component: SpaceIndex
        },
        {
          path: "/space/:userId/index/fan",
          name: "fan",
          meta: {
            requiresAuth: true
          },
          redirect: {
            path: "/space/:userId/index/fan/00"
          },
          component: SpaceFan,
          children: [
            {
              path: "/space/:userId/index/fan/:tagID",
              meta: {
                requiresAuth: true
              },
              name: "follow_type"
            }
          ]
        },
        {
          path: "/space/:userId/index/fans",
          meta: {
            requiresAuth: true
          },
          component: SpaceFan
        },
        {
          path: "/space/:userId/collection",
          name: "myCollection",
          meta: {
            requiresAuth: true
          },
          component: SpaceCollection
        },
        {
          path: "/space/:userId/history",
          name: "浏览记录",
          meta: {
            requiresAuth: true
          },
          component: SpaceHistory
        },
        {
          path: "/space/:userId/article",
          meta: {
            requiresAuth: true
          },
          name: "我的文章",
          component: SpaceArticle
        }
      ]
    },
    {
      path: "/used",
      name: "Market",
      component: UsedPage,
      meta: {
        ifShow: true,
        requiresAuth: false
      },
      children: [
        {
          path: "/used/",
          name: "UsedHome",
          meta: {
            requiresAuth: false
          },
          component: UsedHome
        },
        {
          path: "/used/release",
          name: "UsedRelease",
          meta: {
            requiresAuth: true
          },
          component: UsedRelease
        },
        {
          path: "/used/:used_id",
          name: "UsedDetail",
          meta: {
            requiresAuth: false
          },
          component: UsedDetail
        },
      ]
    },
    {
      path: "/shop",
      name: "Shop",
      component: HomePage,
      meta: {
        ifShow: true,
        requiresAuth: false
      }
    },
    {
      path: "*",
      component: NotFound
    }
  ]
});

router.beforeEach((to, from, next) => {
  let token = store.state.UserSetting.token;
  const uid = VueCookie.get("uid");
  if(to.params.com_id) {
    //说明访问了文章
    // console.log(to.params.com_id);
    api.historyFunction('post',to.params.com_id).then(({data})=> {
      console.log(data)
    })
  }
  if(to.path === '/') {
    next('/timeline')
  }
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (token) {
      if (!uid) {
        store.dispatch("PromptReLogin");
        next("/");
      } else {
        next();
      }
    } else {
      next("/");
    }
  } else {
    next();
  }
});

export default router;
