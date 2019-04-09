<template>
  <div class="news">
    <router-view></router-view>
    <Card class="ri" dis-hover :bordered="false">
      <p slot="title">本周最热</p>
      <div class="hot-item" v-for="(item, index) in hot" :key="index">
        <router-link :to="{path: `/timeline/${item._id}`}">
          <span>{{item.article.title}}11</span>
        </router-link>
        <span>{{item.article.nickname}}</span>
      </div>
    </Card>
  </div>
</template>

<script>
import api from '../../api'
export default {
  data() {
    return {
      time2: (new Date()).getTime() - 86400 * 3 * 1000,
      hot: []
    }
  },
  methods: {
    async getHot() {
      try {
        let {data} = await api.getHotArticles()
        this.hot = data.articles
      } catch (error) {

      }
    }
  },
  created() {
    this.getHot()
  }
}
</script>

<style lang="scss" >
  .news{
    display: flex;
    justify-content: space-between;
    &__subside{
      @include mobile-only{
        display: none;
      }
      width: 280px;
      // height: 500px;
      // background-color: $c-green;
      .ivu-card {
        margin-bottom: 36px;
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
  .ri {
    min-width: 262px;
  }
</style>

