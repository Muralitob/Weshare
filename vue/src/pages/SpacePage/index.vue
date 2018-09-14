<template>
  <div class="space">
    <div class="h">
      <div class="h-inner">
        <div class="h-gradient"></div>
        <div class="h-user">
          <div class="h-info">
            <router-link :to="{name: 'setting' }">
              <Avatar class="avatar" />
            </router-link>
            <div class="h-basic">
              <div class="h-name">
                木拉M
              </div>
              <div class="h-basic-spacing">
                <span>
                  我爱吃柚子
                </span>
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
              <router-link exact-active-class="active" :to="fourl" @click.native="reset"  >
                <div>
                  <Icon type="md-eye" size="20" color="#23c9ed"  />
                  <span>我的关注</span>
                </div>
                <span>0</span>
              </router-link>
            </Col>
            <Col span="12" class="col wrap" style="text-align:center">
              <router-link exact-active-class="active" :to="faurl" @click.native="reset" >
                <div>
                  <Icon type="md-heart" size="20" color="#ff5d47" />
                  <span>粉丝人数</span>
                </div>
                <span>0</span>
              </router-link >
            </Col>
          </Row>
        </Card>
        <Menu theme="light" class="b-menubar" @on-select="routeTo" :active-name="activeName">
          <MenuItem name="index"> <Icon type="md-home" color="#00c091" size="20" />我的主页</MenuItem>
          <MenuItem name="article"><Icon type="md-create" color="#02b5da" size="20" />我的文章</MenuItem>
          <MenuItem name="collection"><Icon type="md-star" size="20" color="#f3a034" /></Icon>我的收藏</MenuItem>
          <MenuItem name="history"><Icon type="md-paw" size="20" color="#23c9ed" />浏览记录</MenuItem>
        </Menu>
      </div>
    </div>
  </div>  
</template>

<script>
export default {
  data() {
    return {
      fourl: `/space/${this.$route.params.userId}/index/fan/00`,
      faurl: `/space/${this.$route.params.userId}/index/fan/-1`,
    };
  },
  methods: {
    //menu跳转
    routeTo(name) {
      this.$router.push({
        path: `/space/${this.$route.params.userId}/${name}`
      });
      this.$store.commit("Menu_SELECT", name);
    },
    reset() {
      this.$store.commit('Menu_SELECT', 'index')
    }
  },
  computed: {
    activeName() {
      return this.$store.state.Menu.activeName;
    }
  },
  mounted() {
    //判断this.$route.params.userId是否与本地储存的uid是否相同
    //相同则展示目前的样子，如果不相同 则为他人空间，最好每个组件都传uid判断一下
  },
};
</script>

<style lang="scss">
.space {
  .active {
    color: $c-green;
  }
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
      color: #d6dee4;
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
