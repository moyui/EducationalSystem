<template>
  <el-header class="header">
    <el-menu
      mode="horizontal"
      :default-active="activeIndex"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#fff"
      class="menu"
    >
      <el-menu-item index="0">
        <router-link to="/" slot="title">
          <span>在线教育系统</span>
        </router-link>
      </el-menu-item>
      <el-menu-item v-if="!isLogin" index="1" class="nav__login" @click="activeLogin">
        <i class="el-icon-setting"></i>
        <span slot="title">登录</span>
      </el-menu-item>
      <el-submenu v-else index="2" class="nav__login">
        <template slot="title">{{userName || '未知'}}</template>
        <el-menu-item index="2-1" @click="toUserCenter">个人中心</el-menu-item>
        <el-menu-item index="2-2" @click="activeReport">举报用户</el-menu-item>
        <el-menu-item index="2-3" class="nav__login_out" @click="logout">退出登录</el-menu-item>
      </el-submenu>
    </el-menu>
    <el-dialog :append-to-body="true" :visible="reportVisible" @close="cancelReport">
      <el-form label-width="80px" :model="info">
        <el-form-item label="用户邮箱">
          <el-input v-model="info.mail" placeholder="请输入用户邮箱" suffix-icon="el-icon-phone"></el-input>
        </el-form-item>
        <el-form-item label="用户名">
          <el-input v-model="info.userName" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="举报理由">
          <el-input
            v-model="info.reason"
            placeholder="请输入举报理由"
            type="textarea"
            show-word-limit
            :autosize="{ minRows: 2, maxRows: 6 }"
          ></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancelReport">取 消</el-button>
        <el-button type="primary" @click="submitReport">确定举报</el-button>
      </span>
    </el-dialog>
  </el-header>
</template>
<script>
import Cookie from "js-cookie";
import { getUserInfo } from "./api";

export default {
  data() {
    return {
      activeIndex: "1",
      info: {
        mail: "",
        userName: "",
        reason: ""
      },
      reportVisible: false,
      userName: ""
    };
  },
  created() {
    if (Cookie.get("userid")) {
      this.$store.commit("SET_LOGIN", true);
      getUserInfo().then(data => (this.userName = data.data.name));
    }
  },
  computed: {
    isLogin() {
      return this.$store.state.login;
    },
    getUserName() {},
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
      window.location.reload();
    },
    activeLogin() {
      this.$store.commit("SET_LOGIN_VISIBLE", true);
    },
    activeReport() {
      this.reportVisible = true;
    },
    cancelReport() {
      this.reportVisible = false;
    },
    submitReport() {
      this.cancelReport();
    },
    toUserCenter() {
      this.$router.push({ path: "/center" });
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
  padding: 0 0;
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
.menu {
  height: 80px;
  padding: 0 0;
  .el-menu-item,
  .el-submenu {
    height: 100%;
    display: inline-flex;
    align-items: center;
    font-size: 16px;
  }
  .el-submenu__title {
    height: 100%;
  }
  .el-menu-item:first-child {
    width: 20%;
    display: inline-flex;
    justify-content: center;
    align-self: center;
  }
}
</style>

