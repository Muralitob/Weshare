<template>
  <div class="art-com">
    <div id="news-header">
      <h1 class="header-title">评论</h1>
      <p class="header-protocol">文明上网理性发言</p>
      <p class="header-number">8条评论</p>
    </div>
    <div class="box">
      <div class="myface" >
        <Avatar icon="ios-person" size="large" />
      </div>
      <div class="box-textarea">
        <Input :cols=80 :rows=2  type="textarea" placeholder="请自觉遵守互联网相关的政策法规，严禁发布色情、暴力、反动的言论。" />
        <button class="box-post">发表评论</button>
      </div>
    </div>
    <div class="comment-list">
      <div class="list-item" v-for="(item, idx) in comLists" :key="idx">
        <div class="user-face">
          <Avatar icon="ios-person" size="large"  />
        </div>
        <div class="con">
          <div class="user-name">{{item.userName}}</div>
          <p class="text">{{item.comText}}</p>
          <div class="info">
            <span>#{{idx}}</span>
            <span class="time">{{item.comTime}}</span>
            <span class="like"><Icon type="md-thumbs-up" />{{item.comLikes}}</span>
            <span class="reply"><Button type="text">回复</Button></span>
          </div>
          <div class="reply-box">
            <div class="reply-item">
              <Avatar icon="ios-person" size="small" class="reply-face" />
              <div class="reply-con">
                <div class="reply-name">Mura</div>
                <div class="info">
                  <span class="time">2018-10-1 22:55</span>
                  <span class="like"><Icon type="md-thumbs-up" />0</span>
                  <span class="reply"><Button type="text">回复</Button></span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>  
</template>

<script>
export default {
  data() {
    return {
      comLists: [
        {
          userName: 'Mura',
          userUrl: '',
          comTime: '2018-10-1 22:55',
          comLikes: 40,
          comText: 'skrrrrrrrrrrrrrrrrrr',
        },
        {
          userName: 'Mura',
          userUrl: '',
          comTime: '2018-10-1 22:55',
          comLikes: 40,
          comText: 'skrrrrrrrrrrrrrrrrrr',
        }
      ]
    }
  }
}
</script>

<style lang="scss">
  .art-com {
    border: 1px solid #E1E1E1;
    background-color: #fff;
    padding: 20px;
    #news-header {
      display: flex;
      align-items: center;
      position: relative;
      padding-bottom: 20px;
      .header {
        &-title {
          font-size: 26px;
          color: #2a2a2a;
          height: 100%;
          margin-right: 10px;
        }
        &-protocol {
          height: 52px;
          color: #ccc;
          font-size: 14px;
          position: absolute;
          margin-left: 4rem;
          line-height: 52px;
        }
        &-number {
          position: absolute;
          right: 0;
          height: 52px;
          line-height: 52px;
          color: #adadad;
          font-size: 14px;
        }
      }
    }
    .box {
      .myface {
        float: left;
        margin-top: 6px;
        position: relative;
      }
      &-textarea {
        position: relative;
        margin-left: 4rem;
        margin-right: 6rem;
        textarea {
          resize: none;
        }
      }
      &-post {
        width: 58px;
        height: 52px;
        position: absolute;
        right: -6rem;
        top: 0;
        padding: 4px 15px;
        font-size: 14px;
        color: #fff;
        border-radius: 4px;
        text-align: center;
        min-width: 60px;
        vertical-align: top;
        cursor: pointer;
        background-color: $c-green;
        border: 1px solid $c-green;
        transition: .1s;
        user-select: none;
        outline: none;
      }
    }
  }
  .comment-list {
    padding-top: 20px;
    .list-item {
      // display: flex;
      // padding: 22px 0 14px;
      .user-face {
        float: left;
        margin-top: 24px;
      }
      .con {
        position: relative;
        margin-left: 4rem;
        border-top: 1px solid #e5e9ef;
        padding: 22px 0 14px;
        .user-name {
          color: #6d757a;
        }
        .text {
          padding-bottom: 4px;
        }
        .info {
          display: flex;
          span {
            margin-right: .5rem;
            display: flex;
          }
        }
        .reply {
            button {
              padding: 0;
            }
            &-box {

            }
            &-item {
              padding: 10px 0;
            }
            &-face {
              float: left;
              margin-top: 0;
            }
            &-con {
              position: relative;
              margin-left: 2rem;
            }
          }
      }
    }
  }
</style>
