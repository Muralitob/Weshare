<template>
  <Card class="b-profile-info row" shadow style="width: 960px">
    <p class="section-title" slot="title" >{{title}}</p>
    <a href="#" slot="extra">
      <span @click="edit">
        编辑
      </span>
    </a>
    <slot></slot>
  </Card>
</template>

<script>
export default {
  props: ["title"],
  methods: {
    edit() {
      this.$emit("editable", true);
    }
  }
};
</script>

<style lang="scss">
.section-title {
}
</style>
