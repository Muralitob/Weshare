<template>
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
    <InfiniteLoading  @infinite="handleReachBottom" :distance='1000' direction="bootom" ref="infiniteLoading"  spinner="waveDots" >
      <span slot="no-more">
        没有更多数据了:)
      </span>
    </InfiniteLoading>
  </shadow-card>
</template>

<script>
import ShadowCard from "../../components/ShadowCard";
import InfiniteLoading from "vue-infinite-loading";
import api from '../../api'
export default {
  components: { ShadowCard, InfiniteLoading },
  data() {
    return {
      collection_Array: [
      ],
      page: 1,
    };
  },
  methods: {
    handleReachBottom($state) {
      $state.loaded();
      api.collectionFun('get', 1, 10).then(({data})=> {
        console.log(data)
      })
      $state.complete();
    }
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
</style>
