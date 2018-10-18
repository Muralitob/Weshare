<template>
  <shadow-card class="card" title="我的文章">
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
          <Dropdown trigger="click">
            <a href="javascript:void(0)">
              <Icon type="ios-arrow-down"></Icon>
            </a>
            <DropdownMenu slot="list">
                <DropdownItem>编辑</DropdownItem>
                <DropdownItem>删除</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </section>
      </Row>
    </div>
    <InfiniteLoading :on-infinite="handleReachBottom" ref="infiniteLoading"  spinner="waveDots" >
      <span slot="no-more">
        没有更多数据了:)
      </span>
    </InfiniteLoading>
  </shadow-card>
</template>

<script>
import editShadowCard from "../../components/editShadowCard";
import ShadowCard from "../../components/ShadowCard";
import InfiniteLoading from "vue-infinite-loading";
export default {
  components: { InfiniteLoading, editShadowCard, ShadowCard },
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
  },
  methods: {
    handleReachBottom() {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          this.$refs.infiniteLoading.$emit("$InfiniteLoading:loaded");
          const last = this.collection_Array[this.collection_Array.length - 1];
          for (let i = 1; i < 11; i++) {
            this.collection_Array.push(last + i);
          }
          this.$refs.infiniteLoading.$emit("$InfiniteLoading:complete");
          resolve();
        }, 2000);
      });
    }
  }
};
</script>

<style lang="scss">
@import "../../scss/common.scss";
.steam-list {
  section {
  }
  .ivu-col + .ivu-dropdown {
    position: absolute;
    right: 1rem;
    top: 1.1rem;
  }
  .ivu-dropdown-item:nth-child(2) {
    color: #ff371e;
  }
}
</style>
