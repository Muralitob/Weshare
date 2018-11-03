<template>
  <div class="commetion">
    <div class="commetion__wrapper" >
      <div class="cutarea" v-if="IsLogin">
        <section class="cutarea_bar" v-if="!searhIf">
          <router-link to="/commit/write" class="user__Write shortcut"><Icon size="38" type="ios-create-outline" />写文章</router-link>
          <router-link :to="{name: 'Space', params: {userId: uid}}" class="user__History shortcut"><Icon size="38" type="md-globe" />浏览历史</router-link>
          <router-link :to="{name: 'myCollection', params: {userId: uid}}" class="user__Collection shortcut"><Icon size="38" type="ios-star" />我的收藏</router-link>
          <span class="shortcut" @click="showSearch"><Icon size="38" type="md-search" />搜索</span>
        </section>
        <section id="search" ref="ss" v-if="searhIf">
          <Input element-id="search-form" @on-blur="searhIf= false" autofocus="autofocus" size="large"  search placeholder="在这里搜索吧~" />
        </section>
      </div>
      <ul class="a_list">
        <li class="a_item">
          <article>
            <div class="a_con">
              <div class="a_tags"> 
                  <Tag color="red">公告</Tag>
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
              <router-link :to="{path: `/timeline/${item._id}`}">
                <h3 class="a_title">{{item.title}}</h3>
              </router-link>
            </header>
            <div class="a_con">
              <div class="a_tags">
                <Tag v-if="item.tagLists.length >= 1" color="green" v-for="t in item.tagLists" :key="t" :name="t" >{{t}}</Tag>
                <Tag  v-if="!item.tagLists.length" color="cyan">日常</Tag>
              </div>
              <div class="a_text" v-html="item.summary"></div>
            </div>
            <footer>
                <span class="a_author"><Icon type="md-person" />{{item.nickname}}</span>
                <span class="a_time"><Icon type="md-time" />
                <Time :time="item.time" />
                </span>
            </footer>
          </article>
          </li>
          <Spin size="large" fix v-if="spinShow"></Spin>
      </ul>
      <Page prev-text="上一页" next-text="下一页" :current="parseInt(currentPage)" @on-change="changepage" :total="total" show-elevator class-name="timeline-pageBox"></Page>
    </div>
  </div>  
</template>

<script>
import NaviBar from "../../components/Navi";
import api from "../../api";
import general from "../../general/js";
import article from "../../api/article";
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
      total: 0,
      page: 1,
      articles: [],
      result: [],
      spinShow: false,
      uid: this.$cookie.get("uid"),
      token: this.$store.state.UserSetting.token,
      searhIf: false,
      currentPage: this.$route.query.page || 1
    };
  },
  watch: {},
  computed: {
    IsLogin() {
      return this.$store.state.UserSetting.token;
    }
  },
  updated() {},
  mounted() {
    this.fetchResult(this.currentPage);
  },
  methods: {
    changepage(index) {
      this.currentPage = index;
      this.fetchResult(this.currentPage);
    },
    showSearch() {
      this.searhIf = !this.searhIf;
      this.$nextTick(() => {
        document.getElementById("search-form").focus();
      });
    },
    async fetchResult(page) {
      this.$router.push({ path: "/timeline", query: { page } });
      this.spinShow = true;
      try {
        let { data } = await api.getAllArticles(page);
        this.articles = data.result;
        let obj = {};
        this.articles = Object.values(data)[0].map(value => ({
          time: value.update_time,
          title: value.article.title || "233",
          summary: value.article.summary || "233",
          _id: value._id,
          author: value.author || "Mura",
          watchNum: general.ToThousand(value.read_num) || 0,
          tagLists: value.tagLists,
          nickname: value.article.nickname,
        }));
        this.total = data.total;
        this.spinShow = false;
        console.log("data", data);
      } catch (err) {
        console.log("err", err);
      }
    }
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
  align-items: center;
  position: relative;
  .cutarea_bar {
    display: flex;
    width: 100%;
    justify-content: space-around;
  }
  #search-form {
    // position: absolute;
    // right: 20px;
    transition: width 0.25s ease;
    // i {
    //   position: absolute;
    //   right: 0;
    // }
  }
  #search {
    position: absolute;
    right: 20px;
  }
  #search-form:focus-within {
    width: 1100px;
    // width: 77%;
  }
  input {
    width: 200px;
    height: 40px;
  }
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
      position: relative;
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
