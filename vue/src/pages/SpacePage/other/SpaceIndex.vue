<template>
  <div>
    <div class="h">
      <div class="h-inner">
        <div class="h-gradient"></div>
        <div class="h-user">
          <div class="h-info">
            <Avatar :src='user_info.avatar_url' class="avatar" />
            <div class="h-basic">
              <div class="h-name">
                {{user_info.nickname}}
              </div>
              <div class="h-basic-spacing">
                <span>
                  {{user_info.sign}}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="c">
      <Tabs value="article" @on-click="fetch" class="tab" :animated="false">
          <TabPane name="article" label="文章">
            <Card class="art_item">
              <h2>2019届校招面试题整理</h2>
              <span>20个人赞了该文章</span>
              <span class="art_summary">
                我们除了文字外形基本上是个希腊化的国家，正在变得现代化并有了一代真正的现代人。 
                所谓复兴汉服没有任何意义。我们满脑子所谓自由平等民主，我们满脑子所谓自由平等
                民主我们满脑子所谓自由平等民主我们满脑子所谓自由平等民主...
              </span>
            </Card>
          </TabPane>
          <TabPane name="used" label="闲置">
            <div class="used_list">
              <Card style="width: 48%;">
                <h2>二手马卡龙</h2>
                <span>20个人查看了该闲置</span>
                <section>
                  <img src="../../../assets/makalong.jpg" alt="">
                  <div class="used_info">
                    <span>
                      类型: 食品
                    </span>
                    <span>
                      现价: ￥50
                    </span>
                    <span>
                      状态: 已售出
                    </span>
                  </div>
                </section>
              </Card>
              <Card style="width: 48%;">
                <h2>二手马卡龙</h2>
                <span>20个人查看了该闲置</span>
                <section>
                  <img src="../../../assets/makalong.jpg" alt="">
                  <div class="used_info">
                    <span>
                      类型: 食品
                    </span>
                    <span>
                      现价: ￥50
                    </span>
                    <span>
                      状态: 已售出
                    </span>
                  </div>
                </section>
              </Card>
              <Card style="width: 48%;">
                <h2>二手马卡龙</h2>
                <span>20个人查看了该闲置</span>
                <section>
                  <img src="../../../assets/makalong.jpg" alt="">
                  <div class="used_info">
                    <span>
                      类型: 食品
                    </span>
                    <span>
                      现价: ￥50
                    </span>
                    <span>
                      状态: 已售出
                    </span>
                  </div>
                </section>
              </Card>
            </div>
          </TabPane>
          <TabPane name="collection" label="收藏">收藏</TabPane>
      </Tabs>
      <Card class="c-profile-info row" style="width:240px" dis-hover shadow>
        <Row>
          <Col span="12" class="col wrap" style="text-align:center">
              <div>
                <Icon type="md-eye" size="20" color="#23c9ed"  />
                <span>我的关注</span>
              </div>
              <span>0</span>
          </Col>
          <Col span="12" class="col wrap" style="text-align:center">
              <div>
                <Icon type="md-heart" size="20" color="#ff5d47" />
                <span>粉丝人数</span>
              </div>
              <span>0</span>
          </Col>
        </Row>
      </Card>
    </div>
  </div>

</template>

<script>
import api from "../../../api";
export default {
  data() {
    return {
      user_info: {},
      articles: [],
      uid: this.$route.params.userId
    };
  },
  methods: {
    getUserInfo() {
      api
        .getUserInfo(this.uid)
        .then(({ data }) => {
          let result = {
            nickname: data.nickname,
            sign: data.sign,
            avatar_url: data.avatar_url || ""
          };
          this.user_info = result;
          console.log("用户信息", data);
        })
        .catch(err => {
          console.log(err);
        });
    },
    fetch(name) {
      this.fetchResult(name, 1, 10);
    },
    fetchResult(type, page, limit,) {
      if (type === "article") {
        api
          .getArticles("real", page, limit, this.uid)
          .then(({ data }) => {
            this.myArticle = data.articles;
          })
          .catch(err => {
            console.log(err);
          });
      } else if (type === "used") {
        // api
        //   .collectionFun("get", 1, page, limit, this.uid)
        //   .then(({ data }) => {
        //     this.myCollection = data.collections;
        //   })
        //   .catch(err => {
        //     console.log(err);
        //   });
      } else if (type === "collection") {
        api
          .historyFunction("get", 1, page, limit, this.uid)
          .then(({ data }) => {
            this.myHistory = data.article_history;
          })
          .catch(err => {
            console.log(err);
          });
      }
    }
  },
  mounted() {
    this.getUserInfo();
  }
};
</script>

<style lang="scss">
.h {
  top: -3rem;
  position: relative;
  height: 12.5rem;
  @include firstMedia {
    width: $main-width;
  }
  @include secondMedia {
    width: $min-width;
  }
  &-inner {
    background-image: url("../../../assets/bg2.jpg");
    background-position: 50%;
    background-size: cover;
    padding-top: 7.5rem;
  }
  &-user {
    position: relative;
    z-index: 1;
    color: $c-light;
  }
  &-basic {
    margin: 10px 0 0 20px;
  }
  &-name {
    font-size: 18px;
  }
  &-basic-spacing {
    font-size: 12px;
    color: #d6dee4;
  }
  &-gradient {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 5rem;
    background-image: url("../../../assets/shadow.png");
    background-repeat: repeat-x;
  }
  &-info {
    width: 100%;
    margin-left: 2rem;
    padding-bottom: 1rem;
    display: flex;
    .avatar {
      width: 4rem;
      height: 4rem;
      border-radius: 50%;
    }
  }
}
.c {
  // display: flex;
  position: relative;
  .ivu-tabs-nav-container {
    background-color: #fff;
    padding: 0 0 0 20px;
  }
  .ivu-tabs-nav .ivu-tabs-tab {
    line-height: 40px;
  }
  .tab {
    // flex: 1;
  }
  .ivu-tabs-content {
    width: 1000px;
  }
  &-profile-info {
    position: absolute;
    right: 0;
    top: 72px;
    height: 80px;
  }
  .used_list {
    display: flex;
    flex-wrap: wrap;
    .ivu-card-body {
      flex: 1;
    }
  }
  .ivu-card-body {
    display: flex;
    flex-direction: column;
    span {
      display: inline-block;
      margin: 5px 0;
    }
    .art_summary {
      font-size: 18px;
      width: 700px;
      text-align: justify;
    }
  }
  .used_list {
    img {
      width:200px;
      height:125px;
    }
    section {
      display: flex;
      align-items: center;
      // justify-content: space-between;
    }
    .ivu-card {
      margin-right: 20px;
      margin-bottom: 20px;
      .ivu-card-body {
        padding: 25px;
      }
    }
    .used_info {
      margin-left: 80px;
    }
  }
}
</style>
