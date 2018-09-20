<template>
  <div id="text-contribute">
    <Editor v-model="article.content" ></Editor>
    <Button class="handleArticle" type="warning">提交文章</Button>
  </div>
</template>

<script>
import Editor from '../../components/Editor'
export default {
  components: {
    Editor,
  },
  data() {
    return {
      article: {
        content: '',
        UserId: this.$store.state.UserSetting.UserId,
      }
    }
  },
  methods: {
    reciveContent(content) {
      // console.log(content)
    }
  },
  updated() {
    console.log(this.article)
  },
}
</script>

<style>
  #text-contribute {
    position: relative;
  }
  .handleArticle {
    /* position: absolute;
    bottom: 0; */
  }
</style>
