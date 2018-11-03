<template>
  <div>
    <div  class="top__user" v-if="Token">
      <Dropdown trigger="click">
        <div class="user_avator">
          <Avatar  style="background-color: #87d068" icon="ios-person" />
        </div>
        <DropdownMenu slot="list">
          <DropdownItem @click.native="routeTo('space')" >
            <Icon type="md-home" />
            <span>我的空间</span>
          </DropdownItem>
          <DropdownItem @click.native="routeTo('setting')" >
              <Icon type="md-settings"   />
              <span>个人设置</span>
          </DropdownItem>
          <DropdownItem @click.native="LogOut">
              <Icon type="md-log-out" />
              <span>退出</span>
            </DropdownItem>
        </DropdownMenu>
      </Dropdown>
    </div>
    <ul class="top__user" v-else>
      <li @click="Login"><span>登录</span></li>
      <li @click="Regist"><span>注册</span></li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imgurl: ''
    }
  },
  methods: {
    Login() {
      this.$store.commit('LOGIN_SHOW')
    },
    Regist() {
      this.$store.commit('REGIST_SHOW')
    },
    LogOut() {
      this.$store.dispatch('UserLogOut',this)
    },
    routeTo(name) {
      const uid = this.$cookie.get('uid')
      if(uid){
        this.$router.push({
          path: `/${name}/${uid}`
        });
      }
    }
  },
  computed: {
    Token: {
      get() {
        return this.$store.state.UserSetting.token;
      },
      set() {
        
      }
    }
  },
  updated () {
  }
}
</script>

<style lang="scss">
  .user_avator{
    cursor: pointer;
  }
</style>
