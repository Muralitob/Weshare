<template>
  <div class="article">
    <div>
      <Affix v-if="!ifnews" class="left_bar" :offset-top="100">
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
        </div>
        <div class="art">
          <art-com :a_id="article_data._id" :list="article_data.reply || []"></art-com>
        </div>
        <Spin size="large" fix v-if="spinShow"></Spin>
      </div>
    </div>
    <!-- <Card class="ri" dis-hover :bordered="false">
      <p slot="title">本周最热</p>
      <div class="hot-item" v-for="(item, index) in hot" :key="index">
        <router-link :to="{path: `/timeline/${item._id}`}">
          <span>{{item.article.title}}11</span>
        </router-link>
        <span>{{item.article.nickname}}</span>
      </div>
    </Card> -->
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
      time2: new Date().getTime() - 86400 * 3 * 1000,
      hot: [],
      ifnews: false
    };
  },
  methods: {
    returnLast() {
      this.$router.go(-1);
    },
    async fetchData() {
      this.spinShow = true;
      try {
        if(this.$route.name == 'NewsArticle') {
          console.log('新闻')
          let { data } = await api.getNewsById(this.com_id);
          console.log(data);
          this.article_content = data.new.article;
          this.article_data = data.new;
          this.spinShow = false;
        }else {
          console.log('文章')
          let { data } = await api.getArticleById(this.com_id);
          this.article_content = data.articles.article;
          this.article_data = data.articles;
          this.spinShow = false;
        }
      } catch (error) {
        // console.log(error);
      }
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
    },
    async getHot() {
      try {
        let {data} = await api.getHotArticles()
        this.hot = data.articles
      } catch (error) {

      }
    }
  },
  mounted() {
    this.fetchData();
    this.getHot()
    this.$route.name == 'NewsArticle'? this.ifnews = true: this.ifnews = false
  }
};
</script>

<style lang="scss">
.article {
  border-radius: 3px;
  width: 100%;
  position: relative;
  display: flex;
  justify-content: space-between;
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
  .hot-item {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding: 10px;
    border-bottom: 1px solid #ccc;
    a {
      span {
        width: 150px;
        display: inline-block;
        font-size: 14px;
        overflow: hidden;
        -webkit-line-clamp: 2;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-box-orient: vertical;
      }
    }
  }
}
.ivu-card {
  // float: right;
  // margin-left: 120px;
  // position: absolute;
  // right: 0;
  max-height: 45rem;
}
.art {
  width: 56.25rem;
}
</style>
