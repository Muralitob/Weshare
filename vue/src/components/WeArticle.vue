<template>
  <div class="article">
    <Affix class="left_bar" :offset-top="100">
      <ButtonGroup vertical>
        <Button @click="colArticle(1)" v-if="!article_data.is_collection" icon="md-star"></Button> 
        <Button @click="colArticle(-1)" v-else icon="md-star" class="col_btn_active"></Button>
        <Button @click="likeArticle(1)" v-if="!article_data.is_like" icon="md-thumbs-up"></Button>
        <Button @click="likeArticle(-1)" v-else icon="md-thumbs-up" class="like_btn_active"></Button>
        <Button icon="logo-facebook"></Button>
        <Button icon="logo-twitter"></Button>
        <Button icon="logo-googleplus"></Button>
        <Button icon="logo-tumblr"></Button>
      </ButtonGroup>
    </Affix>
    <div>
      <div class="article__content" >
        <div class="wrap">
          <div class="article__title">{{article_content.title}}</div>
          <div class="reback" @click="returnLast">
            <Icon type="arrow-return-left" size=35 color="#01d277"></Icon>
          </div>
        </div>
        <p class="article__artinfo borline">
          <router-link :to="{name:'Space', params: {userId: article_content.uid}}">
            <span class="article__author">{{article_content.nickname}}</span>
          </router-link>
          {{article_data.update_time}}
        </p>
        <section class="article__main" v-html="article_content.content"></section>
        <!-- <Card style="width:80px">
          <div style="text-align:center">
              <span>喜欢</span>
          </div>
        </Card> -->
      </div>
      <div class="art">
        <art-com :a_id="article_data._id" :list="article_data.reply || []"></art-com>
      </div>
      <Spin size="large" fix v-if="spinShow"></Spin>
    </div>
    <Card dis-hover :bordered="false">
      <p slot="title">本周最热</p>
      <div class="hot-item">
        <router-link to="/">
          <span>23333333</span>
        </router-link>
        <Time :time="time2" type="date" />
      </div>
    </Card>
  </div>  
</template>

<script>
import ArtCom from "./ArtCom";
import api from "../api";
export default {
  components: { ArtCom },
  data() {
    return {
      article_content: {},
      article_data: {},
      com_id: this.$route.params["com_id"],
      spinShow: false,
      time2: new Date().getTime() - 86400 * 3 * 1000
    };
  },
  methods: {
    returnLast() {
      this.$router.go(-1);
    },
    async fetchData() {
      this.spinShow = true;
      try {
        let { data } = await api.getArticleById(this.com_id);
        this.article_content = data.articles.article;
        console.log("当前文章信息", data.articles);
        this.article_data = data.articles;
        this.spinShow = false;
      } catch (error) {
        console.log(error);
      }
    },
    async readArticle() {
      let { data } = await api.countArticle(this.com_id);
    },
    async colArticle(add) {
      if (add === 1) {
        //收藏
        let { data } = await api.collectionFun("post", this.com_id);
        this.article_data.is_collection = true;
      } else {
        //取消收藏
        let { data } = await api.collectionFun("delete", this.com_id);
        this.article_data.is_collection = false;
      }
    },
    likeArticle(add) {
      if (add === 1) {
        this.article_data.is_like = true;
      } else {
        this.article_data.is_like = false;
      }
      api.addLikeArticle(add, this.com_id);
    }
  },
  mounted() {
    this.fetchData();
    this.readArticle();
  }
};
</script>

<style lang="scss">
.article {
  border-radius: 3px;
  position: relative;
  .left_bar {
    position: absolute;
    left: -3.5rem;
    width: 36px;
    .ivu-btn-group .ivu-btn-icon-only .ivu-icon {
      font-size: 18px;
    }
    .col_btn_active {
      i {
        color: $c-col;
      }
    }
    .like_btn_active {
      i {
        color: $c-green;
      }
    }
  }
  &__content {
    @include tablet-min {
      background-color: $c-white;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid #e1e1e1;
      width: 56.25rem;
      min-width: 40rem;
      padding: 1.5625rem;
      margin-bottom: 10px;
    }
    .wrap {
      display: flex;
      justify-content: space-between;
      .reback {
        display: flex;
        align-items: center;
        margin-right: 1.5rem;
        transition: all 0.1s linear;
        &:hover {
          transform: scale(1.05);
        }
        i {
          cursor: pointer;
        }
      }
    }
  }
  &__main {
    padding: 30px 0 50px;
    font-size: 15px;
    overflow: hidden;
    color: #333;
  }
  &__title {
    font-size: 22px;
    line-height: 50px;
    color: $c-deepgreen;
    font-weight: normal;
  }
  &__artinfo {
    color: $c-info;
    font-size: 12px;
    padding-bottom: 5px;
  }
  &__author {
    color: $c-gray;
    font-size: 12px;
  }
  section {
    min-height: 380px;
  }
  .ivu-card {
    width: 280px;
    position: absolute;
    right: 0;
    top: 0;
  }
  .hot-item {
    display: flex;
    justify-content: space-between;
    a {
      span {
        font-size: 16px;
      }
    }
  }
}
.art {
  width: 56.25rem;
}
</style>
