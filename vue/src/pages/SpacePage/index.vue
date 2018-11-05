<template>
  <div>
    <component :is="current"></component>
  </div>
</template>

<script>
import OtherIndex from './other/SpaceIndex.vue'
import MyIndex from './MyIndex.vue'
export default {
  components:{
    OtherIndex,MyIndex
  },
  data() {
    return {
      // current: this.$store.state.UserSetting.currentComp,
    }
  },
  computed: {
    current() {
      return this.$store.state.UserSetting.currentComponent;
    }
  },
  watch: {
    // visitUid() {
    //   if(this.$cookie.get('uid') === this.visitUid) {
    //     console.log('一样')
    //     this.current = 'MyIndex'
    //   }else {
    //     this.current = 'OtherIndex'
    //   }
    // }
  },
  mounted() {
    
  },
}
</script>

<style>

</style>
