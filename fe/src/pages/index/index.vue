<template>
  <el-container class="index" v-if="indexVisible">
    <el-menu
      :default-active="groupActiveIndex"
      v-if="group.length > 0"
      class="course__nav"
      @select="selectGroup"
      text-color="#545c64"
      active-text-color="#545c64"
    >
      <el-menu-item v-for="item in group" :key="item.id" :index="item.id.toString()" class="nav_li">
        <span slot="title" class="nav_text">{{item.name}}</span>
      </el-menu-item>
    </el-menu>
    <el-main class="main">
      <el-tabs
        v-model="variteyActiveIndex"
        v-if="showVariety.length > 0"
        @tab-click="requestList()"
      >
        <el-tab-pane
          v-for="item in showVariety"
          :label="item.name"
          :name="item.id.toString()"
          :key="item.id"
          class="course__warp"
        >
          <template v-if="list.length > 0">
            <div
              v-for="item in list"
              :key="item.id"
              class="course__unit"
              @click="goToView(item.id)"
            >
              <img :src="item.logo">
              <h4 class="course__title">{{item.name}}</h4>
              <div class="course__meta">
                <span class="course__price">￥{{item.price}}</span>
                <span class="course__teacher">{{item.teacher}}</span>
              </div>
            </div>
          </template>
        </el-tab-pane>
      </el-tabs>
      <div v-else class="no-data">
        <span>很抱歉、目前暂无数据</span>
      </div>
    </el-main>
  </el-container>
</template>
<script>
import { getClassify, getList } from "./api";

export default {
  data() {
    return {
      groupActiveIndex: "1",
      variteyActiveIndex: "1",
      indexVisible: false,
      group: [],
      variety: [],
      list: []
    };
  },
  created() {
    this.requestClassify();
    this.requestList();
  },
  computed: {
    showVariety() {
      return this.variety.filter(
        item => item.group_id == this.groupActiveIndex
      );
    }
  },
  methods: {
    requestClassify() {
      return getClassify()
        .then(data => {
          this.group = data.data.group;
          this.variety = data.data.variety;
          this.indexVisible = true;
        })
        .catch(rej => console.log(rej));
    },
    requestList() {
      return getList(this.variteyActiveIndex)
        .then(data => {
          this.list = data.list;
        })
        .catch(rej => console.log(rej));
    },
    selectGroup(index) {
      this.groupActiveIndex = index;
    },
    goToView(id) {
      this.$router.push({ path: `/view/${id}` });
    }
  }
};
</script>
<style lang="less" scoped>
.index {
  height: calc(100% - 60px);
  margin-top: 60px;
  width: 100%;
  // background-color: #C8E8FF;
}
.course__nav {
  margin-top: 20px;
  width: 20%;
  background-color: #c8e8ff;
}
.el-tabs__nav-scroll {
  display: flex;
  flex-direction: row;
  justify-content: center;
  height: 50px;
  .el-tabs__item {
    height: 100%;
    line-height: 50px;
    font-size: 16px;
  }
}
.el-tabs__nav-wrap::after {
  content: none;
}
.course__warp {
  display: flex;
  flex-direction: row;
  align-content: flex-start;
  justify-content: space-around;
  .course__unit {
    width: 28%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: #f4f4f4;
    padding: 20px;
    border-radius: 10px;
    
    img {
      width: 100%;
    }
    .course__title {
      font-size: 16px;
      font-weight: normal;
      margin: 10px 0 5px;
      width: 100%;
      text-align: left;
    }
    .course__meta {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      .course__price {
        color: #e53808;
        font-size: 16px;
      }
      .course__teacher {
        color: #909399;
        font-size: 12px;
      }
    }
  }
}
.no-data {
  font-size: 16px;
  width: 300px;
  height: 200px;
  position: relative;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 22px;
}
.nav_li {
  text-align: center;
  font-size: 16px;
  font-weight: 700;
}
.nav_li:hover {
  background: #91d1fe;
}
.main {
  width: calc(100% - 300px);
}
</style>

