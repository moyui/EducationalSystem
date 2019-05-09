<template>
  <el-form>
    <el-form-item label="您的邮箱">
      <el-input v-model="mail" suffix-icon="el-icon-phone"></el-input>
    </el-form-item>
    <el-form-item label="您的用户名">
      <el-input v-model="userName"></el-input>
    </el-form-item>
    <el-form-item label="手机号">
      <el-input v-model="phone" placeholder="请输入您的手机" suffix-icon="el-icon-phone"></el-input>
    </el-form-item>
  </el-form>
</template>
<script>
export default {
  data() {
    return {
      mail: "",
      userName: "",
      phone: ""
    };
  }
};
</script>
<style lang="less">
</style>
