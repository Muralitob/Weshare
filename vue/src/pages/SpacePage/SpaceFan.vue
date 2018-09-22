<template>
  <div class="fan">
    <Menu style="position: relative" ref="fanMenu" width="180px" theme="light" :active-name="Fan_Type" @on-select='routeTo'>
      <Icon type="md-add-circle" color='#cbd0d8' class="add" size="20" @click="addGroup" />
      <MenuGroup title="我的关注">
        <MenuItem name="00" class="between">
            <div>
              <Icon type="md-people" />
              全部关注
            </div>
            <span class="num">20</span>
        </MenuItem>
        <MenuItem name="01" class="between">
          <div>
            <Icon type="md-person" />
            特别关注
          </div>
          <span class="num">0</span>
        </MenuItem>
        <MenuItem name="02" class="between">
          <div>
            <Icon type="md-eye-off" />
            悄悄关注
          </div>
          <span class="num">0</span>
        </MenuItem>
        <MenuItem name="03" class="between">
          <div>
            <Icon type="md-bookmark" />
            默认关注
          </div>
          <span class="num">20</span>
        </MenuItem>
        <MenuItem v-for="(item, idx) in my_group" :key="idx" :name="item.id" class="between" >
          <div>
            <Icon type="md-outlet" />
            {{item.group_name}}
          </div>
          <span class="num">{{item.group_count}}</span>
        </MenuItem>
    </MenuGroup>
    <MenuGroup title="我的粉丝" >
      <MenuItem name="fans" class="between" >
      <div>
        <Icon type="md-heart" />
        我的粉丝
      </div>
      <span class="num">0</span>
      </MenuItem>
    </MenuGroup>
    </Menu>
    <div class="fan-main">
      <space-follow :type='fan_type'></space-follow>
    </div>
  </div>  
</template>
<script>
import SpaceFollow from './SpaceFollow'
export default {
  components: { SpaceFollow },
  data() {
    return {
      fan_type: '',
      my_group: [],
    }
  },
  methods: {
    addGroup() {},
    routeTo(tagID) {
      if(tagID === 'fans') {
        this.$router.push({
        path: `/space/${this.$route.params.userId}/index/fans`
      });
      }else {
        this.$router.push({
          path: `/space/${this.$route.params.userId}/index/fan/${tagID}`
        });
      }
      this.fan_type = tagID
    },
  },
  computed: {
    Fan_Type() {
      if(this.$route.params.tagID) {
        return this.$route.params.tagID
      }else {
        return 'fans'
      }
    }
  },
  mounted() {
    // this.$nextTick(function() {
    //     this.$refs.fanMenu.updateActiveName();
    //     console.log(this.$refs.fanMenu);
    //   })
    
  },
};
</script>

<style lang="scss">
.fan {
  width: 62rem;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0 0 0 1px #eee;
  display: flex;
  &-main {
    width: calc(62rem - 180px);
    padding: 20px 20px;
  }
  .add {
    position: absolute;
    top: 13px;
    right: 24px;
    z-index: 10;
    cursor: pointer;
    &:hover {
      color: rgb(173, 174, 183) !important;
    }
  }
}
.ivu-menu {
  border: none;
}
.between div {
  font-size: 14px;
}
.num {
  display: inline-block;
  width: 20px;
  color: #99a2aa;
  text-align: center;
  line-height: 19px;
}
.fan .ivu-menu-light.ivu-menu-vertical .ivu-menu-item-active {
  background: $c-green;
  color: #fff;
  .num {
    color: #fff;
  }
}
</style>
