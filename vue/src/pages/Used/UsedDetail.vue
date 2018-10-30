<template>
  <div>
    <div class="used_seller box">
      <Avatar icon="ios-person" size="large" />
      <div class="base_ver">
        <span class="name">599y</span>
        <div><span>金牌卖家</span> </div>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">累计交易次数</span>
        <span>20</span>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">浏览数</span>
        <span>500</span>
      </div>
      <Divider type="vertical" />
      <div class="base_ver">
        <span class="base_title">闲置时间</span>
        <span>2018-10-20</span>
      </div>
      <Divider type="vertical" />
      <span class="report">举报</span>
    </div>
    <Card dis-hover class="used_con">
      <section class="used_title">
        <h3>二手马卡龙 刚刚买的 可好吃了 买多了 有带走的吗</h3>
        <span><Icon color="#F00303" type="md-heart-outline" />收藏</span>
      </section>
      <section class="used_top">
        <img class="used_img" src="../../static/makalong.jpg" alt="商品图片">
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
          其实也没什么好说的，大家都看到了，这是一个吃的呀对不对，你喜欢吃你就买咯，我保证好吃的，价格就是这个价格，这款是有点像冰激凌的，
          草莓味，凉凉的，放久了就不好吃了，快点来找我买下好吗，图书馆门口当面交易！不好吃你打我啊。
        </div>
      </section>
      <section class="used_imgcar" style="margin-top: 50px">
        <h3 class="used_title">物品详图</h3>
        <Carousel class="carousel" loop>
          <CarouselItem>
            <img class="used_img" src="../../static/makalong.jpg" alt="商品图片">
          </CarouselItem>
          <CarouselItem>
            <img class="used_img" src="../../static/makalong.jpg" alt="商品图片">
          </CarouselItem>
        </Carousel>
      </section>
    </Card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      imgurl: "../../static/makalong.jpg"
    };
  }
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
