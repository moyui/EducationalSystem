<template>
  <el-container>
    <el-dialog title="登录" center width="30%" :visible="loginVisible" class="dialog" @close="cancelLogin">
      <el-form label-width="80px" :model="info">
        <el-form-item label="邮箱">
          <el-input v-model="info.mail" placeholder="请输入邮箱" suffix-icon="el-icon-phone"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="info.password" placeholder="请输入密码" show-password></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancelLogin">取 消</el-button>
        <el-button type="primary" @click="login">确 定</el-button>
        <el-button type="info" @click="switchRegister">前往注册</el-button>
      </span>
    </el-dialog>

    <el-dialog title="注册" center width="30%" :visible="registerVisible" class="dialog" @close="cancelRegister">
      <el-form label-width="80px" :model="info">
        <el-form-item label="邮箱">
          <el-input v-model="info.mail" placeholder="请输入邮箱" suffix-icon="el-icon-phone"></el-input>
        </el-form-item>
        <el-form-item label="密码">
          <el-input v-model="info.password" placeholder="请输入密码" show-password></el-input>
        </el-form-item>
        <el-form-item label="确认密码">
          <el-input v-model="info.checkPassword" placeholder="请确认密码" show-password></el-input>
        </el-form-item>
        <el-form-item label="用户名">
           <el-input v-model="info.userName" placeholder="请输入用户名"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancelRegister">取 消</el-button>
        <el-button type="primary" @click="register">确 定</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>
<script>
import { postLogin, postRegister } from "./api";

export default {
  data() {
    return {
      info: {
        mail: "",
        password: "",
        checkPassword: "",
        userName: ""
      }
    };
  },
  computed: {
    loginVisible() {
      return this.$store.state.loginVisible;
    },
    registerVisible() {
      return this.$store.state.registerVisible;
    }
  },
  methods: {
    login() {
      this.$store.commit("SET_LOGIN_VISIBLE", false);
      return postLogin(this.info).then(data => this.loginBack(data));
    },
    register() {
      return postRegister(this.info)
        .then(data => this.registerBack(data))
        .catch(() =>
          this.$message({
            message: "服务器君不行了，请稍后再试一下",
            type: "error"
          })
        );
    },
    loginBack(data) {
      if (data.status == 0)
        this.$message({
          message: "登录失败, 邮箱错误或密码错误",
          type: "error"
        });
      if (data.status == 1) {
        this.$message({
          message: "登录成功",
          type: "success"
        });
        setTimeout(() => window.location.reload(), 2000);
      }
    },
    registerBack(data) {
      if (data.status == 0)
        this.$message({
          message: data.message,
          type: "warn"
        });
      if (data.status == 1) {
        this.$message({
          message: "注册成功",
          type: "success"
        });
        this.switchLogin();
      }
    },
    cancelLogin() {
      this.$store.commit("SET_LOGIN_VISIBLE", false);
    },
    cancelRegister() {
      this.$store.commit("SET_REGISTER_VISIBLE", false);
    },
    switchLogin() {
      this.$store.commit("SET_LOGIN_VISIBLE", true);
      this.$store.commit("SET_REGISTER_VISIBLE", false);
    },
    switchRegister() {
      this.$store.commit("SET_LOGIN_VISIBLE", false);
      this.$store.commit("SET_REGISTER_VISIBLE", true);
    }
  }
};
</script>


