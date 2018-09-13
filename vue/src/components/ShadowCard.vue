<template>
  <Card class="b-profile-info row" shadow style="width: 960px">
    <p class="section-title"  slot="title" >{{title}}</p>
    <slot></slot>
  </Card>
</template>

<script>
export default {
  props: ['title']
}
</script>

<style lang="scss">
  .section-title {
  }
</style>
