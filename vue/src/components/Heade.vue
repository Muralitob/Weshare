<template>
  <header>
    <Modal class="useraction" scrollable footer-hide  v-model="LoginShow" width="360">
      <h1>登录</h1>
      <Form ref="LoginForm" :model="loginForm" :rules="LoginRule">
        <FormItem label="用户名/学号/邮箱:" prop="account">
            <Input type="text"  placeholder="Username" v-model="loginForm.account">
            </Input>
        </FormItem>
        <FormItem label="密码:" prop="password">
            <Input type="password" placeholder="Password" v-model="loginForm.password">
            </Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('LoginForm')">登录</Button>
        </FormItem>
        <div class="prompt-box">
          <span>没有账号?</span> 
          <span @click="changeAction('regist')">立即注册</span>
          <span>忘记密码?</span>
        </div>
    </Form>
    </Modal>
    <Modal class="useraction" scrollable footer-hide v-model="RegistShow" width="360">
      <h1>注册</h1>
      <Form ref="RegistForm" :model="registForm" :rules="RegistRule">
        <FormItem label="用户名/学号/邮箱:" prop="account">
            <Input type="text"  placeholder="Username" v-model="registForm.account">
            </Input>
        </FormItem>
        <FormItem label="密码:" prop="password">
            <Input type="password" placeholder="Password" v-model="registForm.password">
            </Input>
        </FormItem>
        <FormItem label="重复密码:" prop="passwdCheck">
            <Input type="password" placeholder="请填写相同的密码" v-model="registForm.passwdCheck">
            </Input>
        </FormItem>
        <FormItem>
            <Button type="primary" @click="handleSubmit('RegistForm')">注册</Button>
        </FormItem>
        <div class="prompt-box">
          <span>已有账号?</span> 
          <span @click="changeAction('login')">立即登录</span>
        </div>
    </Form>
    </Modal>
    <div class="top">
      <ul class="top__list">
        <div class="wrapper" @click="toggleNav">
          <router-link  v-for="(item, idx) in routeList" 
          v-if="item.meta.ifShow"
          :key="idx" 
          class="top__item" 
          tag="li" 
          :to="item.path"
          activeClass="link_active"
          >
            <span class="top__item-title">{{item.name}}</span>
          </router-link>
        </div>
      </ul>
      <ul class="top__user">
        <li @click="Login"><span>登录</span></li>
        <li @click="Regist"><span>注册</span></li>
      </ul>
      <!-- <div class="top__hamburger" @click="toggleNav">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
      </div> -->
      <router-link to="/" id="logo">Weshare</router-link>
    </div>
    <!--banner-->
    <!-- <div class="banner"></div> -->
  </header>
</template>

<script>
import Routes from '../router';
import { translate } from '../general/js/translate.js';
export default {
  data () {
    const validatePassCheck = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再输入一遍密码'));
      } else if (value !== this.registForm.password) {
        callback(new Error('输入两个密码匹配,请重新输入'));
      } else {
        callback();
      }
    };
    return {
      routeList: [],
      LoginShow: false,
      RegistShow: false,
      LoginRule: {
          account: [
              { required: true, message: '请填写用户名/学号/邮箱', trigger: 'blur' }
          ],
          password: [
              { required: true, message: '请填写密码', trigger: 'blur' },
              { type: 'string', min: 6, message: '密码至少是6位', trigger: 'blur' }
          ]
      },
      RegistRule: {
          account: [
            { required: true, message: '请填写用户名/学号/邮箱', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请填写密码', trigger: 'blur' },
            { type: 'string', min: 6, message: '密码至少是6位', trigger: 'blur' }
          ],
          passwdCheck: [
            { validator: validatePassCheck, trigger: 'blur' }
          ],
      },
      loginForm: {
        account: '',
        password: '',
      },
      registForm: {
        account: '',
        password: '',
        passwdCheck: ''
      }
    }
  },
  methods: {
    //移动端下的切换
    toggleNav() {  
      // document.querySelector(".top__hamburger")
      // .classList.toggle("top__hamburger--active")
      // document.querySelector(".top__list")
      // .classList.toggle("top__list--active")
    },
    handleScroll() {  //菜单栏吸附
       var scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
       if( scrollTop >=(15.5*16)){
         document.querySelector('.top__list').style.position = "fixed" 
         document.querySelector('.top__list').style.top = "0"
       }else{
         document.querySelector('.top__list').style.position = "static" 
       }
    },
    Login() {
      this.LoginShow = true
    },
    Regist() {
      this.RegistShow = true
    },
    changeAction(action) {
      if(action === 'regist') {
        this.LoginShow = false
        this.RegistShow = true
      }else if(action === 'login') {
        this.RegistShow = false
        this.LoginShow = true
      }
    },
    handleSubmit(name) {
      this.$refs[name].validate((valid) => {
        if (valid) {
          this.$store.dispatch('UserLogin', this.loginForm)
          //关闭Modal
          this.LoginShow = false
          //清空表单数据
          // this.loginForm = {
          //   account: '',
          //   password: '',
          // }
          // this.registForm = {
          //   account: '',
          //   password: '',
          //   passwdCheck: ''
          // }
        }else {
          return
        }
      })
    }
  },
  mounted() {
    /***设置滚动监听事件 */
    // window.addEventListener('scroll', this.handleScroll)
    // Routes.options.routes.forEach(currentItem => {
      //   this.routeList.path = translate(currentItem.path)
      // console.log(translate('Setting'))
    // })
    // console.log(this.routeList);
    const routes_Array = Routes.options.routes
    this.routeList = Object.keys(routes_Array).map(e => ({
      name: translate(routes_Array[e].name),
      key: e,
      path: routes_Array[e].path,
      meta: Object.assign({},routes_Array[e].meta),
    }))
  },
}
</script>

<style lang="scss">
#logo{
  @include tablet-min{
    display: none;
  }
}
header{
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  @include tablet-min{
    // position: static;
    width: 100%;
    min-width: $min-width;
  }
}
.link_active{
  // background-color:  $c-deepgreen;
  border-bottom: 4px solid $c-green;
}
.top{
  // justify-content: flex-end;
  min-width: $min-width;
  position: absolute;
  background-color: $menu_color;
  display: flex;
  justify-content: center;
  width: 100%;
  a{
    text-align: center;
    line-height: 3.5rem;
  }
  &__user{
    position: absolute;
    right: 0;
    bottom: 0;
    display: flex;
    margin-right: 17px;
    height: 3.5rem;
    line-height: 3.5rem;
    li{
      font-size: 14px;
      font-weight: 350;
      cursor: pointer;
      &:nth-child(1){
        &::after{
          content: "\B7";
          margin: 0 .3rem;
        }
      }
      a{
        @include tablet-min{
          color: $c-white;
        }
      }
    }
  }
  &__hamburger{
    position: fixed;
    top: 0;
    left: 0;
    width: 3.5rem;
    height: 3.5rem;
    z-index: 10;
    @include tablet-min {
      display: none;
    }
    .bar{
      width: 22px;
      height: 1px;
      position: absolute;
      transition: all .3s ease;
      background: rgba(8, 28, 36, 0.5);
      &:nth-child(1){
        left: 16px;
        top: 17px;
      }
      &:nth-child(2){
        right: 18px;
        top: 26px;
        &::after{
          content: "";
          position: absolute;
          left: 0px;
          top: 0px;
          width: 23px;
          height: 1px;
          background: transparent;
          transition: all 300ms ease;
        }
      }
      &:nth-child(3){
        left: 16px;
        top: 35px;
      }
    }
    &--active{
      .bar{
        &:nth-child(1),
        &:nth-child(3){
          width: 0;
        }
        &:nth-child(2){
          transform: rotate(-45deg);
        }
        &:nth-child(2):after {
          transform: rotate(-90deg);
          background: rgba($c-dark, 0.5);
        }
      }
    }
  }
  &__list{
      // background: rgba($c-white, 0.98);
      box-sizing: border-box;
      z-index: 11;
      @include mobile-only{
        border-top: 1px solid $c-light;
        opacity: 0;
        visibility: hidden;
        height: calc(100vh - 3.5rem);
        transition: all 0.5s ease;
        &--active{
          opacity: 1;
          visibility: visible;
        }
      }
      @include tablet-min{
        // background-color: $menu-color;
        color: $c-white;
        height: 3.5rem;
        // box-shadow: 0px 2px 10px 0px rgba(0,0,0,0.1), 0 1px rgba(0,0,0,0.1);
        .wrapper{
          display: flex;
        }
      }
    }
    &__item{
      &-title {
        font-size: 16px;
      }
      @include mobile-only {
        display: inline-block;
        text-align: center;
        width: 50%;
        height: 6rem;
        line-height: 6rem;
        border-bottom: 1px solid $c-light;
        &:nth-child(even){
          border-right: 1px solid $c-light;
        }
      }
      @include tablet-min{
        width: 6rem;
        height: 3.5rem;
        line-height: 3.5rem;
        text-align: center;
        cursor: pointer;
        // &:nth-child(1){
        //   text-align: left;
        //   width: 2rem;
        //   margin-right: 1rem;
        //   border-bottom: none;
        // }
      }
    }
}
.useraction {
  h1 {
    padding-top: 1rem;
  }
  button {
    width: 100%;
  }
  .prompt-box {
    margin-bottom: .5rem;
    span{
      &:nth-child(2),&:nth-child(3) {
        color: $c-green;
        cursor: pointer;
      }
      &:nth-child(3) {
        float: right;
      }
    }
  }
}
</style>
