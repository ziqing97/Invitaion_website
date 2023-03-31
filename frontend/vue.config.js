const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  //publicPath: '/static/',
  assetsDir: "static",
  transpileDependencies: true,
  pages: {
    index: {
      entry: 'src/main.js',
      filename: 'index.html',
      title: '邀请函'
    }
  },
})
