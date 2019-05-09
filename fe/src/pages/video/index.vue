<template>
  <el-container class="video__wrap">
    <el-main class="video__main">
      <d-player v-if="videoVisible && !dialogVisible" :options="playerOptions"></d-player>
      <div class="video__ar">
        <img src="../../assets/HIRO.jpg" class="dingwei">
        <el-alert
          title="AR课件使用提示"
          type="success"
          description="用手机浏览器（推荐微信浏览器）扫描下方二维码后再对准上方识别区即可查看AR课件"
          show-icon
          close-text="知道了"
        ></el-alert>
        <img src="../../assets/qrcode.png" class="qrcode">
      </div>
    </el-main>
    <el-dialog title="阻止收看" :visible.sync="dialogVisible" width="30%">
      <span>你可能未登录或者未购买</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="backToView">确 定</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>
<script>
import VueDPlayer from "vue-dplayer";
import "vue-dplayer/dist/vue-dplayer.css";
import { getVideo, postProgress } from "./api";

export default {
  props: ["videoid", "courseid"],
  data() {
    return {
      playerOptions: {
        autoplay: true,
        lang: "zh-cn",
        video: {
          url: "",
          pic: ""
        }
      },
      videoVisible: false,
      dialogVisible: false
    };
  },
  components: {
    "d-player": VueDPlayer
  },
  created() {
    this.requestVideo();
    postProgress({ videoid: this.videoid, courseid: this.courseid });
  },
  methods: {
    requestVideo() {
      return getVideo({ videoid: this.videoid, courseid: this.courseid })
        .then(data => {
          this.playerOptions.video = {
            url: data.data.url,
            pic: data.data.picurl
          };
          this.videoVisible = true;
        })
        .catch(rej => {
          if (rej.data && rej.data.message) {
            this.$message({
              message: rej.data.message,
              type: "error"
            });
          }
          if (rej.status == 401) {
            this.dialogVisible = true;
          }
        });
    },
    backToView() {
      this.$router.push({ path: `/view/${this.courseid}` });
    }
  }
};
</script>
<style lang="less">
.video__wrap {
  width: 100%;
  margin-top: 60px;
  margin-bottom: 60px;
  padding: 0 20px;
}

.video__main {
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  .dplayer {
    width: 75%;
    height: calc(100vh - 160px);
  }

  .video__ar {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    margin-left: 20px;

    .dingwei {
      width: 300px;
    }
    .qrcode {
      margin-top: 20px;
      margin-right: 50px;
    }
  }
}
</style>

