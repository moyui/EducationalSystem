<template>
  <el-container id="app">
    <customHeader></customHeader>
    <router-view></router-view>
    <customFooter></customFooter>
    <auth></auth>
    <order></order>
  </el-container>
</template>

<script>
const customHeader = () => import("./components/header/index.vue");
const customFooter = () => import("./components/footer/index.vue");
const auth = () => import("./components/auth/index.vue");
const order = () => import("./components/purchase/index.vue");

export default {
  name: "app",
  components: { customHeader, customFooter, auth, order }
};
</script>
<style lang="less">
body,
ol,
ul,
h1,
h2,
h3,
h4,
h5,
h6,
p,
th,
td,
dl,
dd,
form,
fieldset,
legend,
input,
textarea,
select {
  margin: 0;
  padding: 0;
}
body {
  font: 12px "PingFangSC-Regular";
  -webkit-text-size-adjust: 100%;
}
html,
body {
  height: 100%;
}
a {
  text-decoration: none;
}
a:hover {
  text-decoration: none;
}
em {
  font-style: normal;
}
li {
  list-style: none;
}
img {
  border: 0;
  vertical-align: middle;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
p {
  word-wrap: break-word;
}
#app {
  height: 100%;
  width: 100%;
}
</style>
