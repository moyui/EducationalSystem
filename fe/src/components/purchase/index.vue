<template>
  <el-dialog title="购买课程" :visible="visible" @close="cancel" width="40%">
    <div class="purchase__content">
      <div class="purchase__header">
        <img :src="img" class="purchase__img">
        <div class="purchase__meta">
          <h5 class="purchase__title">{{name}}</h5>
          <span class="purchase__teacher">{{teacher}}</span>
        </div>
      </div>
      <p class="purchase__price">
        课程价格
        <i class="purchase__price-unit">￥</i>
        <i class="purchase__price-num">{{price}}</i>
      </p>
      <el-form label-width="120px" class="fen">
        <el-form-item label="课程分销代码：">
          <el-input v-model="link" placeholder="请输入分销代码，无就忽略"></el-input>
        </el-form-item>
      </el-form>
    </div>
    <div slot="footer" class="dialog-footer">
      <el-button @click="cancel">取 消</el-button>
      <el-button type="primary" @click="confirm">去付款</el-button>
    </div>
  </el-dialog>
</template>
<script>
import { postPurchase } from "./api";

export default {
  data() {
    return {
      link: ""
    };
  },
  computed: {
    id() {
      return this.$store.state.order.id || 0;
    },
    img() {
      return this.$store.state.order.img || "";
    },
    teacher() {
      return this.$store.state.order.teacher || "";
    },
    name() {
      return this.$store.state.order.name || "";
    },
    price() {
      return this.$store.state.order.price || "";
    },
    visible() {
      return this.$store.state.orderVisible;
    }
  },
  methods: {
    cancel() {
      this.$store.commit("SET_ORDER_VISIBLE", false);
    },
    confirm() {
      return postPurchase(this.id, this.link)
        .then(data => {
          this.$message({
            message: data.message,
            type: "success"
          });
          window.location.reload();
        })
        .catch(rej => {
          this.$store.commit("SET_ORDER_VISIBLE", false);
          // 跳转支付单独页
          if (rej.data.status == 3) {
            localStorage.setItem('link', this.link);
            this.$router.push({ path: "/payment" });
          } else {
            this.$message({
              message: rej.data.message,
              type: "error"
            });
          }
        });
    }
  }
};
</script>
<style lang="less" scoped>
.purchase__content {
  .purchase__header {
    display: flex;
    flex-direction: row;
  }
  .purchase__img {
    width: 90px;
    height: 50px;
  }
  .purchase__meta {
    display: flex;
    flex-direction: column;
    margin-left: 20px;
    flex: 1;
    .purchase__title {
      font-weight: normal;
      font-size: 18px;
    }
    .purchase__teacher {
      margin-top: 5px;
      color: #999999;
    }
  }
  .purchase__price {
    margin-top: 10px;
  }
  .purchase__price-unit {
    color: #e85308;
    font-size: 14px;
    font-style: normal;
    margin-left: 10px;
  }
  .purchase__price-num {
    color: #e85308;
    font-size: 30px;
    font-style: normal;
  }
}
.fen {
  margin-top: 20px;
}
</style>
