<template>
  <el-table height="400" stripe border :data="orderList">
    <el-table-column prop="order" label="课程订单" width="150" fixed type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="order-table-expand">
          <el-form-item label="订单日期">
            <span>{{ props.row.createdate }}</span>
          </el-form-item>
          <el-form-item label="课程名称">
            <span>{{ props.row.name }}</span>
          </el-form-item>
          <el-form-item label="订单号">
            <span>{{ props.row.id }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column prop="price" label="价格" width="200"></el-table-column>
    <el-table-column prop="status" label="状态" width="200"></el-table-column>
    <el-table-column label="操作" width="300">
      <template slot-scope="scope">
        <el-button @click="addDistribute(scope.row.id)">课程分销</el-button>
        <el-button v-if="scope.row.statusid != 4" type="danger" @click="addwithdraw(scope.row.id)">退 课</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
import { getOrderList, distribute, withdraw } from "./api";

export default {
  data() {
    return {
      orderList: []
    };
  },
  created() {
    getOrderList()
      .then(
        data =>
          (this.orderList = data.orderlist.map(item => {
            return {
              id: item.id,
              name: item.coursename,
              createdate: getLocalTime(item.createdate),
              price: item.price,
              status: item.statusname,
              statusid: item.statusid
            };
          }))
      )
      .catch(rej => {
        this.$message({
          message: rej.data.message,
          type: "error"
        });
      });
  },
  methods: {
    addDistribute(id) {
      return distribute(id).then(data => {
        this.$message({
          message: "课程分销成功，请前往售后模块查看分销链接",
          type: "success"
        });
      });
    },
    addwithdraw(id) {
      console.log(id)

      return withdraw(id)
        .then(data => {
          this.$message({
            message: "课程退课成功，请前往我的余额查看详情",
            type: "success"
          });
        })
        .catch(rej => {
          this.$message({
            message: rej.data.message,
            type: "error"
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

<style lang="less">
.order-table-expand {
  font-size: 0;
}
.order-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.order-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
</style>
