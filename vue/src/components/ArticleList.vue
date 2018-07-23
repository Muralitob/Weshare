<template>
  <div class="arlist pl pr">
    <div class="arlist__wrap">
      <div class="arlist__box">
      <p class="arlist__box-title">{{title}}</p>
      <span class="arlist__box-more" @click="goToMore">More</span>
      </div>
      <div class="arlist__list" >
        <div class="arlist__item" v-for="(item,index) in dataList" :key="index">
          <router-link to="#">
            <div class="arlist__item--summary">{{item.summary}}</div>
          </router-link>
          <div class="arlist__item--time">{{item.time}}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: [ 'title' ],
  data () {
    return {
      dataList: [
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
        {summary: 'Weshare正式上线发布......', time: '04/19'},
      ]
    }
  },
  methods: {
    goToMore(){
      //dosomthing
      this.$router.push( { name: `${this.title}`} )
    }
  }
}
</script>

<style lang="scss" scoped >
.arlist{
  margin-top: 1.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background-color: $c-white;
  &__wrap{
    @include mobile-only{
      border-bottom: 1px solid #E5E5E5;
      padding-bottom: 1.5rem;
    }
    @include tablet-min{
      padding: 0;
    }
  }
  &:nth-child(2){
    margin-top: 2.5rem;
    @include tablet-min{
      margin-top: 1.5rem;
    }
  }
  @include tablet-only{
    width: 30rem;
    height: 21.25rem /* 340/16 */;
    background-color: $c-white;
    border-radius: 7px;
  }
  @include desktop-min{
    width: 35rem;
    height: 23rem /* 340/16 */;
    background-color: $c-white;
    border-radius: 7px;
  }
  &__box{
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    &-more{
      cursor: pointer;
      transition: all .3s ease;
      &:hover{
        transform: scale(1.05);
      }
    }
    &-title{
      font-weight: 550;
      &::before{
        content: ''
      }
    }
  }
  &__item{
    display: flex;
    justify-content: space-between;
    margin-top: .8rem;
    padding-bottom: .3rem;
    border-bottom: 1px dashed #CCC;
  }
}

.nav__link-icon{
  width: 20px;
  height: 20px;
  margin-bottom: 3px;
  fill: rgba($c-dark, 0.7);
  transition: fill 0.5s ease;
  @include tablet-min {
    width: 20px;
    height: 20px;
    margin-bottom: 5px;
  }
}
</style>
