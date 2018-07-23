<template>
  <div class="home">
    <div class="home__article">
      <article-list title="新闻资讯"></article-list>
      <article-list title="交流平台"></article-list>
    </div>
  </div>  
</template>

<script>
import ArticleList from '@components/ArticleList'
export default {
  data() {
    return {

    }
  },
  components: { ArticleList }
}
</script>

<style lang="scss">
  .home{
    padding-top: 3.5rem;
    &__article{
      @include tablet-min{
      display: flex;
      justify-content: space-between;
      }
    }
  }
</style>
