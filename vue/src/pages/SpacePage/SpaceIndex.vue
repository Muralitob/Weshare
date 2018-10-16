<template>
  <div>
    <shadow-card class="card" title="我的文章">
      <div class="steam">
        <Row v-for="(item, index) in myArticle_Array" :key="index"  class="steam-list">
          <section>
            <div class="favs bookmark-rank">
              1
              <span>收藏</span>
            </div>
            <Col>
              <router-link class="title" to="/">
                {{item.article.title}}
              </router-link>
              <span>{{item.article.summary}}</span>
            </Col>
            <Col>
              <span>{{item.update_time}}</span>
            </Col>
          </section>
        </Row>
      </div>
      <div class="more" @click="routeTo('article')"> 查看更多 </div>
    </shadow-card>
    <shadow-card class="card" title="我的收藏">
      <div class="steam">
        <Row v-for="(item, index) in collection_Array" :key="index"  class="steam-list">
          <section>
            <div class="favs bookmark-rank">
              1
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
      <div class="more" @click="routeTo('collection')"> 查看更多 </div>
    </shadow-card>
    <shadow-card class="card" title="我的浏览记录">
      <div class="steam">
        <Row v-for="(item, index) in collection_Array" :key="index"  class="steam-list">
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
import api from '../../api';
export default {
  components: { ShadowCard },
  data() {
    return {
      collection_Array: [
        {
          article_title: "2019届校招前端面试题整理——HTML、CSS篇",
          date: "2018年10月10日",
          author: "ddduanlian"
        },
        {
          article_title: "2019年学期统计",
          date: "2018年10月10日",
          author: "ddduanlian"
        },
        {
          article_title: "2019年学期统计",
          date: "2018年10月10日",
          author: "ddduanlian"
        }
      ],
      myArticle_Array: []
    };
  },
  methods: {
    routeTo(name) {
      this.$router.push({path: `/space/${this.$route.params.userId}/${name}`});
      this.$store.commit('Menu_SELECT', name)
    },
    fetchResult(type){
      if(type === 'myArticle') {
        api.getArticles('real').then(({data}) => {
          this.myArticle_Array = data
        }).catch(err => {
          console.log(err);
        })
      }
    },
    fetchAll() {
      this.fetchResult('myArticle')
    }
  },
  mounted() {
    this.fetchAll()
  },
};
</script>

<style lang="scss">
  @import '../../scss/common.scss'
</style>
