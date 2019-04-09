<template>
  <div class="newsp">
    <!-- <navi-bar ></navi-bar> -->
    <div class="newsp__list">
      <ul class="newsp__list-box">
        <li class="newsp__list-item"
        v-for=" (item, index) in news"
        :key="index">
          <p>
            <router-link :to="{path: `/news/${item._id}`}">[{{item.origin}}]</router-link>
            <router-link :to="{path: `/news/${item._id}`}">{{item.article.summary}}</router-link>
          </p>
          <Time :time="item.update_time" />
        </li>
      </ul>
      <Page prev-text="上一页" next-text="下一页" :current="parseInt(currentPage)" @on-change="changepage" :total="total" show-elevator class-name="newsp-pageBox"></Page>
    </div>
  </div>
</template>

<script>
import api from '../../api'
export default {
  data () {
    return {
      news: [
      ],
      total: 100,
      currentPage: 1
    }
  },
  methods: {
    getData() {
      api.getNewsList().then(({data}) => {
        this.news = data.news
        this.total = data.total
      }).catch((err) => {

      });
    },
    changepage() {

    }
  },
  created() {
    this.getData()
  }
}
</script>

<style lang="scss">
.newsp{
  .newsp-pageBox {
    padding: 20px;
  }
  display: flex;
  flex-direction: column;
  &__list{
    @include tablet-min{
      background-color: $c-white;
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid #E1E1E1;
      box-shadow: 0 0 2px rgba(0,0,0,.2);
      width: 56.25rem;
      min-width: 40rem;
      min-height: 50rem;
    }
    &-box{
      @include tablet-min{
        padding: 30px 0 30px;
      }
    }
    &-item{
      display: block;
      position: relative;
      font-size: 14px;
      border-left: 4px solid #fff;
      margin-bottom: 6px;
      &:hover{
        border-left: 4px solid $c-green;
        a{
          color: $c-green;
        }
      }
      p{
        width: 92%;
        height: 37px;
        line-height: 37px;
        margin: 0 auto;
        border-bottom: 1px dashed #BFBFBF;
      }
      span{
        position: absolute;
        top: 0;
        right: 4%;
        line-height: 37px;
        color: $c-gray;
        font-size: 12px;
      }
    }
    &-page{
      text-align: center;
      margin: 20px 20px;
      button{
        width: 60px;
        height: 30px;
        line-height: 30px;
        text-align: center;
        display: inline-block;
        border: 1px solid #CECECE;
        font-size: 14px;
        color: $c-gray;
        font-weight: normal;
        border-radius: 4px;
        cursor: pointer;
        &:hover{
          background-color: #03c36f;
          color: $c-white;
        }
      }
    }
  }
}
</style>
