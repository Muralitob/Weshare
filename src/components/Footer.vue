<template>
  <footer class="foot">
    <p>Copyright @ 2018 Weshare.（沪ICP备12026287号-1）</p>
    <p>为了更方便的大学生活</p>
  </footer>  
</template>

<script>
export default {

}
</script>

<style lang="scss">
  .foot{
    width: 100%;
    height: 6.5rem;
    background-color: $c-dark;
    margin-top: 4rem;
    padding-bottom: .445rem;
    color: $c-white;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    @include tablet-min{
      min-width: $min-width;
    }
    p{
      font-size: 13px;
      padding: 5px 0;
    }
  }
</style>
