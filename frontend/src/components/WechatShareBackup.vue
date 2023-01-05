<template>
  <div>
    <div>{{ nonceStr }}</div>
    <div>{{ timestamp }}</div>
    <div>{{ signature }}</div>
  </div>
</template>

<script>
import axios from 'axios'
import wx from "weixin-js-sdk";
//import { shares } from '@/api/index'
export default {
    name: 'WechatShare',
    data(){
      return {
        apiId: "wxbc77294cc827500b",
        noncestr: "a",
        timestamp: null,
        signature: null
      };
    },

    props: {
      domainSuffix: String
    },

    mounted() {
      this.Noncestr();
    },
    
    methods:{
      Noncestr(){
          var str = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
          var res = "";
          for(var i = 0; i < 16 ; i ++) {
            var id = Math.ceil(Math.random()*35);
            res += str[id];
          }
          this.noncestr = res
      },

      genTimestamp () {
        return this.timestamp;
      },

      genNoncestr () {
        var str = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
          var res = "";
          for(var i = 0; i < 16 ; i ++) {
            var id = Math.ceil(Math.random()*35);
            res += str[id];
          }
          return res;
      },

      getToken () {
        this.nonceStr = this.genNoncestr()
        this.timestamp = this.genTimestamp()
        var data = {'appid':this.apiId, 'noncestr': this.nonceStr, 
                    'timestamp': this.timestamp, 'domainSuffix': this.domainSuffix} 
        axios.post('/wechat/apitoken', data).then(
        res => {
          this.signature = res
          console.log(res)
        }
        ).catch(res => {
          console.log(res)
        })
      },

      getShareInfo() {
        this.getToken();
        wx.config({
          debug: true,
          appId: this.appId,  // appID 公众号的唯一标识
          timestamp: this.timestamp, // 生成签名的时间戳
          nonceStr: this.nonceStr, //  生成签名的随机串
          signature: this.signature, // 生成的签名
          jsApiList: [
            'updateAppMessageShareData', // 分享到朋友
            'updateTimelineShareData', // 分享到朋友圈
          ]
        });

        wx.ready(() => {
          var shareData = {
            title: '邀请函',
            desc: '给您的邀请函',
            link: 'http://www.junnuolc.cn/invitation_longcheng/', // 分享后的地址
            imgUrl:
              ''
          };
          //点击要去分享
          wx.updateAppMessageShareData(shareData);
          wx.updateTimelineShareData(shareData);
        });
        //});
      },
    }
  }
</script>
