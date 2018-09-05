<template>
  <div class="space">
    <div class="h">
      <div class="h-inner">
        <div class="h-gradient"></div>
        <div class="h-user">
          <div class="h-info">
            <Avatar class="avatar" />
            <div class="h-basic">
              <div class="h-name">
                木拉M
              </div>
              <div class="h-basic-spacing">
                我爱吃柚子
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-view></router-view>
  </div>  
</template>

<script>
export default {};
</script>

<style lang="scss">
.space {
  color: $c-light;
  .h {
    top: 3.5rem;
    height: 12.5rem;
    position: absolute;
    @include firstMedia {
      width: $main-width;
    }
    @include secondMedia {
      width: $min-width;
    }
    &-inner {
      background-image: url("../../assets/bg2.jpg");
      background-position: 50%;
      background-size: cover;
      padding-top: 7.5rem;
    }
    &-user {
      position: relative;
      z-index: 1;
    }
    &-basic {
      margin: 10px 0 0 20px;
    }
    &-name {
      font-size: 18px;
    }
    &-basic-spacing {
      font-size: 12px;
    }
    &-gradient {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 5rem;
      background-image: url("../../assets/shadow.png");
      background-repeat: repeat-x;
    }
    &-info {
      width: 100%;
      margin-left: 2rem;
      padding-bottom: 1rem;
      display: flex;
      .avatar {
        width: 4rem;
        height: 4rem;
        border-radius: 50%;
      }
    }
  }
}
</style>
