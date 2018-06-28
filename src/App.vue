<template>
  <div id="app">
    <Header></Header>
    <main class="wrapper">
      <router-view/>
    </main>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from './components/Heade';
import Footer from './components/Footer';
export default {
  name: 'App',
  components: { Header, Footer }
}
</script>


<style lang="scss">
@import './scss/variable.scss';
@import './scss/media-queries.scss';
body,html{
  font-family: -apple-system,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Helvetica Neue,Arial,sans-serif;
  @include tablet-min{
    background-color: $c-background;
  }
}
*{
  font-size: 16px;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  // transition: all .3s ease;
}
ul,li{
  list-style: none;
  margin: 0;
  padding: 0;
}
a{
  text-decoration: none;
  color: $c-dark;
  text-decoration: none;
}
.pl{
  @include mobile-only{
    padding-left: 10px
  }
  @include tablet-min{
    padding-left: 30px;
  }
}
.pr{
  @include mobile-only{
    padding-right: 10px
  }
  @include tablet-min{
    padding-right: 30px;
  }
}
.wrapper{
  width: 100%;
  margin: 0 auto;
  @include firstMedia{
    width: $main-width;
  }
  @include secondMedia {
    width: $min-width;
  }
}
.borline{
  border-bottom: 1px dotted #BFBFBF;
  overflow: hidden;
  zoom: 1;
}
main{
  flex: 1 0 auto;
  @include tablet-min{
    position: static;
    padding-top: 2rem;
  }
}
#app{
  display: flex;
  flex-direction: column;
  height: 100vh;
}
footer{
  flex: 0 0 auto;
}
header{
  flex: 0 0 auto;
}
</style>
