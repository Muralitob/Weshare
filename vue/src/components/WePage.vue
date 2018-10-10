<template>
  <Page prev-text="上一页" next-text="下一页" v-if="item.viewMore" :total="40" size="small" class-name="pageBox" @on-change="changePage" ></Page>
</template>

<script>
export default {
  props: ['item','url'],
  data(){
    return {
      pageTotal: '',
      pageNum: 0,
      pageSize: 10,
    }
  },
  methods: {
    changePage(index) {
      let data = 1;
      this.$emit("returnData", data)
    }
  }
};
</script>

<style lang="scss">
.pageBox {
  li {
    a {
      font-size: 12px;
    }
  }
}
</style>
