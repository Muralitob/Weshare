<template>
  <div class="article__article">
    <div class="article__content" >
      <div class="wrap">
        <div class="article__title">{{article_content.title}}</div>
        <div class="reback" @click="returnLast">
          <Icon type="arrow-return-left" size=35 color="#01d277"></Icon>
        </div>
      </div>
      <p class="article__artinfo borline">
        <span class="article__author">{{article_data.author||'mura'}}</span>
        {{article_data.update_time}}
      </p>
      <section class="article__main" v-html="article_content.content"></section>
    </div>
    <div class="art">
      <art-com :a_id="article_data._id" :list="article_data.reply || []"></art-com>
    </div>
  </div>  
</template>

<script>
import ArtCom from './ArtCom';
import api from '../api';
export default {
  components: { ArtCom },
  data(){
    return {
      article_content: {},
      article_data: {},
    }
  },
  methods: {
    returnLast() {
      this.$router.go(-1)
    },
    async fetchData() {
      let _id = this.$route.params['com_id']
      try {
        let { data } = await api.getArticleById(_id)
        this.article_content = data.articles.article
        console.log(data)
        this.article_data = data.articles
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.fetchData()
  }
}
</script>

<style lang="scss">
  .article{
    &__content{
      @include tablet-min{
        background-color: $c-white;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        border: 1px solid #E1E1E1;
        width: 56.25rem;
        min-width: 40rem;
        padding: 1.5625rem;
        margin-bottom: 10px;
      }
      .wrap{
        display: flex;
        justify-content: space-between;
        .reback {
          display: flex;
          align-items: center;
          margin-right: 1.5rem;
          transition: all .1s linear;
          &:hover{
            transform: scale(1.05);
          }
          i{
            cursor: pointer;
          }
        }
      }
    }
    &__main{
      padding: 30px 0 50px;
      font-size: 15px;
      overflow: hidden;
      color: #333;
    }
    &__title{
      font-size: 22px;
      line-height: 50px;
      color: $c-deepgreen;
      font-weight: normal;
    }
    &__artinfo{
      color: $c-info;
      font-size: 12px;
      padding-bottom: 5px;
    }
    &__author{
      color: $c-gray;
      font-size: 12px;
    }
    section {
      min-height: 380px;
    }
  }
  .art {
    width: 56.25rem;
  }
</style>
