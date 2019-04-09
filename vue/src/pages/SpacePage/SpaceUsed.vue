<template>
  <shadow-card class="card" title="我的闲置">
    <div class="used_list">
      <Card dis-hover style="width: 46%;" v-for="(item,idx) in goodsList" :key="idx">
        <h2>{{item.title}}</h2>
        <span>20个人查看了该闲置</span>
        <section>
          <img :src="item.pic" alt="">
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
        <Dropdown @on-click="function(name){action(name,item._id)}" trigger="click" class="goods-dropdown">
          <Button type="primary">
            操作
            <Icon type="ios-arrow-down"></Icon>
          </Button>
          <DropdownMenu slot="list" >
            <DropdownItem name="saleout" >售出</DropdownItem>
            <DropdownItem name="cancel" >取消</DropdownItem>
          </DropdownMenu>
        </Dropdown>
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
import  usedTypeMap  from '../../constants/usedType.js'
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
          if (data.goods.length) {
            let result = Object.values(data.goods).map(ele => ({
              title: ele.title,
              type: usedTypeMap.usedTypeMap[ele.type],
              price: ele.price,
              pic: `data:image/png;base64,${ele.pic[0].response.good_base64}`,
              _id: ele._id
            }));
            console.log(result)
            this.goodsList = this.goodsList.concat(result);
            this.page += 1;
            $state.loaded();
          } else {
            $state.complete();
          }
        })
        .catch(err => {
        });
    },
    action(name, _id) {
      if(name == 'saleout') {
        api.changeGoodStatus({_id}).then(({data}) => {
          if(data.code == 409) {
            this.$Message.sucess('操作成功')
          }
        }).catch((err) => {
          this.$Message.error('操作失败')
        });
      }else {
        let arr = []
        arr.push(_id)
        api.realeaseUsed('delete', {goods_list: arr}).then(({data}) => {
          if(data.code == 403) {
            this.$Message.sucess('删除成功')
          }
        }).catch((err) => {
          this.$Message.error('操作失败')
        });
      }
      this.handleReachBottom()
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
  .goods-dropdown {
    margin-top: 1rem;
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
