<template>
  <div class="commetion">
    <div class="commetion__wrapper">
      <div class="cutarea">
        <router-link to="/commit/write" class="user__Write shortcut"><Icon size="38" type="ios-create-outline" />写文章</router-link>
        <router-link :to="{name: 'Space', params: {userId: uid}}" class="user__History shortcut"><Icon size="38" type="md-globe" />浏览历史</router-link>
        <router-link :to="{name: 'myCollection', params: {userId: uid}}" class="user__Collection shortcut"><Icon size="38" type="ios-star" />我的收藏</router-link>
        <span class="shortcut" @click="showSearch"><Icon size="38" type="md-search" />搜索</span>
      </div>
      <ul class="a_list">
        <li class="a_item">
          <article>
            <div class="a_con">
              <div class="a_tags"> 
                  <Tag type="border">标签三</Tag>
              </div>
              <router-link to="">
                <h3 class="a_title">置顶公告,发帖必须看！</h3>
              </router-link>
            </div>
          </article>
        </li>
        <li class="a_item" v-for="item in articles" :key="item._idx">
          <article>
            <header>
              <div class="a_watch"><Icon type="md-eye" />{{item.watchNum}}</div>
              <router-link to="">
                <h3 class="a_title">{{item.title}}</h3>
              </router-link>
            </header>
            <div class="a_con">
              <div class="a_tags"> 
                <Tag type="border">标签三</Tag>
                <Tag type="border">标签三</Tag>
              </div>
              <div class="a_text" v-html="item.summary"></div>
            </div>
            <footer>
                <span class="a_author"><Icon type="md-person" />{{item.author}}</span>
                <span class="a_time"><Icon type="md-time" />{{item.time}}</span>
            </footer>
          </article>
          </li>
      </ul>
      <Page prev-text="上一页" next-text="下一页" @on-change="changepage" :total="40" show-elevator class-name="timeline-pageBox"></Page>
    </div>
  </div>  
</template>

<script>
import NaviBar from "../../components/Navi";
import api from "../../api";
export default {
  components: { NaviBar },
  data() {
    return {
      user_info: {
        userID: "01",
        avator_URL: "../../assets/avator.jpeg",
        name: "稳健如poi",
        beLiked: "1.2K",
        beWatched: "3K",
        points: 3000
      },
      articles: [
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        },
        {
          tags: [],
          _id: "111222333",
          title: "今日分享：我想分享些什么呢？今天的天气很好，这就是标题吧！",
          summary:
            "这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......这里可以放一些内容的摘要，大概可以放两行字，具体有什么我也不知道。要放多长呢？大概这样 就可以了，不然可能会太长了，你说对吧。14px;多出来的内容......",
          time: "30分钟前",
          author: "Mura",
          watchNum: "30K"
        }
      ],
      uid: this.$cookie.get("uid"),
      token: this.$store.state.UserSetting.token
    };
  },
  watch: {},
  computed: {
    IsLogin() {
      return this.$store.state.UserSetting.token && this.$cookie.get("uid");
    }
  },
  updated() {
    // api.getUserInfo(this.$store.state.UserSetting.uid)
  },
  mounted() {
    if (this.$store.state.token) {
      api.getUserInfo(this.$cookie.get("uid")).then(({ data }) => {
        console.log(data);
      });
    }
  },
  methods: {
    changepage(index) {
      console.log(index);
    },
    showSearch() {}
  }
};
</script>

<style lang="scss">
.exp {
  display: flex;
  div {
    font-size: 14px;
  }
}
.cutarea {
  display: flex;
  width: 100%;
  background-color: #fff;
  height: 70px;
  margin-bottom: 50px;
  border-radius: 3px;
  justify-content: space-around;
  .shortcut {
    line-height: 70px;
    display: flex;
    align-items: center;
    i {
      margin-right: 1rem;
    }
    + span {
      font-size: 16px;
      cursor: pointer;
      &:hover {
        color: $c-green;
      }
    }
  }
}
.user {
  @include tablet-min {
    &-like,
    &-watch {
      font-size: 14px;
      display: block;
    }
    &-wrapper {
      margin-left: 1.25rem;
    }
    &-name {
      a {
        font-size: 14px;
      }
    }
  }
}
#user-info {
  @include tablet-min {
    display: flex;
    height: 5rem;
    .head_img {
      width: 5rem;
    }
  }
}
.commetion {
  width: 100%;
  &__wrapper {
    @include tablet-min {
      display: flex;
      flex-direction: column;
    }
  }
  .a {
    &_list {
      background-color: $c-white;
      width: 100%;
      min-height: 60rem;
    }
    &_item {
      padding: 20px;
      border-bottom: 1px solid #eeeeee;
      color: #000;
      &:not(:first-child):hover {
        background-color: #fbfbfb;
      }
      &:last-child {
        border: none;
      }
      header {
        // display: flex;
        height: 30px;
      }
      footer {
        margin-left: 6rem;
        display: flex;
        span {
          font-size: 14px;
          display: flex;
          align-items: center;
        }
      }
    }
    &_watch {
      float: left;
      line-height: 30px;
      i {
        margin-right: 10px;
        margin-top: -2px;
      }
    }
    &_title {
      margin-left: 6rem;
      line-height: 30px;
      font-size: 16px;
      font-family: MicrosoftYaHei-Bold;
      font-weight: bold;
      color: rgba(0, 0, 0, 1);
    }
    &_con {
      position: relative;
      margin: 1.5rem 0 1rem 0;
      display: flex;
    }
    &_text {
      font-size: 16px;
      margin-left: 6rem;
      width: 80%;
    }
    &_tags {
      position: absolute;
      left: 20px;
      display: flex;
      flex-direction: column;
    }
    &_author {
    }
    &_time {
      margin-left: 2rem;
      font-size: 14px;
    }
  }
  &__me {
    @include mobile-only {
      display: none;
    }
    @include tablet-min {
      width: 17.5rem;
      height: 30rem;
      background-color: $c-white;
      padding: 10px 10px;
      &-region {
        margin-bottom: 20px;
        font-size: 15px;
        font-weight: 700;
        font-family: "microsoft yahei", simhei, sans-serif;
      }
    }
    &--info {
    }
  }
  .timeline-pageBox {
    background-color: #fff;
    padding: 20px 0 20px 20px;
  }
}
</style>
