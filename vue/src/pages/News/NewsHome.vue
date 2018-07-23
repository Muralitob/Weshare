<template>
  <div class="news">
    <router-view></router-view> 
    <div class="news__subside">广告或者其他</div> 
  </div>
</template>

<script>
export default {
  
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
      height: 500px;
      background-color: $c-green;
    }
  }
</style>

