<template>
  <div class="news">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      time2: (new Date()).getTime() - 86400 * 3 * 1000
    }
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
</style>

