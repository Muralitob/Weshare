<template>
  <div class="newsp">
    <!-- <navi-bar ></navi-bar> -->
    <div class="newsp__list">
      <ul class="newsp__list-box">
        <li class="newsp__list-item" 
        v-for=" (item, index) in articleList" 
        :key="index">
          <p>
            <router-link :to="{path: `/news/${item._id}`}">[{{item.type}}]</router-link>
            <router-link :to="{path: `/news/${item._id}`}">{{item.summary}}</router-link>
          </p>
          <span>{{item.created_at}}</span>
        </li>
      </ul>
      <div class="newsp__list-page">
        <button>上一页</button>
        <button>下一页</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  components: {  },
  data () {
    return {
      articleList: [
        { type: '公告', summary: '微分享重磅登场......', created_at: '2018-04-12', _id: '123113213' },
      ]
    }
  }
}
</script>

<style lang="scss">
.newsp{
  display: flex;
  flex-direction: column;
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
      min-height: 50rem;
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
}
</style>
