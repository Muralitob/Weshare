<template>
  <shadow-card class="card" title="我的记录">
    <div class="steam">
      <Row v-for="(item, index) in collection_Array" :key="index"  class="steam-list">
        <section>
          <Col class="between">
            <router-link class="title" to="/">
              {{item.title}}
            </router-link>
            <div>
              <router-link to="/" class="author">
                {{item.author}}
              </router-link>
              <span><Time type="datetime" :time="item.time" /></span>
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
import api from '../../api';
export default {
  components: { ShadowCard, InfiniteLoading },
  data() {
    return {
      collection_Array: [
      ],
      currentPage: 1
    };
  },
  methods: {
    handleReachBottom($state) {
      $state.loaded();
      api
        .historyFunction("get", 0, this.currentPage)
        .then(({ data }) => {
          // console.log('history', data)
          let result = Object.values(data.article_history).map(ele=> ({
            title: ele.article.title,
            time: ele.update_time,
            _id: ele._id
          }))
          this.collection_Array = this.collection_Array.concat(result);
          // console.log(this.collection_Array)
          this.currentPage = this.currentPage + 1;
        })
        .catch(err => {
          console.log(err);
        });
      $state.complete();
    },
  },
  mounted () {
    // this.fetchData(1)
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
</style>
