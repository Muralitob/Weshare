<template>
  <div class="avator">
    <div class="info_desc">
      我的头像
    </div>
    <div class="center">
      <div class="pre-container">
        <img  :src="imgDataUrl" alt="">
      </div>
      <div style="margin-top: 20px">
        <Icon type="md-refresh" />
        <Button class="show" type="text" @click="show = true">更新头像</Button>
      </div>
    </div>
    <my-upload
      field="upload-avator"
      @crop-success="cropSuccess"
      @crop-upload-success="cropUploadSuccess"
      @crop-upload-fail="cropUploadFail"
      v-model="show"
      img-format="png"
      :params="params"
      url="/api/user/save_user_avatar"
      method="post"
    >
    </my-upload>
  </div>
</template>

<script>
import myUpload from 'vue-image-crop-upload';
export default {
  components: { myUpload },
  data() {
    return {
      show: false,
      params: {
        uid: this.$cookie.get('uid'),
        token: localStorage.getItem('jwt') || this.$cookie.get('jwt')
      },
      imgDataUrl : `data:image/png;base64,${this.$store.state.UserSetting.userInfo.avatar_base64}`
    }
  },
  methods: {
    cropSuccess(imageDataUrl, field ) {
      this.imgDataUrl  = imageDataUrl
      console.log(this.imgDataUrl)
    },
    cropUploadSuccess(jsonData, field){
      console.log('-------- upload success --------');
      console.log(jsonData);
      console.log('field: ' + field);
    },
    cropUploadFail(status, field){
      console.log('-------- upload fail --------');
      console.log(status);
      console.log('field: ' + field);
    }
  },
  mounted () {
    let userInfo = this.$store.state.UserSetting.userInfo;
  }
}
</script>

<style lang="scss">
  .avator {
    &-confirm {
      width: 140px;
    }
  }
  .center {
    display: flex;
    align-items: center;
    flex-direction: column;
    padding: 80px 20px;
  }
  .pre-container {
    width: 96px;
    height: 96px;
    overflow: hidden;
    border-radius: 50%;
    border: 1px solid #e6eaf0;
    background-size: cover;
  }
  .show {
    padding-left: 0;
  }
  img {
    width: 96px;
    height: 96px;
    vertical-align: middle;
  }
</style>
