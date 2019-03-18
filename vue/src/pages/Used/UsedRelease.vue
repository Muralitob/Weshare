<template>
  <div class="used_release box">
    <h3>发布信息</h3>
    <Form ref="usedGoods" :model="usedGoods" :rules="ruleValidate" :label-width="80">
        <FormItem label="标题" prop="title">
            <Input v-model="usedGoods.title" placeholder="输入标题"></Input>
        </FormItem>
        <FormItem label="描述" prop="desc">
            <Input v-model="usedGoods.desc" placeholder="描述一下闲置物品" type="textarea" :autosize="{minRows: 2,maxRows: 5}" ></Input>
        </FormItem>
        <FormItem label="类型" prop="type">
            <Select style="width:150px" v-model="usedGoods.type" placeholder="选择物品类型">
                <Option v-for="item in usedtypes" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
        </FormItem>
        <FormItem label="新旧程度" prop="degree">
            <Select style="width:150px" v-model="usedGoods.degree" placeholder="选择物品类型">
                <Option v-for="item in degree" :value="item.value" :key="item.value">{{ item.label }}</Option>
            </Select>
        </FormItem>
        <FormItem label="物品照片" prop="pic">
          <div class="demo-upload-list" v-for="(item,index) in uploadList" :key="index">
            <template v-if="item.status === 'finished'">
              <img :src="'data:image/png;base64,'+item.response.good_base64">
              <div class="demo-upload-list-cover">
                <Icon type="ios-eye-outline" @click.native="handleView(item.name)"></Icon>
                <Icon type="ios-trash-outline" @click.native="handleRemove(item)"></Icon>
              </div>
            </template>
            <template v-else>
              <Progress v-if="item.showProgress" :percent="item.percentage" hide-info></Progress>
            </template>
          </div>
           <Upload
            ref="upload"
            :show-upload-list="false"
            :on-success="handleSuccess"
            :data="imgdata"
            :format="['jpg','jpeg','png']"
            :max-size="2048"
            :on-format-error="handleFormatError"
            :on-exceeded-size="handleMaxSize"
            :before-upload="handleBeforeUpload"
            :on-progress="handleProgress"
            multiple
            type="drag"
            action="/api/goods/save_good_photo"
            style="display: inline-block;width:58px;">
            <div style="width: 58px;height:58px;line-height: 58px;">
              <Icon type="ios-camera" size="20"></Icon>
            </div>
          </Upload>
        </FormItem>
        <FormItem label="价格" prop="price">
            <Input v-model="usedGoods.price" prefix="logo-yen" placeholder="输入你的价格" style="width: 120px" />
        </FormItem>
        <FormItem label="交易方式" prop="mode">
            <CheckboxGroup v-model="usedGoods.mode">
              <Checkbox label="face" disabled>当面交易</Checkbox>
            </CheckboxGroup>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('usedGoods')">发布</Button>
            <Button @click="handleReset('usedGoods')" style="margin-left: 8px">重置</Button>
        </FormItem>
        
    </Form>
  </div>
</template>

<script>
import api from "../../api";
import used from "../../constants/usedType.js";
export default {
  data() {
    return {
      usedGoods: {
        title: "",
        type: "",
        pic: "",
        price: "",
        mode: ["face"],
        desc: "",
        degree: '',
      },
      degree: [
        {
          value: 10,
          label: '全新',
        },
        {
          value: 9,
          label: "九成新"
        },
        {
          value: 8,
          label: "八成新"
        },
        {
          value: 7,
          label: "七成新"
        },
        {
          value: 6,
          label: "六成新"
        },
        {
          value: 5,
          label: "五成新及以下"
        }
      ],
      ruleValidate: {
        title: [
          {
            required: true,
            message: "标题不能为空",
            trigger: "blur"
          },
          {
            type: "string",
            min: 4,
            message: "至少需要4个字",
            trigger: "blur"
          }
        ],
        type: [
          {
            required: true,
            message: "请选择一个类型",
            trigger: "change"
          }
        ],
        price: [
          {
            required: true,
            message: "输入一个价格",
            trigger: "blur"
          },
          {
            type: "number",
            message: "请输入一个有效的价格",
            trigger: "blur",
            transform(value) {
              return Number(value);
            }
          }
        ],
        degree: [
          {
            type: "number",
            required: true,
            message: "新旧程度不能为空",
            trigger: "change"
          }
        ],
        desc: [
          {
            required: true,
            message: "请输入简介",
            trigger: "blur"
          },
          {
            type: "string",
            min: 20,
            message: "至少需要20个字",
            trigger: "blur"
          }
        ]
      },
      imgName: "",
      visible: false,
      uploadList: [],
      usedtypes: used.usedType,
      defaultList: [],
      imgdata: {
        uid: this.$cookie.get('uid')
      }
    };
  },
  methods: {
    handleView(name) {
      this.imgName = name;
      this.visible = true;
    },
    handleRemove(file) {
      console.log(file);
      const fileList = this.$refs.upload.fileList;
      console.log('fileList', fileList);
      this.$refs.upload.fileList.splice(fileList.indexOf(file), 1);
    },
    handleSubmit(name) {
      this.$refs[name].validate(valid => {
        if (valid) {
          this.$Message.success("发布成功!");
          api
            .realeaseUsed("post", this.usedGoods)
            .then(({ data }) => {
              console.log(data);
            })
            .catch(err => {
              console.log("err", err);
            });
        } else {
          this.$Message.error("请你检查应填信息");
        }
      });
    },
    handleReset(name) {
      this.$refs[name].resetFields();
    },
    handleView(name) {
      this.imgName = name;
      this.visible = true;
    },
    handleRemove(file) {
      const fileList = this.$refs.upload.fileList;
      this.$refs.upload.fileList.splice(fileList.indexOf(file), 1);
    },
    handleSuccess(res, file) {
    },
    handleFormatError(file) {
      this.$Notice.warning({
        title: "文件格式不正确",
        desc: "文件格式:" + file.name + " 不正确，请选择JPG或PNG。"
      });
    },
    handleMaxSize(file) {
      this.$Notice.warning({
        title: "文件大小闲置",
        desc: "文件:" + file.name + " 太大了, 不能超过2M"
      });
    },
    handleBeforeUpload() {
      const check = this.uploadList.length < 5;
      this.usedGoods.pic = this.uploadList
      console.log("上传前");
      if (!check) {
        this.$Notice.warning({
          title: "最多可上传五张图片。"
        });
      }
      return check;
    },
    handleProgress(event, file, fileList) {
      console.log(file);
    }
  },
  mounted() {
    this.uploadList = this.$refs.upload.fileList;
    console.log(this.$refs.upload);
  }
};
</script>

<style lang="scss">
.used_release {
  background-color: #fff;
  padding: 30px 20px;
  border-radius: 3px;
  box-shadow: 0px 2px 10px 0px rgba(0, 0, 0, 0.1), 0 1px rgba(0, 0, 0, 0.1);
  h3 {
    margin-bottom: 20px;
  }
}
img {
  width: 64px;
  height: 64px;
}
</style>
