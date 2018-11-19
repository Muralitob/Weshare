<template>
  <div class="news">
    <router-view></router-view> 
    <div class="news__subside">
      <Card :bordered="false">
        <p slot="title">本周最热</p>
        <div class="hot-item">
          <router-link to="/">
            <span>23333333</span>
          </router-link>
          <Time :time="time2" type="date" />
        </div>
      </Card>
      <Card :bordered="false">
          <p slot="title">本周推荐学生创业团队</p>
          <p>团队名称: <span>wwww</span> </p>
          <p>主营项目: <span>校园外卖</span></p>
          <p>联系方式: <span>110</span></p>
      </Card>
    </div> 
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

