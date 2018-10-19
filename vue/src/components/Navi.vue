// 导航
<template>
  <div class="navi">
    <!-- <router-link to= "/" exact>首页</router-link> -->
    <router-link to= "/news" class="navi-fu" v-if="title" exact>{{preRouteName}}</router-link>
    <!-- <span class="navi-fu" v-if="!title">{{currentRouteName}}</span> -->
    <span v-if="title" class="navi-title">{{title}}</span>
  </div>
</template>

<script>
import general from '../general/js';
export default {
  data() {
    return {
      preRouteName : general.translate(this.$route.name)
    }
  },
  props: [ 'title' ],
  created() {
    // console.log(this.$route);
  }
}
</script>

<style lang="scss">
.navi{
  padding: 20px 0;
  span{
    color: #666;
  }
  &-fu{
    font-size: 14px;
  }
  &-title{
    font-size: 16px;
  }
}
</style>
