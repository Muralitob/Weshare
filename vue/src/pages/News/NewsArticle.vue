<template>
  <div class="news__article">
    <div class="news__content" v-for="item in news_content" :key="item.id" >
      <div class="wrap">
        <div class="news__title">{{item.title}}</div>
        <div class="reback" @click="returnLast">
          <Icon type="arrow-return-left" size=35 color="#01d277"></Icon>
        </div>
      </div>
      <p class="news__artinfo borline">
        <span class="news__author">{{item.author}}</span>
        {{item.created_at}}
      </p>
      <section class="news__main" v-html="item.content"></section>
    </div>
    <div class="art">
      <art-com></art-com>
    </div>
  </div>  
</template>

<script>
import ArtCom from '../../components/ArtCom';
export default {
  components: { ArtCom },
  data(){
    return {
      news_content: [
        {
        id: '01',
        title: '微分享重磅登场......',
        author: 'weshare运营团队',
        created_at: '2018-04-12 10:10:19',
        content: `终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了终于OK了`
        },
      ]
    }
  },
  methods: {
    returnLast() {
      this.$router.go(-1)
    }
  },
  mounted () {
    console.log(this.$route)
  }
}
</script>

<style lang="scss">
  .news{
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
    .art {
      width: 56.25rem;
    }
  }
</style>
