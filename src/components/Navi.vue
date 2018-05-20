// 导航
<template>
  <div class="navi">
    <router-link to= "/" exact>首页</router-link>
    <span>{{this.$route.name}}</span>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
@import '../scss/variable.scss';
@import '../scss/media-queries.scss';
.navi{
  padding: 20px 0;
  span{
    color: #666;
    font-size: 14px;
  }
}
</style>
