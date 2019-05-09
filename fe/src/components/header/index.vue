<template>
  <el-header class="header">
    <el-menu mode="horizontal" :default-active="activeIndex">
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
        <template slot="title">{{getUserName}}</template>
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

export default {
  data() {
    return {
      activeIndex: "1",
      info: {
        mail: "",
        userName: "",
        reason: ""
      },
      reportVisible: false
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

