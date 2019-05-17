<template>
  <el-container class="payment">
    <div>
      <h3>课程编号：{{id}}</h3>
      <span>价格：{{price}}</span>
      <el-button type="primary" @click="confirm">扣款</el-button>
    </div>
  </el-container>
</template>
<script>
import { postPurchase } from "./api";

export default {
  computed: {
    id() {
      return this.$store.state.order.id || 0;
    },
    price() {
      return this.$store.state.order.price || "";
    }
  },
  methods: {
    confirm() {
      var link = localStorage.getItem("link");
      localStorage.removeItem('link');
      return postPurchase(this.id, link).then(() => 
        this.$router.push(`/view/${this.id}`)
      );
    }
  }
};
</script>
<style lang="less" scoped>
.payment {
  height: calc(100% - 60px);
  margin-top: 60px;
  width: 100%;
}
</style>


