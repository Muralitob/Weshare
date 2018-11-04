<template>
  <shadow-card class="card" title="我的收藏">
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
    </div>
    <InfiniteLoading  direction="bottom" @infinite="handleReachBottom" spinner="waveDots">
      <span slot="no-more">
        没有更多数据了:)
      </span>
    </InfiniteLoading>
  </shadow-card>
</template>

<script>
import ShadowCard from "../../components/ShadowCard";
import InfiniteLoading from "vue-infinite-loading";
import MugenScroll from 'vue-mugen-scroll'
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
      api.collectionFun('get', 1, this.page, 5).then(({data})=> {
        if(data.collections.length) {
          this.collection_Array = this.collection_Array.concat(data.collections || {});
          this.page += 1;
          $state.loaded();
        }else {
          $state.complete();
        }
      }).catch(err => {
        console.log(err)
      })
    }
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
</style>
