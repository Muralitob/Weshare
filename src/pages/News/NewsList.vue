<template>
  <div class="news__article">
    <navi-bar :title="news__content.title"></navi-bar>
      <div class="news__content">
        <h2 class="news__title">{{news__content.title}}</h2>
        <p class="news__artinfo borline">
          <span class="news__author">{{news__content.author}}</span>
          {{news__content.created_at}}
        </p>
        <section class="news__main" v-html="news__content.content"></section>
      </div>
  </div>  
</template>

<script>
import NaviBar from '../../components/Navi'
export default {
  components: { NaviBar },
  data(){
    return {
      news__content: {
        title: '微分享重磅登场......',
        author: 'weshare运营团队',
        created_at: '2018-04-12 10:10:19',
        content: `终于OK了`
      }
    }
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
        box-shadow: 0 0 2px rgba(0,0,0,.2);
        width: 56.25rem;
        min-width: 40rem;
        padding: 1.5625rem;
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
  }
</style>
