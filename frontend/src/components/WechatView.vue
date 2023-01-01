<template>
  <div>
    <div>{{ apiId }}</div>
    <div>{{ nonceStr }}</div>
    <div>{{ timestamp }}</div>
    <div>{{ signature }}</div>
    <div>{{ url }}</div>
  </div>
</template>

<script>
import axios from 'axios'
import wx from "weixin-js-sdk";
//import { shares } from '@/api/index'
export default {
    name: 'WechatView',
    data(){
      return {
        apiId: 'wxbc77294cc827500b',
        nonceStr: '',
        timestamp: '',
        signature: '',
        url:'',
      };
    },

    mounted() {
      this.getShareInfo();
    },
    
    methods:{
      getUrl(){
        this.url = encodeURIComponent(window.location.href.split('#')[0]);
      },

      genNoncestr(){
          var str = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
          var res = "";
          for(var i = 0; i < 16 ; i ++) {
            var id = Math.ceil(Math.random()*35);
            res += str[id];
          }
          this.nonceStr = res
      },

      genTimestamp () {
        this.timestamp = Math.ceil(Date.now()/1000).toString()
      },

      getToken () {
        this.genNoncestr()
        this.genTimestamp()
        this.getUrl()
        var data = {'appid':this.apiId, 'nonceStr': this.nonceStr, 
                    'timestamp': this.timestamp, 'url': this.url} 
        axios.post('/wechat/apitoken', data).then(
        res => {
          this.signature = res['data']
          console.log(res)
        }
        ).catch(res => {
          console.log(res)
        })
      },

      getShareInfo() {
        this.getToken();
        alert(location.href.split('#')[0])
        wx.config({
          debug: true, // 开启调试模式,调用的所有 api 的返回值会在客户端 alert 出来，若要查看传入的参数，可以在 pc 端打开，参数信息会通过 log 打出，仅在 pc 端时才会打印。
          appId: this.apiId, // 必填，公众号的唯一标识
          timestamp: this.timestamp, // 必填，生成签名的时间戳
          nonceStr: this.nonceStr, // 必填，生成签名的随机串
          signature: this.signature,// 必填，签名
          jsApiList: [
              'updateTimelineShareData', // 分享到朋友
              'updateAppMessageShareData'
              ] // 必填，需要使用的 JS 接口列表
        });

        /*wx.ready(() => {
          var shareData = {
            title: '邀请函',
            desc: '给您的邀请函',
            link: 'http://www.junnuolc.cn/test', // 分享后的地址
            imgUrl:
              ''
          };
          //点击要去分享
          wx.updateAppMessageShareData(shareData);
          wx.updateTimelineShareData(shareData);
        });*/
      },
    }
  }
</script>
