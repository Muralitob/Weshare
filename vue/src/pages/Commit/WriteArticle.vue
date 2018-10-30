<template>
  <div id="text-contribute">
      <Tabs :value="activeTab" animated @on-click="getDrafts">
        <TabPane name="edit" label="文章投稿">
          <Input v-model="article.title" size="large" placeholder="请输入标题" />
          <Editor v-model="article.content" @summary="returnSummary" ></Editor>
          <div class="block-wrap">
            <h3 class="block-title">
              <p>添加标签</p>
              <span class="tip">{{(`还可以添加${restCount}个标签`)}}</span>
            </h3>
            <div class="tag-wrap">
              <Tag color="primary" v-for="item in tagLists" :key="item" :name="item" closable @on-close="colseTag">{{item}}</Tag>
              <Input @on-enter="addTag" :maxlength=8 clearable style="width: 100px" v-model="inputTag" />
              <span>按回车键添加</span>
            </div>
          </div>
          <div class="btn-bar">
            <Button class="handleArticle" type="success" @click="handleArticle('real')">提交文章</Button>
            <Button class="handleArticle" type="warning" @click="handleArticle('fake')">存入草稿</Button>
          </div>
        </TabPane>
        <TabPane label="草稿箱" name="drafts">
          <div class="draft-card" v-for="item in draftsList" :key="item._id">
            <div class="meta-wrap">
              <div class="meta-title"><h3>{{item.article.title}}</h3></div>
              <p class="meta-summary">
                {{item.article.summary}}
              </p>
              <div class="meta-status"><span>{{item.update_time}}</span></div>
              <div class="meta-action">
                <Button type="primary" @click="editDraft(item._id)">编辑</Button>
                <Button @click="deleteDrafts([item._id])">删除</Button>
              </div>
            </div>
          </div>
          <Page prev-text="上一页" next-text="下一页" @on-change="changepage" :total="total" show-elevator class-name="draft-pageBox"></Page>
        </TabPane>
    </Tabs>
  </div>
</template>

<script>
import Editor from "../../components/Editor";
import general from "../../general/js";
import api from "../../api";
export default {
  components: {
    Editor
  },
  data() {
    return {
      article: {
        content: "",
        summary: "",
        title: ""
      }, //文章
      draftsList: [],
      activeTab: "",
      tagLists: [], //标签
      inputTag: "",
      total: 0
    };
  },
  computed: {
    restCount() {
      return 10 - this.tagLists.length;
    }
  },
  methods: {
    reciveContent(content) {
      // console.log(content)
    },
    addTag() {
      if (this.inputTag) {
        this.tagLists.push(this.inputTag);
      }
      this.tagLists = [...new Set(this.tagLists)];
      this.inputTag = "";
    },
    colseTag(event, name) {
      const index = this.tagLists.indexOf(name);
      this.tagLists.splice(index, 1);
    },
    handleArticle(category) {
      api
        .handleArticle({
          article: this.article,
          tagLists: this.tagLists,
          category
        })
        .then(({ data }) => {
          this.$Message.success(general.translate(data.code));
        })
        .catch(err => {
          this.$Message.error(general.translate(err.code));
        });
    },
    changepage(index) {
      this.getDrafts("drafts", index);
    },
    getDrafts(name) {
      this.activeTab = name
      if (name === "drafts") {
        api
          .getArticles("fake", 1)
          .then(({ data }) => {
            this.draftsList = data.articles;
            console.log(this.draftsList);
            this.total = data.length;
          })
          .catch(err => {
            this.$Message.error(general.translate(data.code));
          });
      }
    },
    async deleteDrafts(idList) {
      api
        .deleteArticles(idList)
        .then(({ data }) => {
          //如果成功,在现有的数组上删除该条数据，并提醒删除成功
          this.$Notice.success({
            title: general.translate(data.code),
            desc: "您所选文章已被删除"
          });
          let draftsList = this.draftsList;
          var arr = [];
          idList.forEach(element => {
            arr = draftsList.filter((item, index) => {
              return item._id !== element;
            });
          });
          this.draftsList = arr;
        })
        .catch(err => {
          this.$Notice.error({
            title: general.translate(data.code),
            desc: "有问题啦"
          });
        });
    },
    returnSummary(data) {
      this.article.summary = data;
    },
    async editDraft(id) {
      // console.log(this.activeTab)
      this.activeTab = "edit";
      try {
        let { data } = await api.getArticleById(id);
        this.article = data.articles.article
        this.tagLists = data.articles.tagLists
        console.log(data);
      } catch (error) {
        console.log(error);
      }
    }
  },
  updated() {
    // console.log(this.article)
  }
};
</script>

<style lang="scss">
#text-contribute {
  position: relative;
}
.handleArticle {
  /* position: absolute;
    bottom: 0; */
}
.draft-pageBox {
  padding: 20px 20px;
  background-color: #fff;
}
.btn-bar {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
  button {
    margin: 0 20px;
  }
}
.block-wrap {
  margin: 20px 0;
}
.block-title {
  display: flex;
  align-items: center;
  padding: 6px 0;
  span {
    color: #99a2aa;
    padding-left: 8px;
  }
}
.tag-wrap {
  span {
    color: #99a2aa;
    padding-left: 8px;
  }
}
.draft-card {
  background-color: #fff;
  height: 12rem;
  padding: 20px;
  box-shadow: 0 0 2px rgba(0, 0, 0, 0.2);
  .meta-wrap {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .meta-summary {
    font-size: 14px;
    line-height: 20px;
    color: #99a2aa;
    padding: 5px 0 10px;
    word-wrap: break-word;
    word-break: break-word;
    text-overflow: ellipsis;
    overflow: hidden;
  }
  p {
    color: #99a2aa;
  }
}
</style>
