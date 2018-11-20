<template>
  <div class="user_home">
    <div class="cutarea">
      <section>
        <div>
          <span>类别:</span>
          <Select clearable  v-model="type" style="width:150px">
            <Option v-for="item in usedType" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </div>
        <div>
          <span>新旧程度:</span>
          <Select clearable  v-model="oldandnew" style="width:120px">
            <Option v-for="item in degree" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </div>
      </section>
      <section class="release">
        <router-link to="/used/release">
          发布闲置
          <Icon size="26" type="md-arrow-dropright" />
        </router-link>
        </section>
    </div>
    <div class="con">
      <ul class="u_list">
        <li class="u_item" v-for="(item, idx) in used_info" :key="idx">
          <article>
            <Time class="u_time" :time="item.release_time" type="date"></Time>
            <router-link :to="{path: `/used/${item._id}`}"><p class="u_tname">{{item.title}}</p></router-link>
            <p class="u_name">{{item.nickname || '0'}}<span> - ￥{{item.price}}</span></p>
          </article>
        </li>
      <Page prev-text="上一页" next-text="下一页" @on-change="changepage" :total="total" show-elevator class-name="used-pageBox"></Page>
      </ul>
      <section>
        最新成交
      </section>
    </div>
  </div>
</template>

<script>
import used from "../../constants/usedType.js";
import api from "../../api";
export default {
  data() {
    return {
      usedType: used.usedType,
      degree: [
        {
          value: "0",
          label: "全新"
        },
        {
          value: "9",
          label: "九成新"
        },
        {
          value: "8",
          label: "八成新"
        },
        {
          value: "7",
          label: "七成新"
        },
        {
          value: "6",
          label: "六成新"
        },
        {
          value: "5",
          label: "五成新及以下"
        }
      ],
      type: "",
      oldandnew: "",
      used_info: [
        {
          release_time: "10月21号",
          release_thingname: "自用九成新ipad",
          user_name: "张三",
          price: 42
        },
        {
          release_time: "10月21号",
          release_thingname: "自用九成新ipad",
          user_name: "张三",
          price: 42
        }
      ],
      total: 0
    };
  },
  methods: {
    changepage() {},
    async fetchResult(page) {
      api.getUsedList(page, 10).then(({ data }) => {
        let result = Object.values(data.goods).map(item => ({
          release_time: item.release_time,
          nickname: item.user.nickname,
          title: item.title,
          price: item.price
        }));
        this.used_info = result;
        this.total = data.total;
        console.log(data);
      });
    }
  },
  mounted() {
    this.fetchResult(1);
  }
};
</script>

<style lang="scss">
.cutarea {
  display: flex;
  width: 100%;
  background-color: #fff;
  height: 70px;
  margin-bottom: 50px;
  border-radius: 3px;
  justify-content: space-between;
  align-items: center;
  position: relative;
  padding: 0 50px;
  section {
    display: flex;
    span {
      margin-right: 11px;
    }
    div {
      margin-right: 11px;
    }
  }
  .release {
    width: 180px;
    height: 3.5rem;
    background: rgba(0, 153, 68, 0.2);
    border-radius: 3px;
    cursor: pointer;
    a {
      text-align: center;
      font-size: 26px;
      color: #009944;
      margin: 0 auto;
      line-height: 3.5rem;
    }
  }
}
.con {
  display: flex;
}
.u {
  &_list {
    border-radius: 3px;
    background-color: $c-white;
    // display: flex;
    // flex-direction: column;
    position: relative;
    width: 100%;
    min-height: 60rem;
    flex: 1;
    + section {
      width: 264px;
      height: 405px;
      background: rgba(255, 255, 255, 1);
      box-shadow: 0px 0px 0px rgba(0, 0, 0, 0.1);
      border-radius: 3px;
      margin-left: 1rem;
    }
    article {
      display: flex;
      line-height: 3rem;
      a {
        margin-left: 2rem;
      }
    }
  }
  &_item {
    display: flex;
    border-bottom: 1px solid rgba(229, 229, 229, 1);
    height: 3rem;
    padding: 0 1rem;
    article {
      width: 100%;
    }
  }
  &_time {
    color: #707070;
  }
  &_tname {
    font-weight: 400;
  }
  &_name {
    font-size: 14px;
    font-weight: 400;
    color: #707070;
    position: absolute;
    right: 0;
    margin-right: 20px;
  }
}
.used-pageBox {
  flex: 0 0 auto;
  padding: 20px 0 20px 20px;
  position: absolute;
  bottom: 20px;
}
</style>
