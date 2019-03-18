<template>
  <div>
    <div class="talk">
      <span class="talk_info">与{{nickname}}对话中</span>
      <div class="talk_board">
        <Avatar :src='user_info.avatar_url' class="avatar" />
      </div>
      <div class="input">
        <textarea class="talk_input">
        </textarea>
          <button class="talk_send">发送</button>
      </div>
    </div>
      <div class="info">

      </div>

  </div>

</template>

<script>
import api from '../../../api/index.js'
export default {
  data() {
    return {
      line: [

      ],
      nickname: this.$route.params.nickname,
      uid: this.$route.params.userId,
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
  },
  mounted() {
    this.getUserInfo()
  }
}
</script>

<style lang="scss">
  .talk {
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
</style>
