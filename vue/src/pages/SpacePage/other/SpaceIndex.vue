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
          <Button  icon="md-add" slot="extra" type="primary">关注他</Button>
          <TabPane name="article" label="文章">
            <Card class="art_item" v-for="(item, idx) in articles" :key="idx">
              <router-link class="title" :to="{name: 'commentArticle', params: {com_id: item._id}}">
                <h2>{{item.article.title}}</h2>
              </router-link>
              <span>{{item.like_num}}个人赞了该文章</span>
              <span class="art_summary">
               {{item.article.summary}}
              </span>
            </Card>
            <InfiniteLoading @infinite="handleReachBottom" :distance='1000' direction="bootom" ref="infiniteLoading"  spinner="waveDots" >
              <span slot="no-more">
                没有更多数据了:)
              </span>
            </InfiniteLoading>
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
          <TabPane name="collection" label="收藏">
            <div class="steam">
              <Row v-for="(item, index) in collection_Array" :key="index"  class="steam-list">
                <section>
                  <div class="favs bookmark-rank">
                    0
                    <span>收藏</span>
                  </div>
                  <Col>
                    <router-link to="/" class="author">
                      {{item.article.nickname}}
                    </router-link>
                    <span>
                      <Time type="date" :time="item.update_time" />
                      {{item.date}}
                      </span>
                  </Col>
                  <Col>
                    <router-link class="title" to="/">
                      {{item.article.title}}
                    </router-link>
                  </Col>
                </section>
              </Row>
              <InfiniteLoading  direction="bottom" @infinite="handleReachBottom" spinner="waveDots">
                <span slot="no-more">
                  没有更多数据了:)
                </span>
              </InfiniteLoading>
            </div>
          </TabPane>
      </Tabs>
      <Card class="c-profile-info row" style="width:240px" dis-hover shadow>
        <Row>
          <Col span="12" class="col wrap" style="text-align:center">
              <div>
                <Icon type="md-eye" size="20" color="#23c9ed"  />
                <span>他的关注</span>
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
      <Card class="c-profile-info total row" style="width:240px" dis-hover shadow>
        <Row>
          <h3>个人资料</h3>
        </Row>
        <Row>
          <Icon type="md-school" />
          {{user_info.major}}
        </Row>
        <Row>
          <Icon type="logo-yen" />
          闲置物品2件
        </Row>
        <Row>
          <Icon type="md-create" />
          发表文章2篇
        </Row>
        <Row>
          <Icon type="md-star" />
          收藏内容2个
        </Row>
      </Card>
    </div>
  </div>

</template>

<script>
import api from "../../../api";
import InfiniteLoading from "vue-infinite-loading";
export default {
  components: { InfiniteLoading },
  data() {
    return {
      user_info: {},
      articles: [],
      collection_Array: [],
      uid: this.$route.params.userId,
      current: "article",
      art_page: 1,
      col_page: 1,
      used_page: 1
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
            avatar_url: data.avatar_url || "",
            major: data.major,
          };
          this.user_info = result;
          console.log("用户信息", data);
        })
        .catch(err => {
          console.log(err);
        });
    },
    fetch(name) {
      this.current = name;
      this.fetchResult(this.current, 1, 10);
    },
    fetchResult(type, page, limit) {
      if (type === "article") {
        api
          .getArticles("real", page, limit, this.uid)
          .then(({ data }) => {
            console.log(data);
            this.articles = data.articles;
          })

          .catch(err => {
            console.log(err);
          });
      } else if (type === "used") {
      } else if (type === "collection") {
        api
          .collectionFun("get", 1, page, limit, this.uid)
          .then(({ data }) => {
            console.log(data);
            this.myCollection = data.collections;
          })
          .catch(err => {
            console.log(err);
          });
      }
    },
    handleReachBottom($state) {
      if (this.current === "article") {
        api
          .getArticles("real", this.art_page, 3, this.uid)
          .then(({ data }) => {
            console.log(data);
            if (data.articles.length) {
              this.articles = this.articles.concat(data.articles || {});
              this.art_page += 1;
              $state.loaded();
            } else {
              $state.complete();
            }
          })
          .catch(err => {
            console.log(err);
          });
      } else if (this.current === "used") {
      } else if (this.current === "collection") {
        api
          .collectionFun("get", 1, this.col_page, 10, )
          .then(({ data }) => {
            if (data.collections.length) {
              this.collection_Array = this.collection_Array.concat(
                data.collections || {}
              );
              this.col_page += 1;
              $state.loaded();
            } else {
              $state.complete();
            }
          })
          .catch(err => {
            console.log(err);
          });
      }
    }
  },
  mounted() {
    this.getUserInfo();
    this.fetchResult("article", 1, 10);
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
  top: -48px;
  position: relative;
  .art_item {
    margin-bottom: 20px;
  }  
  .ivu-tabs-nav-container {
    padding: 0 0 0 20px;
  }
  .ivu-tabs-nav .ivu-tabs-tab {
    line-height: 40px;
  }
  .tab {
    // flex: 1;
  }
  .ivu-tabs-nav-right {
    line-height: 56px;
    margin-right: 20px;
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
  .total {
    position: absolute;
    right: 0;
    top: 180px;
    height: 200px;
    h3 {
      font-size:18px;
      font-family:MicrosoftYaHei-Bold;
      font-weight:bold;
      color:rgba(50,50,50,1);
    }
    .ivu-row {
      margin: 5px 0;
      display: flex;
      align-items: center;
      i {
        margin-right: 5px;
        font-size: 18px;
      }
    }
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
  .ivu-tabs-bar {
    background-color: #fff;
  }
  .used_list {
    img {
      width: 200px;
      height: 125px;
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
