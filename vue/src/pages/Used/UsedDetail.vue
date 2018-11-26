<template>
  <div>
    <div class="used_seller box">
      <Avatar icon="ios-person" size="large" :src="`data:image/png;base64,${good.user.avatar_base64}`" />
      <div class="base_ver">
        <span class="name">{{good.user.nickname}}</span>
        <div><span>金牌卖家</span> </div>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">累计交易次数</span>
        <span>0</span>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">浏览数</span>
        <span>0</span>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">闲置时间</span>
        <Time type="date" :time="good.release_time"></Time>
      </div>
      <Divider type="vertical" />
      <span class="report">举报</span>
    </div>
    <Card dis-hover class="used_con">
      <section class="used_title">
        <h3>{{good.title}}</h3>
        <span><Icon color="#F00303" type="md-heart-outline" />收藏</span>
      </section>
      <section class="used_top">
        <img class="used_img" :src="`data:image/png;base64,${good.pic[0].response.good_base64}`" alt="商品图片">
        <div class="used_info">
          <span>
            类型: 食品
          </span>
          <span>
            现价: ￥50
          </span>
          <span>
            交易区域: 图书馆门口
          </span>
          <span>
            联系方式: 110
          </span>
          <Button type="success" long>立即发出订单</Button>
        </div>
      </section>
      <section>
        <h3 class="used_title">物品详细</h3>
        <div class="used_desc">
          {{good.desc}}
        </div>
      </section>
      <section class="used_imgcar" style="margin-top: 50px">
        <h3 class="used_title">物品详图</h3>
        <Carousel class="carousel" loop>
          <CarouselItem v-for="(item, index) in good.pic" :key="index">
            <img class="used_img" :src="`data:image/png;base64,${item.response.good_base64}`" alt="商品图片">
          </CarouselItem>
        </Carousel>
      </section>
    </Card>
  </div>
</template>

<script>
import api from '../../api'
export default {
  data() {
    return {
      imgurl: "../../static/makalong.jpg",
      good_id: this.$route.params["used_id"],
      good: {}
    };
  },
  methods: {
    fetchData(good_id) {
      api.getGoodContent(good_id).then(({data}) => {
        this.good = data.good
      })
    }
  },
  mounted() {
    this.fetchData(this.good_id)
  },
};
</script>

<style lang="scss">
.box {
  border: 1px solid rgba(210, 210, 210, 1);
  border-top: 5px solid $c-green;
}
.carousel {
  width: 800px;
  margin: 0 auto;
  img {
    width: 100%;
  }
}
.used {
  &_title {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
    border-left: 5px solid $c-green;
    margin-bottom: 32px;
  }
  &_imgcar {
  }
  &_img {
    width: 608px;
    height: 362px;
  }
  &_info {
    display: flex;
    flex-direction: column;
    // justify-content: space-around;
    margin-left: 105px;
    span {
      display: block;
      font-size: 16px;
      font-weight: 400;
      margin-bottom: 40px;
    }
    button {
      span {
        margin: 0;
      }
    }
  }
  &_top {
    display: flex;
    margin-bottom: 50px;
  }
}
.used_seller {
  display: flex;
  margin-bottom: 50px;
  .base_title + span {
    font-size: 14px;
    font-weight: 400;
    color: rgba(50, 50, 50, 1);
  }
  .report {
    position: absolute;
    right: 20px;
  }
}
.ivu-divider-vertical {
  height: 40px;
}
.used_con {
  min-height: 50rem;
}
</style>
