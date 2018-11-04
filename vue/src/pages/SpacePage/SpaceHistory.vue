<template>
  <shadow-card class="card" title="我的记录">
    <div class="steam">
      <Row v-for="(item, index) in history_Array" :key="index"  class="steam-list">
        <section>
          <Col class="between">
            <router-link class="title" to="/">
              {{item.title}}
            </router-link>
            <div>
              <router-link to="/" class="author">
                {{item.nickname}}
              </router-link>
              <span><Time type="date" :time="item.time" /></span>
            </div>
          </Col>
        </section>
      </Row>
    </div>
    <InfiniteLoading @infinite="handleReachBottom"  spinner="waveDots" >
      <span slot="no-more">
        没有更多数据了:)
      </span>
    </InfiniteLoading>
  </shadow-card>
</template>

<script>
import ShadowCard from "../../components/ShadowCard";
import InfiniteLoading from "vue-infinite-loading";
import api from "../../api";
export default {
  components: { ShadowCard, InfiniteLoading },
  data() {
    return {
      history_Array: [],
      currentPage: 1
    };
  },
  methods: {
    handleReachBottom($state) {
      $state.loaded();
      api
        .historyFunction("get", 0, this.currentPage)
        .then(({ data }) => {
          if (data.article_history.length) {
            let result = Object.values(data.article_history).map(ele => ({
              title: ele.article.title,
              time: ele.update_time,
              nickname: ele.article.nickname,
              _id: ele._id
            }));
            this.history_Array = this.history_Array.concat(result);
            this.currentPage = this.currentPage + 1;
            $state.loaded();
          } else {
            $state.complete();
          }
        })
        .catch(err => {
          console.log(err);
        });
      $state.complete();
    }
  },
  mounted() {
    // this.fetchData(1)
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
</style>
