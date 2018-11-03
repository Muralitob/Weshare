<template>
  <shadow-card class="card" title="我的文章">
    <div class="steam">
      <Row v-for="item in myArticle" :key="item._id"  class="steam-list">
        <section>
          <div class="favs bookmark-rank">
            1
            <span>收藏</span>
          </div>
          <Col>
            <router-link to="/" class="author">
              {{item.author || 'Mura'}}
            </router-link>
            <span>{{item.update_time}}</span>
          </Col>
          <Col>
            <router-link class="title" :to="{name: 'commentArticle', params: {com_id: item._id}}">
              {{item.article.title}}
            </router-link>
          </Col>
          <Dropdown trigger="click">
            <a href="javascript:void(0)">
              <Icon type="ios-arrow-down"></Icon>
            </a>
            <DropdownMenu slot="list">
                <DropdownItem @click.native="edit(item._id)" name="edit">编辑</DropdownItem>
                <DropdownItem @click.native="del(item._id)" >删除</DropdownItem>
            </DropdownMenu>
          </Dropdown>
        </section>
      </Row>
    </div>
    <InfiniteLoading @infinite="handleReachBottom" :distance='1000' direction="bootom" ref="infiniteLoading"  spinner="waveDots" >
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
import general from "../../general/js";
import api from "../../api";
export default {
  components: { InfiniteLoading, editShadowCard, ShadowCard },
  data() {
    return {
      myArticle: [],
      page: 1
    };
  },
  methods: {
    handleReachBottom($state) {
      $state.loaded();
      api
        .getArticles("real", this.page, 10)
        .then(({ data }) => {
          // console.log(data);
          this.myArticle = this.myArticle.concat(data.articles || {});
          this.page = this.page + 1;
        })
        .catch(err => {
          console.log(err);
        });
      $state.complete();
    },
    articleAction(name) {
      if (name === "edit") {
      } else if (name === "delete") {
      }
    },
    edit(_id) {
      console.log(_id);
    },
    del(_id) {
      this.$Modal.confirm({
        title: "确认",
        content: "<p>你确定删除这篇文章吗?</p>",
        onOk: () => {
          api.deleteArticles([_id]).then(({ data }) => {
            if (data.code === 108) {
              this.$Notice.success({
                title: general.translate(data.code),
                desc: "您所选文章已被删除"
              });
              var arr = [];
              [_id].forEach(element => {
                arr = this.myArticle.filter((item, index) => {
                  return item._id !== element;
                });
              });
              this.myArticle = arr;
            }
          });
        }
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
