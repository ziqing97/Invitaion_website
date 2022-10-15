const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  publicPath: './',
  devServer: {
    proxy: "http://47.100.131.89:80",
  },
  configureWebpack: {
    devtool: 'source-map'
  },
  publicPath:'./'
})
