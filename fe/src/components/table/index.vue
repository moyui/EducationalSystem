<template>
  <div>
    <h5>课程表</h5>
    <el-table height="400" stripe border :data="table">
      <el-table-column type="expand" label="详细信息" width="100">
        <template slot-scope="props">
          <el-table :data="props.row.video">
            <el-table-column prop="title" label="视频名称" width="150"></el-table-column>
            <el-table-column prop="totaltime" label="时长" width="150"></el-table-column>
            <el-table-column prop="isWatch" label="已观看" width="150"></el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column prop="coursename" label="课程名称" width="450"></el-table-column>
    </el-table>
  </div>
</template>
<script>
import { getTable } from "./api";

export default {
  data() {
    return {
      table: []
    };
  },
  created() {
    getTable().then(res => (this.table = res.data));
  }
};
</script>