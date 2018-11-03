<template>
  <div>
    <shadow-card class="card" title="我的文章">
      <div class="steam">
        <Row v-for="(item, index) in myArticle" :key="index"  class="steam-list">
          <section>
            <div class="favs bookmark-rank">
              0
              <span>收藏</span>
            </div>
            <Col>
              <router-link class="title" :to="{name: 'commentArticle', params: {com_id: item._id}}">
                {{item.article.title}}
              </router-link>
              <span>{{item.article.summary}}</span>
            </Col>
            <Col>
              <Time type="datetime" :time="item.update_time" />
            </Col>
          </section>
        </Row>
      </div>
      <div class="more" @click="routeTo('article')" v-if="myArticle.length>4"> 查看更多 </div>
    </shadow-card>
    <shadow-card class="card" title="我的收藏">
      <div class="steam">
        <Row v-for="(item, index) in myCollection" :key="index"  class="steam-list">
          <section>
            <div class="favs bookmark-rank">
              0
              <span>收藏</span>
            </div>
            <Col>
              <router-link to="/" class="author">
                {{item.author}}
              </router-link>
              <span>{{item.date}}</span>
            </Col>
            <Col>
              <router-link class="title" to="/">
                {{item.article_title}}
              </router-link>
            </Col>
          </section>
        </Row>
      </div>
      <div class="more" @click="routeTo('collection')" v-if="myCollection.length>4"> 查看更多 </div>
    </shadow-card>
    <shadow-card class="card" title="我的浏览记录">
      <div class="steam">
        <Row v-for="(item, index) in myHistory" :key="index"  class="steam-list">
          <section>
            <Col class="between">
              <router-link class="title" to="/">
                {{item.article_title}}
              </router-link>
              <div>
                <router-link to="/" class="author">
                  {{item.author}}
                </router-link>
                <span>{{item.date}}</span>
              </div>
            </Col>
          </section>
        </Row>
      </div>
      <div class="more" @click="routeTo('history')" >查看更多 </div>
    </shadow-card>
  </div>  
</template>

<script>
import ShadowCard from "../../components/ShadowCard";
import api from "../../api";
export default {
  components: { ShadowCard },
  data() {
    return {
      collection_Array: [],
      myArticle: [],
      myCollection: [],
      myHistory: [],
      visitUid: this.$route.params["userId"],
    };
  },
  methods: {
    routeTo(name) {
      this.$router.push({
        path: `/space/${this.$route.params.userId}/${name}`
      });
      this.$store.commit("Menu_SELECT", name);
    },
    fetchResult(type, page, limit) {
      if (type === "myArticle") {
        api
          .getArticles("real", page, limit)
          .then(({ data }) => {
            this.myArticle = data.articles;
          })
          .catch(err => {
            console.log(err);
          });
      } else if (type === "myCollection") {
      } else if (type === "myHistory") {
      }
    },
    fetchAll() {
      this.fetchResult("myArticle", 1, 5);
      this.fetchResult("myCollection", 1, 5);
      this.fetchResult("myHistory", 1, 5);
    }
  },
  mounted() {
    this.fetchAll();
  },
  computed: {
    IsSelf() {
      if(this.$cookie.get('uid')   === this.visitUid) {
        return true
      }else {
        return false
      }
    }
  },
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
</style>
