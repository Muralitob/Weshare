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
        <Input v-model="first_content" :cols=80 :rows=2  type="textarea" placeholder="请自觉遵守互联网相关的政策法规，严禁发布色情、暴力、反动的言论。" />
        <button @click="reply" class="box-post">发表评论</button>
      </div>
    </div>
    <div v-if="comLists.length > 0" class="comment-list">
      <div class="list-item" v-for="(parent, idx) in comLists" :key="idx">
        <div class="user-face">
          <Avatar icon="ios-person" size="large"  />
        </div>
        <div class="con">
          <router-link to="" class="user-name" >
            {{parent.userName}}
          </router-link>
          <p class="text">{{parent.content}}</p>
          <div class="info">
            <span>#{{idx}}</span>
            <Time type="date" :time="parent.comment_time" />
            <span class="like"><Icon type="md-thumbs-up" />{{parent.like_num}}</span>
            <span class="reply"><Button type="text" @click="reply(parent)">回复</Button></span>
          </div>
          <div class="reply-box">
            <div class="reply-item" v-for="(child, idx) in parent.comments" :key="idx">
              <Avatar icon="ios-person" size="small" class="reply-face" />
              <div class="reply-con">
                <router-link to="" class="user-name" >
                  {{child.reply_Name}}
                </router-link>
                <span class="reply-text">{{child.reply_Text}}</span>
                <div class="info">
                  <span class="time">{{child.reply_Time}}</span>
                  <span class="like"><Icon type="md-thumbs-up" />{{child.reply_Likes}}</span>
                </div>
              </div>
            </div>
            <Page prev-text="上一页" next-text="下一页" @on-change="changepage" v-if="parent.viewMore" :total="40" size="small" class-name="reply-pageBox"></Page>
            <!-- <we-page :item="parent" ></we-page> -->
            <div class="more" v-if="parent.replyNums>3&&!parent.viewMore">共有<b>{{parent.replyNums}}</b>条回复<Icon @click="viewmore(parent)" size='28' type="md-arrow-dropdown" class="more-view"/></div>
            <div class="box-textarea reply-textarea" v-if="parent.replyshow">
              <Input :cols=80 :rows=2  type="textarea" :placeholder='placeholderString' />
              <button class="box-post" @click="reply">发表评论</button>
            </div>
          </div>
        </div>
      </div>
      <Page prev-text="上一页" next-text="下一页" @on-change="changepage" :total="total" show-elevator class-name="commit-pageBox"></Page>
    </div>
    <div class="no_reply" v-else>
      <span>暂无评论 :)</span>
    </div>
  </div>  
</template>

<script>
import api from "../api";
import general from "../general/js";
export default {
  props: ["list"],
  data() {
    return {
      comLists: [],
      placeholderString: "回复:",
      nowReplyPerson: "",
      first_content: "",
      a_id: this.$route.params["com_id"],
      total: 0,
      currentPage: 1
    };
  },
  methods: {
    async reply(parent) {
      //主级评论
      if (!parent.replyshow) {
        //判断是否回复内容是否为空
        try {
          if (this.first_content.length > 0) {
            let { data } = await api.commentArticle("post", {
              parent_id: this.a_id,
              content: this.first_content
            });
            if (data.code === 110) {
              this.getReplyById(this.currentPage);
              this.$Notice.success({
                title: general.translate(data.code)
              });
              this.first_content = "";
            }
          }
        } catch (error) {
          this.$Notice.error({
            title: general.translate(error.data.code)
          });
        }
      }else {
        
      }
      // if (child) {
      //   this.placeholderString = `回复 @${child.reply_Name}`;
      //   parent.replyshow = true;
      // } else {
      //   this.placeholderString =
      //     "请自觉遵守互联网相关的政策法规，严禁发布色情、暴力、反动的言论。";
      //   for (let i of this.comLists) {
      //     i.replyshow = false;
      //   }
      //   if (this.nowReplyPerson === parent.userName) {
      //     this.nowReplyPerson = "";
      //     parent.replyshow = false;
      //   } else {
      //     this.nowReplyPerson = parent.userName;
      //     parent.replyshow = true;
      //   }
      // }
    },
    viewmore(parent) {
      //调用pagechange接口，去获得第一页面的数据
      parent.viewMore = true;
    },
    changepage(index) {
      //通过index去获取数据
      this.currentPage = index;
      this.getReplyById(this.currentPage);
    },
    async getReplyById(page) {
      try {
        let { data } = await api.commentArticle("get", this.a_id, page);
        this.comLists = data.comments;
        this.total = data.total;
        console.log("回复", data);
      } catch (error) {
        console.log(error);
      }
    }
  },
  mounted() {
    this.getReplyById(this.currentPage);
  }
};
</script>

<style lang="scss">
.no_reply {
  text-align: center;
}
.art-com {
  border: 1px solid #e1e1e1;
  background-color: #fff;
  padding: 20px;
  .more {
    font-size: 12px;
    color: #6d757a;
    b {
      font-size: 14px;
    }
    &-view {
      transition: all 0.5s ease;
      cursor: pointer;
      &:hover {
        color: $c-green;
      }
    }
  }
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
      transition: 0.1s;
      user-select: none;
      outline: none;
    }
  }
}
.comment-list {
  .commit-pageBox {
    padding: 20px;
  }
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
        font-size: 12px;
        // vertical-align: middle;
      }
      .text {
        padding-bottom: 4px;
      }
      .info {
        display: flex;
        span {
          margin-right: 0.5rem;
          display: flex;
        }
      }
      .reply {
        button {
          padding: 0;
        }
        &-box {
        }
        &-pageBox {
          li {
            a {
              font-size: 12px;
            }
          }
        }
        &-item {
          padding: 10px 0;
        }
        &-face {
          float: left;
          margin-top: 0;
        }
        &-text {
          font-weight: 400;
          font-size: 14px;
          line-height: 20px;
          word-wrap: break-word;
          overflow: hidden;
        }
        &-con {
          position: relative;
          margin-left: 2rem;
        }
        &-textarea {
          margin-left: 0;
          margin-top: 0.5rem;
        }
      }
    }
  }
}
</style>
