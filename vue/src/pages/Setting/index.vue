<template>
  <div class="security_content">
    <Menu style="position: relative" ref="side_menu" width="180px" theme="primary" :active-name="security_type" @on-select='routeTo'>
      <MenuGroup title="个人中心">
        <MenuItem name="info" >
          <Icon type="md-people" />
          个人资料
        </MenuItem>
        <MenuItem name="avator" >
          <Icon type="md-camera" />
          我的头像
        </MenuItem>
        <MenuItem name="account" >
          <Icon type="md-lock" />
          账号安全
        </MenuItem>
        <MenuItem name="space" >
          <Icon type="md-home" />
          个人空间
        </MenuItem>
    </MenuGroup>
    </Menu>
    <div class="security_main">
      <!-- <space-follow :type='fan_type'></space-follow> -->
      <router-view></router-view>
    </div>
  </div>   
</template>

<script>
export default {
  data() {
    return {
      security_type: 'info'
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.$refs.side_menu.updateOpened();
      this.$refs.side_menu.updateActiveName();
    });
  },
  methods: {
    routeTo(name) {
      this.$router.push({
        path: `/setting/${this.$route.params.userId}/${name}`
      });
      if( name === 'space') {
        this.$router.push({
          path: `/space/${this.$route.params.userId}`
        });
      }
    }
  }
}
</script>

<style lang="scss">
.security{
  &_content {
    overflow: hidden;
    width: 100%;
    height: 100%;
    margin: 10px auto 100px;
    border: 1px solid #e1e2e5;
    box-shadow: 0 2px 4px rgba(0,0,0,.14);
    background: #fff;
    border-radius: 4px;
    display: flex;
  }
  &_main {
    width: calc(100% - 180px);
    min-height: 40rem;
    padding: 20px 20px;
  }
}
</style>
