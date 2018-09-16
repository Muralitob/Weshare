<template>
  <div class="info">
    <div class="info_desc">
      个人资料
    </div>
    <div class="info_main">
      <Form :model="formItem" :label-width="80">
        <FormItem label="昵称:">
            <Input style="width: 200px" v-model="formItem.nick_name" placeholder="输入你的昵称" />
        </FormItem>
        <FormItem label="我的签名">
          <Input class="sign" v-model="formItem.sign" type="textarea" :autosize="{minRows: 4,maxRows: 5}" placeholder="Enter something..."></Input>
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
            <Button style="width: 110px" type="primary">保存</Button>
        </FormItem>
    </Form>
    </div>
  </div>  
</template>

<script>
export default {
  data() {
    return {
      formItem: {
        nick_name: '年轻人QZ',
        sign: '我草了都',
        sex: 'secret',
        birth_day: new Date(),
      }
    }
  },
  methods: {
    test(pre, next) {
      console.log(pre, next)
    }
  }
}
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
        resize:none;
      }
      width: 500px;
    }
  }
</style>
