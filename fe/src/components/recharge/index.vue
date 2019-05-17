<template>
  <div>
    <div>
      <div>
        <h5>我的余额</h5>
        <span>{{rest || '暂无数据'}}</span>
      </div>
      <el-button type="primary" @click="activeRecharge">充值</el-button>
    </div>
    <div>
      <h5>余额明细</h5>
      <el-table height="400" stripe border :data="restList">
        <el-table-column prop="type" label="类型" width="150" fixed></el-table-column>
        <el-table-column prop="date" label="日期" width="120"></el-table-column>
        <el-table-column prop="price" label="金额" width="120"></el-table-column>
      </el-table>
    </div>
    <el-dialog :append-to-body="true" :visible="rechargeVisible" @close="cancelRecharge">
      <el-form label-width="80px">
        <el-radio-group v-model="recharge.payway">
          <el-radio v-for="item in payWayShow" :label="item.id" :key="item.id">{{item.name}}</el-radio>
        </el-radio-group>
        <el-form-item label="充值金额">
          <el-input placeholder="请输入充值金额" v-model="recharge.amount"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="cancelRecharge">取 消</el-button>
        <el-button type="primary" @click="submitRecharge">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>
<script>
import { getPayWay, postRecharge, getUserInfo, getRestList } from "./api";

export default {
  data() {
    return {
      rest: "",
      restList: [],
      rechargeVisible: false,
      payWay: [],
      payWayShow: [],
      recharge: {
        payway: 0,
        amount: 0
      }
    };
  },
  created() {
    this.requestPayWay().then(() => this.getRestList());
    this.getRest();
  },
  methods: {
    activeRecharge() {
      this.rechargeVisible = true;
    },
    cancelRecharge() {
      this.rechargeVisible = false;
    },
    submitRecharge() {
      return postRecharge({
        payway: this.recharge.payway,
        amount: this.recharge.amount
      })
        .then(data => {
          this.cancelRecharge();
          this.$message({
            message: data.message,
            type: "success"
          });
          setTimeout(() => window.location.reload(), 2000)
        })
        .catch(rej => {
          this.cancelRecharge();
          this.$message({
            message: rej.data.message,
            type: "error"
          });
        });
    },
    getRest() {
      return getUserInfo()
        .then(data => (this.rest = data.data.rest + "元"))
        .catch(() => (this.rest = ""));
    },
    requestPayWay() {
      return getPayWay()
        .then(data => {
          this.payWayShow = data.payway.filter(item => item.id < 3)
          this.payWay = data.payway
        })
        .catch(rej => {
          this.$message({
            message: rej.data.message,
            type: "error"
          });
        });
    },
    getRestList() {
      return getRestList().then(data => {
        const payWayHash = this.payWay.reduce((prev, item) => {
          prev[item.id] = item.name;
          return prev;
        }, {});
        this.restList = data.restlist.map(item => {
          return {
            id: item.id,
            date: getLocalTime(item.createdate),
            type:
              item.payway == "3" && item.distribute != -1
                ? payWayHash[3] + " 课程分销号：" + item.distribute
                : payWayHash[item.payway],
            price: item.payway == "4" ? -item.amount : item.amount
          };
        });
      });
    }
  }
};

function getLocalTime(nS) {
  return new Date(parseInt(nS) * 1000)
    .toLocaleString()
    .replace(/:\d{1,2}$/, " ");
}
</script>

