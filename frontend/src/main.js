import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import Vue3TouchEvents from "vue3-touch-events";
import wx from "weixin-js-sdk";

const app = createApp(App)
app.use(router)
app.use(Vue3TouchEvents)
app.config.globalProperties.$wxsdk=wx
app.mount('#app')
