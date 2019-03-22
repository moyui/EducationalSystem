<template>
  <el-header class="header">
    <el-menu mode="horizontal" :default-active="activeIndex">
      <el-menu-item index="0">
        <span slot="title">教育信息系统</span>
      </el-menu-item>
      <el-menu-item v-if="!isLogin" index="1" class="nav__login" @click="activeLogin">
        <i class="el-icon-setting"></i>
        <span slot="title">登录</span>
      </el-menu-item>
      <el-submenu v-else index="2" class="nav__login">
        <template slot="title">{{getUserName}}</template>
        <el-menu-item index="2-1">个人中心</el-menu-item>
        <el-menu-item index="2-2">收藏夹</el-menu-item>
        <el-menu-item index="2-3">课程表</el-menu-item>
        <el-menu-item index="2-4" class="nav__login_out" @click="logout">退出登录</el-menu-item>
      </el-submenu>
    </el-menu>
  </el-header>
</template>
<script>
import Cookie from "js-cookie";

export default {
  data() {
    return {
      activeIndex: "0"
    };
  },
  created() {
    if (Cookie.get("userid")) this.$store.commit("SET_LOGIN", true);
  },
  computed: {
    isLogin() {
      return this.$store.state.login;
    },
    getUserName() {
      return Cookie.get("username") || "未知生物";
    },
    loginVisible() {
      return this.$store.state.loginVisible;
    },
    registerVisible() {
      return this.$store.state.registerVisible;
    }
  },
  methods: {
    logout() {
      Cookie.remove("userid");
      Cookie.remove("username");
      window.location.reload();
    },
    activeLogin() {
      this.$store.commit("SET_LOGIN_VISIBLE", true);
    }
  }
};
</script>
<style lang="less" scoped>
.header {
  position: fixed;
  left: 0;
  right: 0;
  top: 0;
  z-index: 1;
}
.nav__login {
  float: right;
}
.nav__login_out {
  border-top: 1px solid #ebebee;
}
.dialog {
  z-index: 3000;
}
</style>

