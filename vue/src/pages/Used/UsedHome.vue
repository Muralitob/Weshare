<template>
  <div class="user_home">
    <div class="cutarea">
      <section>
        <div>
          <span>类别:</span>
          <Select clearable  v-model="model1" style="width:150px">
            <Option v-for="item in cityList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </div>
        <div>
          <span>新旧程度:</span>
          <Select clearable  v-model="model2" style="width:120px">
            <Option v-for="item in cityList1" :value="item.value" :key="item.value">{{ item.label }}</Option>
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
            <span class="u_time">{{item.release_time}}</span>
            <router-link to="/used/101"><p class="u_tname">{{item.release_thingname}}</p></router-link>
            <p class="u_name">{{item.user_name}}<span> - ￥{{item.price}}</span></p>
          </article>
        </li>
      <Page prev-text="上一页" next-text="下一页" @on-change="changepage" :total="40" show-elevator class-name="used-pageBox"></Page>
      </ul>
      <section>
        最新成交
      </section>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cityList: [
        {
          value: "New York",
          label: "New York"
        },
        {
          value: "London",
          label: "London"
        }
      ],
      cityList1: [
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
      model1: "",
      model2: "",
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
      ]
    };
  },
  methods: {
    changepage() {}
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
      * {
        margin-right: 2rem;
      }
    }
  }
  &_item {
    border-bottom: 1px solid rgba(229, 229, 229, 1);
    height: 3rem;
    padding: 0 1rem;
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
  }
}
.used-pageBox {
  flex: 0 0 auto;
  padding: 20px 0 20px 20px;
  position: absolute;
  bottom: 20px;
}
</style>
