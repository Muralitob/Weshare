<template>
  <div class="micro">
    <div class="used-list">
      <header>历史记录</header>
      <section>
        <div @click="startTalk(item.chater_uid, item.chater)" class="chat_item" v-for="(item, index) in user_list" :key="index">
          <span class="chat_item_title">{{item.chater}}</span>
        </div>
      </section>
    </div>
    <div class="talk">
      <div class="flex">
        <span v-if="current_id" class="talk_info">与{{nickname}}对话中</span>
        <div class="pointer" @click="goback">返回</div>
      </div>
      <div class="talk_board">
        <div class="line">
          <div class="bubble" v-for="(item, index) in line" :key="index">
            <div class=" left" v-if="item.from == uid">
              <Avatar :src='user_info.avatar_url' class="avatar" />
              <span class="bubble_msg">{{item.msg}}</span>
            </div>
            <div class="right" v-else>
              <span class="bubble_msg">{{item.msg}}</span>
              <Avatar :src='myavatar' class="avatar" />
            </div>
          </div>
        </div>
      </div>
      <div class="input">
        <textarea class="talk_input" v-model="strmsg">
        </textarea>
          <button class="talk_send" @click="sendMsg">发送</button>
      </div>
    </div>
  </div>

</template>

<script>
import api from '../../api'
export default {
  data() {
    return {
      line: [],
      current_id: '',
      user_list: [],
      nickname: this.$route.params.nickname,
      uid: this.$route.params.userId,
      user_info: {},
      myavatar: localStorage.getItem('myavatar'),
      first: false,
      strmsg: ''
    }
  },
  methods: {
    getUserInfo() {
      api
        .getUserInfo(this.uid)
        .then(({ data }) => {
            this.user_info =  {
            nickname: data.nickname,
            sign: data.sign,
            avatar_url: `data:image/png;base64,${data.avatar_base64}`
          };
        })
        .catch(err => {
          console.log(err);
        });
    },
    getTalkList() {
      api.talkto('get').then(({data}) => {
         this.user_list = data
      }).catch((err) => {
        
      });
    },
    getChatLogs(_id) {
      api.talkto('get', _id).then(({data}) => {
        this.line = data.content
        let dom = document.getElementById('talk_board')
        dom.scrollTop = dom.scrollHeight
      }).catch((err) => {
      });
    },
    startTalk(_id, nickname) {
      this.current_id = _id
      this.nickname = nickname
      this.getChatLogs(_id)
    },
    sendMsg() {
      let str = ''
      str = 'post'
      if(this.strmsg) {
        api.talkto(str, {
          to: parseInt(this.current_id),
          msg: this.strmsg
        }).then(({data}) => {
          if(data.code === 501) {
            this.strmsg = ''
            this.getChatLogs(this.current_id)
          }
        }).catch((err) => {

        });
      }else {
        return
      }
    },
    goback() {
      this.$router.back(-1)
    }
  },
  mounted() {
    this.getTalkList()
  }
}
</script>

<style lang="scss">
  .micro {
    display: flex;
  }
  .chat_item {
    padding: 10px 10px;
    cursor: pointer;
    &:hover {
      background-color: #eee;
    }
    &_title {
      font-size: 16px;
    }
  }
  .used-list {
    width: 180px;
    margin-right: 24px;
    display: flex;
    flex-direction: column;
    section {
      margin-top: 10px
    }
  }
  .flex {
    display: flex;
    justify-content: space-between;
  }
  .talk {
    flex: 1;
    width: 100%;
    height: 100%;
    &_info {
      display: block;
      font-size: 18px;
      padding-bottom: 12px;
      color: black;
    }
    &_board {
      width: 100%;
      height: 520px;
      background-color: #eee;
      overflow: auto;
      padding: 20px;
      border-top-left-radius: 8px;
      border-top-right-radius: 8px;
      &::-webkit-scrollbar {
        display: none;
      }
    }
    .input {
      height: 120px;
      width: 100%;
    }
    &_input {
      border: none;
      border-top: 1px solid #ccc;
      height: 120px;
      background-color: #eee;
      position: relative;
      width: 100%;
      resize: none;
      outline: none;
      padding: 20px;
      overflow-y: auto;
      &:focus {
        background-color: #fff;
      }
    }
    &_send {
      float: right;
      position: relative;
      top: -60px;
      left: -20px;
      background-color: #eee;
      width: 120px;
      height: 42px;
      // outline: none;
      border: 1px solid #ccc;
      &:hover {
        background-color: #01d277;
        color: #fff;
      }
    }
  }
  .input {
    background-color: #eee;
    &:focus {
      background-color: #fff;
    }
  }
  .bubble {
    margin: 12px 0;
  }
  .bubble_msg {
    font-size: 16px;
  }
  .line {
    display: flex;
    flex-direction: column;
  }
  .right {
    // align-items: flex-end;
    float: right;
  }
  .pointer {
    cursor: pointer;
  }
</style>
