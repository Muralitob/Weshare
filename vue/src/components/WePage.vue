<template>
  <Page prev-text="上一页" next-text="下一页" v-if="item.viewMore" :total="40" size="small" class-name="pageBox"></Page>
</template>

<script>
export default {
  props: ['item']
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
