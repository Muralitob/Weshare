<template>
  <div>
    <shadow-card class="card" title="我的收藏">
      <div class="steam">
        <Row v-for="(item, index) in collection_Array" :key="index"  class="steam-list">
          <section>
            <div class="favs bookmark-rank">
              1
              <small>收藏</small>
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
      <div class="more" > <a href="">查看更多</a> </div>
    </shadow-card>
    <shadow-card class="card" title="我的浏览记录">
      d
    </shadow-card>
  </div>  
</template>

<script>
import ShadowCard from "../../components/ShadowCard";
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
      ]
    };
  }
};
</script>

<style lang="scss">
  @import '../../scss/common.scss'
</style>
