<template>
  <div class="follow">
    <span v-if="result.length <= 0">暂无关注,赶快去关注吧！</span>
    <ul v-else class="relation-list">
      <li class="list-item" v-for="(item, idx) in result" :key="idx">
          <Avatar class="avatar" @click.native="routeTo(item.uid)" />
        <div class="content" >
          <div class="fan-name" @click="routeTo(item.uid)">
            {{item.nickname}}
          </div>
          <p class="desc">
              {{item.sign|| ''}}
          </p>
        </div>
        <Dropdown trigger="click" class="fan-dropdown" @on-click="function(name){fanEdit(name, item.uid)}">
          <Button type="primary">
            已关注
            <Icon type="ios-arrow-down"></Icon>
          </Button>
          <DropdownMenu slot="list" >
            <DropdownItem name="unfollow" @click="cancelFollow(item._id)">取消关注</DropdownItem>
          </DropdownMenu>
        </Dropdown>
      </li>
    </ul>
  </div>  
</template>

<script>
let lodash = require('lodash')
import api from '../../api'
export default {
  props: [ 'type' ],
  data() {
    return {
      result: [
      ],
    }
  },
  mounted () {
    this.fetchReult(1)
  },
  methods: {
    fetchReult(page) {
      api.followAttention('get', 1, page).then(({data}) => {
        this.$store.commit('TOTAL_WATCH', data.total)
        this.result = data.attentions
      })
    },
    fanEdit(name,uid) {
      //根据
      if(name==='unfollow') {
        this.cancelFollow(uid)
      }
    },
    routeTo(uid) {
      this.$router.push({
        path: `/space/${uid}`
      });
    },
    cancelFollow(_id) {
      api.followAttention('delete', _id).then(({data}) => {
        if(data.code === 213) {
          this.fetchReult(1)
        }
      })
    }
  },
  watch: {
    type() {
      if(this.type === '00') {
        this.fetchReult(1)
      }else {
        this.result = []
      }
    }
  },
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
