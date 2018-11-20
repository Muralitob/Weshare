<template>
  <div class="info">
    <div class="info_desc">
      个人资料
    </div>
    <div class="info_main">
      <Form :model="formItem" :label-width="80">
        <FormItem label="昵称:">
            <Input style="width: 200px" v-model="formItem.nickname" placeholder="输入你的昵称" />
        </FormItem>
        <FormItem label="我的签名">
          <Input class="sign" v-model="formItem.sign" type="textarea" :autosize="{minRows: 4,maxRows: 5}" placeholder="Enter something..."></Input>
        </FormItem>
        <FormItem label="我的分院">
          <Select filterable v-model="formItem.branch" style="width:200px">
            <Option v-for="item in majorList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </FormItem>
        <FormItem label="性别:">
            <RadioGroup v-model="formItem.sex">
                <Radio label="male">男</Radio>
                <Radio label="female">女</Radio>
                <Radio label="secret">保密</Radio>
            </RadioGroup>
        </FormItem>
        <FormItem label="出生年月:">
          <DatePicker :value="formItem.birth_day" @on-change="test" type="date" placeholder="选择出生日期" style="width: 200px"></DatePicker>
        </FormItem>
        <FormItem>
            <Button style="width: 110px" type="primary" @click="handleUserInfo">保存</Button>
        </FormItem>
    </Form>
    </div>
  </div>  
</template>

<script>
import api from "../../api";
import general from "../../general/js";
import major from '../../constants/major.js';
export default {
  data() {
    return {
      formItem: {
        nickname: "",
        sign: "",
        sex: "",
        birth_day: "",
        branch: '',
      },
      majorList: major
    };
  },
  methods: {
    test(pre, next) {
      this.formItem.birth_day = pre;
    },
    fetchUserInfo() {
      let data = this.$store.state.UserSetting.userInfo
      let result = {
        nickname: data.nickname,
        sex: data.sex || "secret",
        birth_day: data.birth_day || "",
        sign: data.sign || "你怎么这么懒,签名都不写",
        branch: data.branch
      };
      this.formItem = result;
    },
    handleUserInfo() {
      api.editUserInfo(this.formItem).then(({ data }) => {
        let message = new general.MyMessage(data.code, data.message)
        message.successnotice()
        // this.mymessage().successnotice(data.code, data.message)
        // this.$Notice.success({
        //   title: "用户信息更新",
        //   desc: data.message
        // });
      });
    }
  },
  mounted() {
    this.fetchUserInfo();
  }
};
</script>

<style lang="scss">
.info {
  width: 100%;
  &_desc {
    border-bottom: 3px solid $c-green;
    width: 90px;
  }
  &_main {
    margin-top: 20px;
    display: flex;
    justify-content: center;
    padding: 20px 20px;
    form {
      width: 800px;
    }
  }
  .sign {
    textarea {
      resize: none;
    }
    width: 500px;
  }
}
</style>
