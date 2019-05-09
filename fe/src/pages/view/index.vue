<template>
  <el-main class="view" v-if="view.basic">
    <el-breadcrumb separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/?' }">小学</el-breadcrumb-item>
      <el-breadcrumb-item>{{view.basic.name}}</el-breadcrumb-item>
    </el-breadcrumb>
    <div class="view__header">
      <img v-if="view.basic.logo" :src="view.basic.logo">
      <div class="view__header_meta">
        <div class="view__title-wrap">
          <h3 class="view__title">{{view.basic.name}}</h3>
          <!-- <el-rate v-model="rateValue" allow-half show-score @change="rateChange"></el-rate> -->
        </div>
        <div class="view__buy">
          <span>购买人数：{{view.basic.total}}人</span>
          <span class="view__favour">好评度：{{favourRate}}</span>
          <!-- <el-button class="view__favour el-icon-star-off" size="small">收藏</el-button> -->
        </div>
        <p class="view__info">{{view.basic.info}}</p>
        <p class="view__extra-info">{{view.basic.extra_info}}</p>
        <span class="view__price">￥{{view.basic.price}}</span>
        <div>
          <template v-if="!view.detail.isbought">
            <el-button v-if="view.basic.price > 0" type="primary" plain @click="order">立即购买</el-button>
            <el-button v-else type="primary" plain>立即订阅</el-button>
          </template>
          <el-button
            v-else
            type="primary"
            plain
            @click="goToVideo(view.detail.menu[0].video[0].id, view.basic.id)"
          >学习课程</el-button>
          <el-button
            v-if="canTest"
            type="warning"
            plain
            @click="goToVideo(view.detail.menu[0].video[0].id, view.basic.id)"
          >开始测试</el-button>
          <el-button>咨询</el-button>
        </div>
      </div>
    </div>
    <div class="view__detail">
      <el-tabs v-model="activeIndex" class="view__tabs" tab-position="left">
        <el-tab-pane label="目录" name="1">
          <div v-for="(item, key) in view.detail.menu" :key="key">
            <h5 class="video__menu-title">{{key + 1}} {{item.title}}</h5>
            <el-card
              class="video__menu-card"
              v-for="(video, videokey) in item.video"
              :key="videokey"
            >
              <div class="video__menu-content" @click="goToVideo(video.id, view.basic.id)">
                <img :src="view.basic.logo" class="video__menu-img">
                <div class="video__menu-meta">
                  <span class="video__unit-title">{{video.title}}</span>
                  <span class="video__unit-total">总时长：{{sToHs(parseInt(video.totaltime))}}</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-tab-pane>
        <el-tab-pane label="评论" name="2">
          <div class="comment__wrap">
            <div class="comment">
              <div class="editor__bound" ref="editorBound">
                <quillEditor
                  v-model="comment"
                  ref="myQuillEditor"
                  :options="editorOption"
                  class="editor"
                ></quillEditor>
              </div>
              <el-button type="primary" class="launch-comment" @click="requestCommentPost">发表评论</el-button>
            </div>
            <template v-if="commentList.length > 0 && isLogin">
              <h5>您的评论</h5>
              <el-card>
                <div class="comment-content">
                  <span class="comment-username">您</span>
                  <div
                    class="comment-usercontent"
                    v-html="commentList[0].content"
                  >{{commentList[0].content}}</div>
                  <span class="comment-date">发表时间： {{getLocalTime(commentList[0].createdate)}}</span>
                  <div class="comment-add-content" v-if="commentList[0].addcontent">
                    <h6>您的追评</h6>
                    <div
                      class="comment-usercontent"
                      v-html="commentList[0].addcontent"
                    >{{commentList[0].addcontent}}</div>
                    <span class="comment-date">发表时间： {{getLocalTime(commentList[0].modifydate)}}</span>
                  </div>
                  <template v-else>
                    <el-button @click="activeAddComment" v-if="!addCommentStatus">追评</el-button>
                    <div class="comment" v-if="addCommentStatus">
                      <div class="editor__bound" ref="editorBound">
                        <quillEditor
                          v-model="addComment"
                          ref="myQuillEditor"
                          :options="addEditorOption"
                          class="editor"
                        ></quillEditor>
                      </div>
                      <el-button
                        type="primary"
                        class="launch-comment"
                        @click="requestAddComment(commentList[0].id)"
                      >发表追评</el-button>
                    </div>
                  </template>
                </div>
              </el-card>
              <el-divider></el-divider>
            </template>
            <el-card v-for="item in commentList" :key="item.id">
              <div class="comment-content">
                <span class="comment-username">{{item.username}}</span>
                <div class="comment-usercontent" v-html="item.content">{{item.content}}</div>
                <span class="comment-date">发表时间： {{getLocalTime(item.createdate)}}</span>
                <div class="comment-add-content" v-if="item.addcontent">
                  <h6>追评</h6>
                  <div class="comment-usercontent" v-html="item.addcontent">{{item.addcontent}}</div>
                  <span class="comment-date">发表时间： {{getLocalTime(item.modifydate)}}</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-tab-pane>
      </el-tabs>
      <el-card class="view__card">
        <div slot="header">
          <h4 class="teacher__name">{{view.teacher.name}}</h4>
        </div>
        <el-row>
          <el-col :span="8">
            <div class="teacher__meta">
              <p>好评度</p>
              <span>{{favourRate}}</span>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="teacher__meta">
              <p>课程数</p>
              <span>{{view.teacher.has_total}}</span>
            </div>
          </el-col>
          <el-col :span="8">
            <div class="teacher__meta">
              <p>学习人次</p>
              <span>{{view.teacher.learning_total}}</span>
            </div>
          </el-col>
        </el-row>
        <p class="teacher__info">{{view.teacher.info}}</p>
        <div class="teacher__connect">
          <p>联系方式</p>
          <div v-for="item in view.teacher.connect" :key="item.type" class="connect">
            <el-tag type="info">{{item.type}}</el-tag>
            <span>{{item.value}}</span>
          </div>
        </div>
      </el-card>
    </div>
  </el-main>
</template>
<script>
import {
  getView,
  postOrder,
  getComment,
  postComment,
  postAddComment,
  getCanTest
} from "./api";
import { setTimeout } from "timers";
import "quill/dist/quill.core.css";
import "quill/dist/quill.snow.css";
import "quill/dist/quill.bubble.css";

import { quillEditor } from "vue-quill-editor";

export default {
  props: ["id"],
  components: { quillEditor },
  data() {
    return {
      view: {},
      activeIndex: "1",
      rateValue: null,
      comment: "",
      addComment: "",
      editorOption: {
        bounds: this.$refs.editorBound || document.body,
        placeholder: "请输入您的评论",
        themes: "Snow",
        modules: {
          toolbar: [
            ["blockquote", "code-block"],
            [{ header: 1 }, { header: 2 }],
            [{ indent: "-1" }, { indent: "+1" }],
            [{ script: "sub" }, { script: "super" }],
            ["clean"]
          ]
        }
      },
      addEditorOption: {
        bounds: this.$refs.editorBound || document.body,
        placeholder: "请输入您的追评",
        themes: "Snow",
        modules: {
          toolbar: [
            ["blockquote", "code-block"],
            [{ header: 1 }, { header: 2 }],
            [{ indent: "-1" }, { indent: "+1" }],
            [{ script: "sub" }, { script: "super" }],
            ["clean"]
          ]
        }
      },
      commentList: [],
      addCommentStatus: false,
      canTest: false
    };
  },
  created() {
    this.requestView();
    this.requestCommentGet();
    this.requestCanTest();
  },
  computed: {
    favourRate() {
      if (this.view.basic.total == 0) return "暂无数据";
      else return this.view.basic.favour / this.view.basic.total + "%";
    },
    isLogin() {
      return this.$store.state.login;
    }
  },
  methods: {
    requestView() {
      return getView(this.id).then(data => {
        this.view = data.data;
      });
    },
    rateChange() {
      this.$message({
        title: "感谢评价",
        message: "您的评价我们已经收到~",
        type: "success"
      });
    },
    requestCommentGet() {
      return getComment(this.id)
        .then(data => {
          this.commentList = data.comment;
        })
        .catch(rej => {
          if (rej.data && rej.data.message) {
            this.$message({
              message: rej.data.message,
              type: "error"
            });
          }
        });
    },

    requestCommentPost() {
      return postComment({ courseid: this.id, comment: this.comment })
        .then(() => {
          this.$message({
            message: "发表评论成功",
            type: "success"
          });
        })
        .catch(rej => {
          if (rej.data && rej.data.message) {
            this.$message({
              message: rej.data.message,
              type: "error"
            });
          }
        });
    },

    activeAddComment() {
      this.addCommentStatus = true;
    },

    requestAddComment(addbelongid) {
      return postAddComment({
        courseid: this.id,
        comment: this.addComment,
        addbelongid: addbelongid
      })
        .then(() => {
          this.$message({
            message: "发表追评成功",
            type: "success"
          });
        })
        .catch(rej => {
          if (rej.data && rej.data.message) {
            this.$message({
              message: rej.data.message,
              type: "error"
            });
          }
        });
    },

    requestCanTest() {
      return getCanTest(this.id).then(data => (this.canTest = data.data.cantest));
    },

    order() {
      return postOrder(this.id)
        .then(data => {
          if (data.status == 1) {
            this.$store.commit("SET_ORDER_INFO", {
              id: this.view.basic.id,
              name: this.view.basic.name,
              img: this.view.basic.logo,
              teacher: this.view.teacher.name,
              price: this.view.basic.price
            });
            this.$store.commit("SET_ORDER_VISIBLE", true);
          } else {
            this.$store.commit("SET_ORDER_VISIBLE", false);
          }
        })
        .catch(rej => {
          this.$store.commit("SET_ORDER_VISIBLE", false);
          this.$message({
            message: rej.data.message,
            type: "error"
          });
          if (rej.data.status == 2) {
            setTimeout(
              () => this.$store.commit("SET_LOGIN_VISIBLE", true),
              2000
            );
          }
        });
    },
    goToVideo(videoid, courseid) {
      const { href } = this.$router.resolve({
        path: `/view/${courseid}/video/${videoid}`
      });
      window.open(href, "_blank");
    },
    sToHs(s) {
      var h;
      h = Math.floor(s / 60);
      //计算秒
      //算法：取得秒%60的余数，既得到秒数
      s = s % 60;
      //将变量转换为字符串
      h += "";
      s += "";
      //如果只有一位数，前面增加一个0
      h = h.length == 1 ? "0" + h : h;
      s = s.length == 1 ? "0" + s : s;
      return h + ":" + s;
    },
    getLocalTime(nS) {
      return new Date(parseInt(nS) * 1000)
        .toLocaleString()
        .replace(/:\d{1,2}$/, " ");
    }
  }
};
</script>
<style lang="less" scope>
.view {
  width: 100%;
  margin-top: 60px;
  padding: 20px 40px;
  margin-bottom: 60px;
  .view__header {
    display: flex;
    flex-direction: row;
    margin-top: 20px;
    img {
      width: 600px;
      height: 338px;
    }
    .view__header_meta {
      display: flex;
      flex-direction: column;
      flex: 1;
      padding-left: 50px;
      .view__title-wrap {
        display: flex;
        flex-direction: row;
        align-items: center;
        .view__title {
          font-weight: normal;
          font-size: 22px;
          height: 40px;
          line-height: 40px;
          margin-right: 10px;
        }
      }

      .view__buy {
        color: #999999;
        font-size: 14px;
        margin-top: 10px;
        display: flex;
        flex-direction: row;
        align-items: center;
        .view__favour {
          margin-left: 50px;
        }
      }
      .view__info {
        font-size: 16px;
        margin-top: 10px;
        padding-left: 10px;
        height: 30px;
        line-height: 30px;
      }
      .view__extra-info {
        font-size: 14px;
        margin-top: 5px;
      }
      .view__price {
        font-size: 22px;
        color: #e85308;
        height: 80px;
        line-height: 80px;
      }
    }
  }
  .view__detail {
    margin-top: 20px;
    display: flex;
    flex-direction: row;
    width: 100%;
    .view__tabs {
      width: 70%;
    }
    .view__card {
      flex: 1;
      margin-left: 50px;
    }
  }
  .teacher__name {
    font-size: 16px;
    text-align: left;
    font-weight: normal;
  }
  .teacher__meta {
    display: flex;
    flex-direction: column;
    align-items: center;
    p {
      font-size: 14px;
      height: 24px;
      line-height: 24px;
    }
    span {
      font-size: 14px;
      color: #999999;
    }
  }
  .teacher__info {
    font-size: 14px;
    margin-top: 20px;
  }
  .teacher__connect {
    margin-top: 50px;
    p {
      font-size: 16px;
    }
    .connect {
      height: 50px;
      line-height: 50px;
      margin-top: 10px;
      span {
        margin-left: 10px;
        font-size: 14px;
      }
    }
  }
  .video__menu-title {
    font-weight: normal;
    font-size: 20px;
    margin-bottom: 20px;
  }
  .video__menu-card {
    margin-bottom: 10px;
  }
  .video__menu-img {
    width: 120px;
    height: 80px;
  }
  .video__menu-meta {
    display: flex;
    flex-direction: column;
    margin-left: 60px;
    flex: 1;
  }
  .video__menu-content {
    display: flex;
    flex-direction: row;
  }
  .video__unit-title {
    font-size: 18px;
  }
  .video__unit-total {
    color: #999999;
    margin-top: 5px;
  }
  .comment__wrap {
    padding: 0 20px;
  }
  .comment {
    display: flex;
    flex-direction: row;
    padding: 20px 0;
    .editor__bound {
      flex: 1;
    }
    .launch-comment {
      margin-left: 30px;
    }
  }
  .comment-content {
    display: flex;
    flex-direction: column;
    .comment-username {
      font-weight: 600;
      font-size: 14px;
    }
    .comment-usercontent {
      font-size: 14px;
      text-indent: 20px;
      margin-top: 10px;
    }
    .comment-date {
      width: 100%;
      text-align: right;
    }
  }
}
</style>


