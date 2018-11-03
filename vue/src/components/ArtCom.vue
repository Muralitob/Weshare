<template>
  <div class="art-com">
    <div id="news-header">
      <h1 class="header-title">评论</h1>
      <p class="header-protocol">文明上网理性发言</p>
      <p class="header-number">{{total}}条评论</p>
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
      <Spin size="large" fix v-if="spinShow"></Spin>
      <div class="list-item" v-for="(parent, idx) in comLists" :key="idx">
        <div class="user-face">
          <Avatar icon="ios-person" size="large"  />
        </div>
        <div class="con">
          <router-link to="" class="user-name" >
            {{parent.name}}
          </router-link>
          <p class="text">{{parent.content}}</p>
          <div class="info">
            <span>#{{parent.floor}}</span>
            <Time :time="parent.comment_time" />
            <span class="like">
              <Icon class="like_btn" type="md-thumbs-up" v-if="!parent.is_like" @click="isLike(+1, parent)" />
              <Icon class="like_btn" type="md-thumbs-up" v-else @click="isLike(-1, parent)"  color="#01af63" />
              {{parent.like_num}}
            </span>
            <span class="reply"><Button type="text" @click="reply(parent)">回复</Button></span>
          </div>
          <div class="reply-box">
            <div class="reply-item" v-for="(child, idx) in parent.comments" :key="idx">
              <Avatar icon="ios-person" size="small" class="reply-face" />
              <div class="reply-con">
                <router-link to="" class="user-name" >
                  {{child.name}}
                </router-link>
                <span class="reply-text">{{child.content}}</span>
                <div class="info">
                  <Time  :time="child.comment_time" />
                  <span class="like">
                    <Icon class="like_btn" type="md-thumbs-up" v-if="!child.is_like" @click="isLike(+1, child)" />
                    <Icon class="like_btn" type="md-thumbs-up" v-else color="#01af63" @click="isLike(-1, child)" />
                    {{child.like_num}}
                  </span>
                </div>
              </div>
            </div>
            <Page prev-text="上一页" next-text="下一页" @on-change="changepage" v-if="parent.viewMore" :total="40" size="small" class-name="reply-pageBox"></Page>
            <!-- <we-page :item="parent" ></we-page> -->
            <div class="more" v-if="parent.comments.length>3&&!parent.viewMore">共有<b>{{parent.replyNums}}</b>条回复<Icon @click="viewmore(parent)" size='28' type="md-arrow-dropdown" class="more-view"/></div>
            <div class="box-textarea reply-textarea" v-if="parent.replyshow">
              <Input v-model="second_content" :cols=80 :rows=2  type="textarea" :placeholder='placeholderString' />
              <button class="box-post" @click="reply(parent)">发表评论</button>
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
import VueStar from 'vue-star'
export default {
  props: ["list"],
  components: {
    VueStar
  },
  data() {
    return {
      comLists: [],
      placeholderString: "回复:",
      nowReplyPerson: "",
      first_content: "",
      second_content: "",
      a_id: this.$route.params["com_id"],
      total: 0,
      currentPage: 1,
      spinShow: false,
    };
  },
  methods: {
    async reply(parent) {
      if (parent.is_first_comment) {
        //二级评论
        parent.replyshow = !parent.replyshow;
        this.placeholderString = `回复: ${parent.name}`;
        try {
          if (this.second_content.length > 0) {
            let { data } = await api.commentArticle("post", {
              parent_id: parent._id,
              content: this.second_content
            });
            if (data.code === 110) {
              this.getReplyById(this.currentPage);
              this.$Notice.success({
                title: general.translate(data.code)
              });
              this.second_content = "";
            }
          }
        } catch (error) {
          this.$Notice.error({
            title: general.translate(error.data.code)
          });
        }
      } else {
        //主级评论
        //判断是否回复内容是否为空
        try {
          if (this.first_content.length > 0) {
            let { data } = await api.commentArticle("post", {
              parent_id: this.a_id,
              content: this.first_content
            });
            if (data.code === 110) {
              //给每个一级评论加上字段
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
      this.spinShow = true
      try {
        let { data } = await api.commentArticle("get", this.a_id, page);
        let result = Object.values(data.comments).map((ele, idx) => {
          return {
            ...ele,
            viewMore: false,
            replyshow: false,
            floor: data.total - ((this.currentPage - 1) * 10 + idx)
          };
        });
        this.comLists = result;
        this.total = data.total;
        this.spinShow = false
      } catch (error) {
        console.log(error);
      }
    },
    async isLike(add, obj) {
      try {
        let {data} = await api.addLikeComment(add,obj._id)
        if(add===1) {
          obj.like_num++;
        }else if(add === -1) {
          obj.like_num--;
        }
        obj.is_like = !obj.is_like
      } catch (error) {
        console.log('点赞error', error);
      }
    }
  },
  mounted() {
    this.getReplyById(this.currentPage);
  }
};
</script>

<style lang="scss">
.like_btn {
  cursor: pointer;
}
.no_reply {
  text-align: center;
}
.art-com {
  border: 1px solid #e1e1e1;
  background-color: #fff;
  padding: 20px;
  .VueStar {
    position: relative;
    .VueStar__ground {
      width: 16px;
      height: 16px;
      .VueStar__icon {
        display: flex;
        align-items: center;
      }
      .VueStar__decoration {
        // background-position: center center;
        width: 100px;
        height: 100px;
        left: -40px;
        top: -40px;
      }
    }
  }
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
