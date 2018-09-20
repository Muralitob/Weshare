<template>
  <div class="follow">
    <ul class="relation-list">
      <li class="list-item" v-for="(item, idx) in result" :key="idx">
          <Avatar class="avatar" @click.native="routeTo(item.uid)" />
        <div class="content" >
          <div class="fan-name" @click="routeTo(item.uid)">
            {{item.user_name}}
          </div>
          <p class="desc">
            {{item.user_desc}}
            <span v-if="!item.user_desc">
              我就是我~~~
            </span>
          </p>
        </div>
        <Dropdown trigger="click" class="fan-dropdown" @on-click="function(name){return fanEdit(name, item.uid)}">
          <Button type="primary">
            已关注
            <Icon type="ios-arrow-down"></Icon>
          </Button>
          <DropdownMenu slot="list" >
            <DropdownItem name="group" >编辑分组</DropdownItem>
            <DropdownItem name="unfollow">取消关注</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </li>
    </ul>
  </div>  
</template>

<script>
let lodash = require('lodash')
export default {
  props: [ 'type' ],
  data() {
    return {
      result: [
        {
          uid: '01',
          user_name: 'Mura',
          user_desc: '我爱吃柚子'
        },
        {
          uid: '02',
          user_name: '村人B',
          user_desc: '我爱吃柚子'
        },
      ]
    }
  },
  created: function () {
    //控制watch请求频率,减轻压力 防抖动
    this.debouncedFetchResult = lodash.debounce(this.fetchReult, 500)
    this.debouncedFetchResult()
  },
  methods: {
    fetchReult() {
      console.log('开始获取数据')
    },
    fanEdit(name,uid) {
      //根据
      console.log(name, uid)
    },
    routeTo(uid) {
      this.$router.push({
        path: `/space/${uid}`
      });
    },
  },
  watch: {
    type() {
      this.debouncedFetchResult()
    }
  }
}
</script>

<style lang="scss">
.follow{
  .avatar {
    width: 52px !important;
    height: 52px !important;
    border-radius: 50%;
    cursor: pointer;
  }
  .list-item {
    border-bottom: 1px solid #eee;
    display: block;
    padding: 20px 0;
    position: relative;
    display: flex;
    align-items: center;
  }

  .content {
    margin-left: 1.5rem; 
    // line-height: 52px;
  }
  .desc {
    font-size: 12px;
    color: #777;
  }
  .fan-name {
    // margin-bottom: 10px;
    cursor: pointer;
  }
  .fan-dropdown {
    position: absolute;
    right: 20px;
  }
}
</style>
