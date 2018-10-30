<template>
  <div id="app">
    <Header></Header>
    <vue-ins-progress-bar></vue-ins-progress-bar>
    <main class="wrapper">
      <router-view/>
    </main>
    <BackTop >
        <!-- <div class="totop">返回顶端</div> -->
    </BackTop>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from "./components/Heade";
import Footer from "./components/Footer";
export default {
  name: "App",
  components: { Header, Footer },
  created() {
    this.$insProgress.start();

    this.$router.beforeEach((to, from, next) => {
      this.$insProgress.start();
      next();
    });

    this.$router.afterEach((to, from) => {
      this.$insProgress.finish();
    });
  }
};
</script>


<style lang="scss">
@import "./scss/variable.scss";
@import "./scss/media-queries.scss";
body,
html {
  font-family: -apple-system, PingFang SC, Hiragino Sans GB, Microsoft YaHei,
    Helvetica Neue, Arial, sans-serif;
  @include tablet-min {
    background-color: $c-background;
  }
}
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-size: 16px;
  // transition: all .3s ease;
}
span {
  font-size: 12px;
}
ul,
li {
  list-style: none;
  margin: 0;
  padding: 0;
}
a {
  text-decoration: none;
  color: $c-dark;
  text-decoration: none;
}
.pl {
  @include mobile-only {
    padding-left: 10px;
  }
  @include tablet-min {
    padding-left: 30px;
  }
}
.pr {
  @include mobile-only {
    padding-right: 10px;
  }
  @include tablet-min {
    padding-right: 30px;
  }
}
.wrap {
  margin: 0 auto;
}
.wrapper {
  width: 100%;
  margin: 0 auto;
  @include firstMedia {
    width: $main-width;
  }
  @include secondMedia {
    width: $min-width;
  }
}
.borline {
  border-bottom: 1px dotted #bfbfbf;
  overflow: hidden;
  zoom: 1;
}
.col {
  display: flex;
  flex-direction: column;
}
main {
  flex: 1 0 auto;
  @include tablet-min {
    //  margin-top: 4.5rem;
    padding-top: 6.5rem;
  }
}
#app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
footer {
  flex: 0 0 auto;
}
header {
  flex: 0 0 auto;
}
.between {
  display: flex;
  justify-content: space-between;
}
.ivu-back-top-inner:hover {
  padding: 5px;
  background: $c-green;
  color: #fff;
  text-align: center;
  border-radius: 2px;
}
.box {
  position: relative;
  background-color: #fff;
  padding: 20px 0 20px 20px;
  border-radius: 3px;
  // box-shadow: 0px 2px 10px 0px rgba(0,0,0,0.1), 0 1px rgba(0,0,0,0.1);
}
.base_ver {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  margin: 0 1.5rem 0 1rem;
  text-align: center;
}
.base_title {
  font-size: 16px;
  color: #6A6A6A;
}
</style>
