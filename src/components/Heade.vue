<template>
  <header>
    <div class="top">
      <ul class="top__user">
        <li><router-link to="/login">登录</router-link></li>
        <li><router-link to="/regist">注册</router-link></li>
      </ul>
      <div class="top__hamburger" @click="toggleNav">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div>
      <router-link to="/" id="logo">Weshare</router-link>
    </div>
    <!--banner-->
    <div class="banner"></div>
    <ul class="top__list">
      <div class="wrapper" @click="toggleNav">
        <router-link  v-for="(item, idx) in routeList" 
        :key="idx" 
        class="top__item" 
        tag="li" 
        :to="item.path"
        activeClass="link_active"
        exact
        >
          <span class="top__item-title">{{item.name}}</span>
        </router-link>
      </div>
    </ul>
  </header>
</template>

<script>
import routes from '../router'
export default {
  data () {
    return {
      routeList: routes.options.routes,
    }
  },
  methods: {
    toggleNav() {  //切换
      document.querySelector(".top__hamburger")
      .classList.toggle("top__hamburger--active")
      document.querySelector(".top__list")
      .classList.toggle("top__list--active")
    },
    handleScroll() {  //菜单栏吸附
       var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
       if( scrollTop >=(15.5*16)){
         document.querySelector('.top__list').style.position = "fixed" 
         document.querySelector('.top__list').style.top = "0"
       }else{
         document.querySelector('.top__list').style.position = "static" 
       }
    },
  },
  mounted() {
    /***设置滚动监听事件 */
    // window.addEventListener('scroll', this.handleScroll)

    
  },
}
</script>

<style lang="scss">
@import '../scss/variable.scss';
@import '../scss/media-queries.scss';
#logo{
  @include tablet-min{
    display: none;
  }
}
header{
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 10;
  background-color: $c-green;
  @include tablet-min{
    position: static;
    width: 100%;
    min-width: $min-width;
  }
}
.link_active{
  // background-color:  $c-deepgreen;
  border-bottom: 4px solid $c-green;
}
.banner{
  @include tablet-min{
    background: url('../assets/titan.jpg') no-repeat;
    background-size: 100%;
    width: 100%;
    min-width: $min-width;
    height: 15.5rem;
  }
}
.top{
  background-color: $c-green;
  width: 100%;
  height: 3.5rem;
  display: flex;
  justify-content: center;
  @include tablet-min{
    justify-content: flex-end;
    min-width: $min-width;
    position: absolute;
    z-index: 10;
    background-color: rgba($c-dark, 0.8);
  }
  a{
    text-align: center;
    line-height: 3.5rem;
  }
  &__user{
    position: fixed;
    top: 0;
    right: 0;
    display: flex;
    margin-right: 17px;
    height: 3.5rem;
    line-height: 3.5rem;
    @include tablet-min{
      color: $c-white;
      position: static;
    }
    li{
      font-size: 14px;
      font-weight: 350;
      &:nth-child(1){
        &::after{
          content: "\B7";
          margin: 0 .3rem;
        }
      }
      a{
        @include tablet-min{
          color: $c-white;
        }
      }
    }
  }
  &__hamburger{
    position: fixed;
    top: 0;
    left: 0;
    width: 3.5rem;
    height: 3.5rem;
    z-index: 10;
    @include tablet-min {
      display: none;
    }
    .bar{
      width: 22px;
      height: 1px;
      position: absolute;
      transition: all .3s ease;
      background: rgba(8, 28, 36, 0.5);
      &:nth-child(1){
        left: 16px;
        top: 17px;
      }
      &:nth-child(2){
        right: 18px;
        top: 26px;
        &::after{
          content: "";
          position: absolute;
          left: 0px;
          top: 0px;
          width: 23px;
          height: 1px;
          background: transparent;
          transition: all 300ms ease;
        }
      }
      &:nth-child(3){
        left: 16px;
        top: 35px;
      }
    }
    &--active{
      .bar{
        &:nth-child(1),
        &:nth-child(3){
          width: 0;
        }
        &:nth-child(2){
          transform: rotate(-45deg);
        }
        &:nth-child(2):after {
          transform: rotate(-90deg);
          background: rgba($c-dark, 0.5);
        }
      }
    }
  }
  &__list{
      position: fixed;
      top: 3.5rem;
      left: 0;
      background: rgba($c-white, 0.98);
      width: 100%;
      box-sizing: border-box;
      @include mobile-only{
        border-top: 1px solid $c-light;
        opacity: 0;
        visibility: hidden;
        height: calc(100vh - 3.5rem);
        transition: all 0.5s ease;
        &--active{
          opacity: 1;
          visibility: visible;
        }
      }
      @include tablet-min{
        position: static;
        background-color: $menu-color;
        height: 3.5rem;
        box-shadow: 0px 2px 10px 0px rgba(0,0,0,0.1), 0 1px rgba(0,0,0,0.1);
        .wrapper{
          display: flex;
        }
      }
    }
    &__item{
      @include mobile-only {
        display: inline-block;
        text-align: center;
        width: 50%;
        height: 6rem;
        line-height: 6rem;
        border-bottom: 1px solid $c-light;
        &:nth-child(even){
          border-right: 1px solid $c-light;
        }
      }
      @include tablet-min{
        width: 6rem;
        height: 3.5rem;
        line-height: 3.5rem;
        text-align: center;
        cursor: pointer;
        &:nth-child(1){
          text-align: left;
          width: 2rem;
          margin-right: 1rem;
          border-bottom: none;
        }
      }
    }
}
</style>
