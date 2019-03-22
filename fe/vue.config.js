module.exports = {
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8888',
        ws: true,
        changeOrigin: true
      }
    }
  }
};
