<template>
  <el-container class="center" direction="vertical">
    <h3 class="title">您好，{{getUserName}}学员</h3>
    <el-container>
      <el-aside>
        <el-menu :default-active="activeIndex" @select="changeIndex">
          <el-menu-item index="1">个人信息</el-menu-item>
          <el-menu-item index="2">课程表</el-menu-item>
          <el-menu-item index="3">全部订单</el-menu-item>
          <el-menu-item index="4">我的余额</el-menu-item>
          <el-menu-item index="5">课程分销</el-menu-item>
        </el-menu>
      </el-aside>
      <el-main>
        <UserInfo v-if="activeIndex == '1'"/>
        <Recharge v-if="activeIndex == '4'"/>
        <Order v-if="activeIndex == '3'"/>
      </el-main>
    </el-container>
  </el-container>
</template>
<script>
import Cookie from "js-cookie";

const UserInfo = () => import("../../components/userinfo/index.vue");
const Recharge = () => import("../../components/recharge/index.vue");
const Order = () => import("../../components/order/index.vue");

export default {
  components: { UserInfo, Recharge, Order },
  data() {
    return {
      activeIndex: "1"
    };
  },
  computed: {
    getUserName() {
      return Cookie.get("username") || "未知生物";
    }
  },
  methods: {
    changeIndex(index) {
      this.activeIndex = index;
    }
  }
};
</script>
<style lang="less">
.center {
  padding: 0 20px;
  height: calc(100% - 60px);
  margin-top: 60px;
  width: 100%;
  .title {
    display: block;
  }
}
</style>
