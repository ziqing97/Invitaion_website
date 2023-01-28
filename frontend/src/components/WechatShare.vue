<template>
<div></div>
</template>

<script>
import axios from 'axios'
import wx from "weixin-js-sdk";
export default {
    name: 'WechatView',
    mounted() {
      this.getSignature();
    },

    props:{
      title: String,
      desc: String,
      picLoc: String,
    },

    methods:{
      getSignature () {
        var data = {'url': encodeURIComponent(location.href.split('#')[0])}
        axios.post('/wechat/apitoken', data).then(
        res => {
          wx.config({
            debug: false, // 开启调试模式,调用的所有 api 的返回值会在客户端 alert 出来
            appId: res['data']['appId'], // 必填，公众号的唯一标识
            timestamp: res['data']['timestamp'], // 必填，生成签名的时间戳
            nonceStr: res['data']['noncestr'], // 必填，生成签名的随机串
            signature: res['data']['signature'],// 必填，签名
            jsApiList: [
                'onMenuShareAppMessage',
                'onMenuShareTimeline',
                'updateTimelineShareData',
                'updateAppMessageShareData'
                ] // 必填，需要使用的 JS 接口列表
          });
          wx.ready(() => {
            var shareData = {
              title: this.title,
              desc: this.desc,
              link: location.href.split('#')[0], // 分享后的地址
              imgUrl: this.picLoc
            };
            //点击要去分享
            wx.updateAppMessageShareData(shareData);
            wx.updateTimelineShareData(shareData);
            wx.onMenuShareAppMessage(shareData);
            wx.onMenuShareTimeline(shareData);
          });
          wx.error(() => {
            alert('something wrong')
          });
          console.log('success')
        }
        ).catch(() => {
          console.log('error')
        })
      }
    }
  }
</script>
