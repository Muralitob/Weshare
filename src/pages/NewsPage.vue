<template>
  <div class="news">
    <navi-bar></navi-bar>
    <div class="news__wrapper">
      <div class="news__list">
        <ul class="news__list-box">
          <li class="news__list-item" 
          v-for=" (item, index) in articleList" 
          :key="index">
            <p>
              <a href="">[{{item.type}}]</a>
              <a href="">{{item.summary}}</a>
            </p>
            <span>{{item.time}}</span>
          </li>
        </ul>
        <div class="news__list-page">
          <button>上一页</button>
          <button>下一页</button>
        </div>
      </div>
      <div class="news__subside">广告或者其他</div>
    </div>
  </div>
</template>

<script>
import NaviBar from '../components/Navi'
export default {
  components: { NaviBar },
  data () {
    return {
      articleList: [
        { type: '公告', summary: '微分享重磅登场......', time: '2018-04-12' },
      ]
    }
  }
}
</script>

<style lang="scss">
.news{
  &__wrapper{
    display: flex;
    justify-content: space-between;
  }
  &__list{
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
    }
    &-box{
      @include tablet-min{
        padding: 30px 0 30px;
      }
    }
    &-item{
      display: block;
      position: relative;
      font-size: 14px;
      border-left: 4px solid #fff;
      margin-bottom: 6px;
      &:hover{
        border-left: 4px solid $c-green;
        a{
          color: $c-green;
        }
      }
      p{
        width: 92%;
        height: 37px;
        line-height: 37px;
        margin: 0 auto;
        border-bottom: 1px dashed #BFBFBF;
      }
      span{
        position: absolute;
        top: 0;
        right: 4%;
        line-height: 37px;
        color: $c-gray;
        font-size: 12px;
      }
    }
    &-page{
      text-align: center;
      margin: 20px 20px;
      button{
        width: 60px;
        height: 30px;
        line-height: 30px;
        text-align: center;
        display: inline-block;
        border: 1px solid #CECECE;
        font-size: 14px;
        color: $c-gray;
        font-weight: normal;
        border-radius: 4px;
        cursor: pointer;
        &:hover{
          background-color: #03c36f;
          color: $c-white;
        }
      }
    }
  }
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
