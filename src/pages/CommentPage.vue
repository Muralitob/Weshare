<template>
  <div class="commetion">
    <navi-bar></navi-bar>
    <div class="commetion__wrapper">
      <div class="commetion__list">
      </div>
      <div class="commetion__me">
        <h4 class="commetion__me-region">我的信息</h4>
        <div id="user-info">
          <router-link to="/myinfo/01">
            <img src="../assets/avator.jpeg" class="head_img">
          </router-link>
          <div class="user-wrapper">
            <div class="user-name">
              <router-link to="/myinfo/01">{{user_info.name}}</router-link>
            </div>
            <span class="user-like">获得喜欢：{{user_info.beLiked}}次</span>
            <span class="user-watch">文章被阅读：{{user_info.beWatched}}次</span>
            <div class="exp">
              <div class="exp__tablet">积分：</div>
              <div class="exp__tablet-current">{{user_info.points}}</div>
            </div>
          </div>
        </div>
        <div class="user__cutarea">
          <router-link to="/commit/write" class="user__Write shortcut">写文章</router-link>
          <router-link to="/commit/history" class="user__History shortcut">浏览历史</router-link>
          <router-link to="/commit/collection" class="user__Collection shortcut">我的收藏</router-link>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
import NaviBar from '../components/Navi'
export default {
  components: { NaviBar },
  data () {
    return {
      user_info:{
        imgurl: '../assets/avator.jpeg',
        name: '稳健如poi',
        beLiked: '1.2K',
        beWatched: '3K',
        points: 3000,
      }
    }
  }
}
</script>

<style lang="scss">
  .shortcut{
    flex: 0 0 50%;
    height: 3.75rem;
    text-align: center;
    line-height: 3.75rem;
    box-sizing: border-box;
    &:nth-child(1),&:nth-child(2),&:nth-child(3){
      border-bottom: 1px solid rgba($c-gray, .5);
      border-right: 1px solid rgba($c-gray, .5);
    }
  }
  .exp{
    display: flex;
    div{
      font-size: 14px;
    }
  }
  .user{
    @include tablet-min{
      &-like,&-watch{
      font-size: 14px;
      display: block;
      }
      &-wrapper{
        margin-left: 1.25rem;
      }
      &-name{
        a{
          font-size: 14px;
        }
      }
      &__cutarea{
        margin-top: 1.25rem;
        display: flex;
        flex-flow: row wrap;
        border: 1px solid rgba($c-gray, .5);
        border-right: none;
        border-bottom: none;
        border-radius: 3px;
        a{
          color: rgba($c-dark,.8);
          &:hover{
            background-color: rgba($c-gray,.3);
          }
        }
      }
    }
  }
  #user-info{
    @include tablet-min{
      display: flex;
      height: 5rem;
      .head_img{
        width: 5rem;
      }
    }
  }
  .commetion{
    width: 100%;
    &__wrapper{
      @include tablet-min{
        display: flex;
        justify-content: space-between;
      }
    }
    &__list{
      @include tablet-min{
        background-color: $c-white;
        width: 60rem;
        height: 60rem;
      }
    }
    &__me{
      @include mobile-only{
        display: none;
      }
      @include tablet-min{
        width: 17.5rem;
        height: 30rem;
        background-color: $c-white;
        padding: 10px 10px;
        &-region{
          margin-bottom: 20px;
          font-size: 15px;
          font-weight: 700;
          font-family: "microsoft yahei",simhei,sans-serif;
        }
      }
      &--info{

      }
    }
  }
</style>
