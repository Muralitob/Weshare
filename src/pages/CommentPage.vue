<template>
  <div class="commetion">
    <navi-bar></navi-bar>
    <div class="commetion__wrapper">
      <div class="commetion__list">

      </div>
      <div class="commetion__me">
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
          <div class="user__Write shortcut ">
            <router-link to="/commit/write">写文章</router-link>
          </div>
          <div class="user__History shortcut">
            <router-link to="/commit/history">浏览历史</router-link>
          </div>
          <div class="user__Collection shortcut">
            <router-link to="/commit/collection">我的收藏</router-link>
          </div>
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
    width: 100%;
    height: 3.75rem;
    text-align: center;
    line-height: 3.75rem;
    a{
      
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
      }
      &--info{

      }
    }
  }
</style>
