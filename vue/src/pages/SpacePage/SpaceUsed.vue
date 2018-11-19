<template>
  <shadow-card class="card" title="我的记录">
    <div class="used_list">
      <Card dis-hover style="width: 46%;" v-for="(item,idx) in goodsList" :key="idx">
        <h2>{{item.title}}</h2>
        <span>20个人查看了该闲置</span>
        <section>
          <img src="../../assets/makalong.jpg" alt="">
          <div class="used_info">
            <span>
              类型: {{item.type}}
            </span>
            <span>
              现价: ￥{{item.price}}
            </span>
            <span>
              状态: {{item.status || '上架中'}}
            </span>
          </div>
        </section>
      </Card>
    </div>
    <InfiniteLoading direction="bottom" @infinite="handleReachBottom"  spinner="waveDots" >
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
import general from "../../general/js";
export default {
  components: { ShadowCard, InfiniteLoading },
  data() {
    return {
      goodsList: [],
      page: 1
    };
  },
  methods: {
    handleReachBottom($state) {
      api
        .getUsedList(this.page, 5)
        .then(({ data }) => {
          console.log(data);
          if (data.goods.length) {
            let result = Object.values(data.goods).map(ele => ({
              title: ele.title,
              type: general.translate(ele.type),
              price: ele.price,
              _id: ele._id
            }));
            this.goodsList = this.goodsList.concat(result);
            this.page += 1;
            $state.loaded();
          } else {
            $state.complete();
          }
        })
        .catch(err => {
          console.log(err);
        });
    }
  },
  mounted() {
    // this.fetchData(1)
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
.used_list {
  display: flex;
  flex-wrap: wrap;
  .ivu-card-body {
    flex: 1;
  }
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
    margin-left: 60px;
    display: flex;
    flex-direction: column;
    span {
      margin: 10px 0;
    }
  }
}
</style>
