<template>
  <div class="space">
    <div class="h">
      <div class="h-inner">
        <div class="h-gradient"></div>
        <div class="h-user">
          <div class="h-info">
            <Avatar class="avatar" @click="" />
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
    <div class="b">
      <router-view></router-view>
      <div>
        <Card class="b-profile-info row" style="width:240px" dis-hover shadow>
          <Row>
            <Col span="12" class="col wrap" style="text-align:center">
              <span>我的关注</span>
              <span>0</span>
            </Col>
            <Col span="12" class="col wrap" style="text-align:center">
              <span>粉丝人数</span>
              <span>0</span>
            </Col>
          </Row>
        </Card>
        <Menu theme="light" class="b-menubar" @on-select="routeTo" :active-name="activeName">
          <MenuItem name="index">我的主页</MenuItem>
          <MenuItem name="collection">我的收藏</MenuItem>
          <MenuItem name="history">浏览记录</MenuItem>
        </Menu>
      </div>
    </div>
  </div>  
</template>

<script>
export default {
  data () {
    return {
      
    }
  },
  methods: {
    //menu跳转
    routeTo(name) {
      this.$router.push({path: `/space/${this.$route.params.userId}/${name}`});
      this.$store.commit('Menu_SELECT', name)
    }
  },
  computed: {
    activeName () {
      console.log(this.$store.state.Menu.activeName)
      return this.$store.state.Menu.activeName
    }
  }
};
</script>

<style lang="scss">
.space {
  .h {
    top: -3rem;
    position: relative;
    height: 12.5rem;
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
      color: $c-light;
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
  .b {
    width: 100%;
    position: relative;
    display: flex;
    justify-content: space-between;
    &-menubar {
      border: 1px solid #eee;
      margin-top: 1rem;
    }
    &-profile-info {
      width: 100%;
    }
  }
}
</style>
