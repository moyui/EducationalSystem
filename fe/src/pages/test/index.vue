<template>
  <el-container class="test" direction="vertical">
    <h2 class="title">期末测试</h2>
    <el-form>
      <el-form-item label="题目一">
        <p>问xxxxxxxx?</p>
        <el-radio-group v-model="answer[0]">
          <el-radio label="A">A</el-radio>
          <el-radio label="B">B</el-radio>
          <el-radio label="C">C</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="题目二">
        <p>问xxxxxxxx?</p>
        <el-input
          type="textarea"
          placeholder="请填写答案一"
          :autosize="{ minRows: 4, maxRows: 10 }"
          v-model="answer[1]"
        ></el-input>
      </el-form-item>
      <el-form-item label="题目三">
        <p>问xxxxxxxx?</p>
        <el-input
          type="textarea"
          placeholder="请填写答案二"
          :autosize="{ minRows: 4, maxRows: 10 }"
          v-model="answer[2]"
        ></el-input>
      </el-form-item>
    </el-form>
    <el-button type="primary" class="submit" @click="submitAnswer">提 交</el-button>
    <el-dialog :append-to-body="true" :visible="scoreAcvivity" @close="close">
      <h3>您的成绩是：</h3>
      <h2><em>{{score}}</em></h2>
      <p v-if="score > 60">恭喜您获得该课程的成就！请前往个人中心查看</p>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="close">确 定</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>
<script>
import Cookie from "js-cookie";
import { postAnswer, getQuestion } from "./api.js";

export default {
  props: ["courseid", "videoid"],
  data() {
    return {
      id: "",
      answer: [],
      scoreAcvivity: false,
      score: ""
    };
  },
  created() {
    getQuestion(this.courseid, "-1", this.videoid).then(
      res => (this.id = res.data.id)
    );
  },
  destroyed() {
    this.submitAnswer();
  },
  methods: {
    submitAnswer() {
      return postAnswer(this.courseid, this.id, this.answer).then(res => {
        this.score = res.data.score;
        this.scoreAcvivity = true;
      });
    },
    close() {
      this.scoreAcvivity = false;
      this.$router.push('/center')
    }
  }
};
</script>
<style lang="less" scoped>
.title {
  margin-top: 10px;
}
.test {
  padding: 0 500px;
  height: calc(100% - 60px);
  margin-top: 60px;
  width: 100%;
}
</style>
