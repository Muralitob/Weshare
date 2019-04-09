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
      <div class="base_ver">
        <Button v-if="!myuid" @click="GOTO(uid)" style="margin-left: 16px" icon="ios-call" slot="extra" type="primary">立即对话</Button>
      </div>
      <!-- <span class="report">举报</span> -->
    </div>
    <Card dis-hover class="used_con">
      <section class="used_title">
        <h3>{{good.title}}</h3>
        <!-- <span><Icon color="#F00303" type="md-heart-outline" />收藏</span> -->
      </section>
      <section class="used_top">
        <img class="used_img" :src="`data:image/png;base64,${good.pic[0].response.good_base64}`" alt="商品图片">
        <div class="used_info">
          <span>
            类型: {{good.type}}
          </span>
          <span>
            现价: ￥{{good.price}}
          </span>
          <span>
            交易区域: {{good.place || '面议'}}
          </span>
          <span>
            状态: {{good.status == 0?'在售': '已售出'}}
          </span>
          <!-- <span>
            联系方式: {{good.phone || '110'}}
          </span> -->
          <!-- <Button type="success" long>立即发出订单</Button> -->
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
import  usedTypeMap  from '../../constants/usedType.js'
export default {
  data() {
    return {
      // imgurl: "../../static/makalong.jpg",
      good_id: this.$route.params["used_id"],
      good: {},
      avatar: '',
      user_info: {},
      uid: 0,
      nickname: '',
      myuid:  this.$store.state.UserSetting.UserId
    };
  },
  methods: {
    fetchData(good_id) {
      api.getGoodContent(good_id).then(({data}) => {
        this.good = {
          price: data.good.price,
          place: data.good.place || '面议',
          desc: data.good.desc,
          pic: data.good.pic,
          user: data.good.user,
          release_time: data.good.release_time,
          type: usedTypeMap.usedTypeMap[data.good.type]
        }
        this.uid = data.good.user.uid
        this.nickname = data.good.user.nickname
        this.getUserInfo()
      })
    },
    GOTO(id) {
      // console.log('this.user_info.nickname', this.user_info.nickname)
      this.$router.push(`/talk/${id}/${this.nickname}`)
      // this.$router.push({name: 'talkpage', params: {userId: id, nickname: this.user_info.nickname}})
      // console.log(id);
    },
    getUserInfo() {
      api
        .getUserInfo(this.uid)
        .then(({ data }) => {
          let result = {
            nickname: data.nickname,
            sign: data.sign,
            uid: data.uid,
            avatar_url: data.avatar_url || "",
            branch: data.branch,
            attentioned: data.attentioned
          };
          this.user_info = result;
          console.log("用户信息", result);
        })
        .catch(err => {
          console.log(err);
        });
    },
  },
  created() {
    this.fetchData(this.good_id)
    // console.log(this.$store.state.UserSetting.UserId)
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
