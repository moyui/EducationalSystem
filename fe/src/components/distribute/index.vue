<template>
  <div>
    <div>
      <h5>课程分销</h5>
      <el-table height="400" stripe border :data="data">
        <el-table-column width="150" type="expand">
          <template slot-scope="props">
            <el-table :data="props.row.detail">
              <el-table-column prop="username" label="下单人" width="150"></el-table-column>
              <el-table-column prop="income" label="获得收入" width="150"></el-table-column>
              <el-table-column prop="radio" label="提成比例" width="150"></el-table-column>
              <el-table-column prop="createdate" label="下单日期" width="150">
                <template slot-scope="date">{{getLocalTime(date.row.createdate)}}</template>
              </el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <el-table-column prop="coursename" label="课程名" width="200"></el-table-column>
        <el-table-column prop="link" label="分享编号" width="300"></el-table-column>
        <el-table-column label="操作" width="150">
          <template slot-scope="scope">
            <el-button type="danger" @click="cancel(scope.row.id)">取 消</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>
<script>
import { getDistribution, closeDistribution } from "./api";

export default {
  data() {
    return {
      data: []
    };
  },
  created() {
    getDistribution().then(res => (this.data = res.back));
  },
  methods: {
    cancel(id) {
      closeDistribution(id).then(data => {
        this.$message({
          message: '取消成功',
          type: "success"
        });
      });
    },
    getLocalTime(nS) {
      console.log(nS);
      return new Date(parseInt(nS) * 1000)
        .toLocaleString()
        .replace(/:\d{1,2}$/, " ");
    }
  }
};
</script>

