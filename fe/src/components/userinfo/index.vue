<template>
  <div>
    <h3>个人信息</h3>
    <el-form>
      <el-form-item label="您的邮箱">
        <el-input v-model="mail" suffix-icon="el-icon-phone" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="您的用户名">
        <el-input v-model="userName" :disabled="true"></el-input>
      </el-form-item>
      <el-form-item label="手机号">
        <el-input
          v-model="phone"
          placeholder="请输入您的手机"
          suffix-icon="el-icon-phone"
          :disabled="phoneAble"
        ></el-input>
      </el-form-item>
      <el-button type="primary" @click="addPhone" v-if="!phoneAble">提交手机号</el-button>
    </el-form>
    <el-divider></el-divider>
    <h3>个人成就</h3>
    <div class="honer-wrap" v-if="honer.length > 0">
      <div v-for="item in honer" :key="item.honerid" class="honer">
        <h5>{{item.typename}}</h5>
        <div class="course-name">{{item.coursename}}</div>
        <span>获得时间：{{getLocalTime(item.createdate)}}</span>
      </div>
    </div>
  </div>
</template>
<script>
import { getInfo, postPhone, getHoner } from "./api.js";

export default {
  data() {
    return {
      mail: "",
      userName: "",
      phone: "",
      phoneAble: true,
      honer: []
    };
  },
  created() {
    getInfo().then(res => {
      this.mail = res.data.mail;
      this.userName = res.data.name;
      this.phone = res.data.phone;
      this.phoneAble = !!this.phone;
    });
    getHoner().then(res => (this.honer = res.data));
  },
  methods: {
    addPhone() {
      return postPhone(this.phone)
        .then(data => {
          this.$message({
            message: data.message,
            type: "success"
          });
          setTimeout(() => window.location.reload(), 2000);
        })
        .catch(rej => {
          this.$message({
            message: rej.data.message,
            type: "error"
          });
        });
    },
    getLocalTime(nS) {
      return new Date(parseInt(nS) * 1000)
        .toLocaleString()
        .replace(/:\d{1,2}$/, " ");
    }
  }
};
</script>
<style lang="less">
.honer-wrap {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}
.honer {
  width: 200px;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  height: 120px;
  justify-content: space-between;
  border: 1px solid #d6d6d6;
  margin-top: 20px;
  padding: 20px 0;
  h5 {
    font-size: 18px;
    font-weight: normal;
  }
  .course-name {
    font-size: 16px;
  }
}
</style>
