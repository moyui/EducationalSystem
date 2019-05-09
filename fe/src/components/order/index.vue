<template>
  <el-table height="400" stripe border :data="orderList">
    <el-table-column
      prop="order"
      label="课程订单"
      width="150"
      fixed
      type="expand"
    >
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
    <el-table-column prop="price" label="价格" width="120"></el-table-column>
    <el-table-column prop="status" label="状态" width="120"></el-table-column>
    <el-table-column prop="operation" label="操作" width="120"></el-table-column>
  </el-table>
</template>
<script>
import { getOrderList } from "./api";

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
              operation: "go"
            };
          }))
      )
      .catch(rej => {
        this.$message({
          message: rej.data.message,
          type: "error"
        });
      });
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
