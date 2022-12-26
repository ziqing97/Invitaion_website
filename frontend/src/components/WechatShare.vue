<template>
  <div>
    <div>{{timestamp}}</div>
    <div>{{noncestr}}</div>
    <div>{{apiToken}}</div>
    <div>{{signature}}</div>
  </div>
</template>

<script>
import axios from 'axios'
import wx from "weixin-js-sdk";
//import { shares } from '@/api/index'
export default {
    name: 'WechatShare',
    data(){
      return{
        apiId: "wxbc77294cc827500b",
        noncestr: "",
        timestamp: null,
        apiToken: null,
        signature: null
      }
    },

    props: {
      domainSuffix: String
    },

    mounted () {
      this.getShareInfo()
    },

    computed:{
      Timestamp () {
        return Date.now()
      },
    },
    methods:{
      getToken () {
        this.noncestr = this.genNoncestr()
        this.timestamp =  this.genTimestamp()
        var data = {'appid':this.apiId, 'noncestr': this.noncestr, 'timestamp': this.timestamp, 'domainSuffix': this.domainSuffix}
        axios.post('/wechat/apitoken', data).then(
        res => {
          this.signature = res
          // eslint-disable-next-line
          console.log(res)
        }
        ).catch(res => {
          // eslint-disable-next-line
          console.log(res)
        })
      },

      /*initConfig(){
        return new Promise((resolve) => {
        wx.config({
          debug: false,
          appId: this.appId,
          timestamp: this.timestamp,
          nonceStr: this.nonceStr,
          signature: this.signature,
          jsApiList: this.jsApiList ?? [
            'updateTimelineShareData',
            'updateAppMessageShareData',
          ],
          openTagList: [],
        })
        wx.ready(() => {
          resolve(true)
        })
      })
      },

      setShareInfo(shareInfo, onSuccess) {
        wx.updateTimelineShareData({
          title: shareInfo.title, // 分享标题
          link: shareInfo.link, // 分享链接，可以不是当前页面，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
          imgUrl: shareInfo.imgUrl,
          success: function () {
            // 用户确认分享后执行的回调函数
            onSuccess()
          },
        })
        wx.updateAppMessageShareData({
          title: shareInfo.title, // 分享标题
          desc: shareInfo.desc,
          link: shareInfo.link, // 分享链接，可以不是当前页面，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
          imgUrl: shareInfo.imgUrl,
          type: 'link', // 分享类型,music、video或link，不填默认为link
          success: function () {
            // 用户确认分享后执行的回调函数
            onSuccess()
          },
        })
      },

      useWxShare() {
        var link = 'http://www.junnuolc.cn'+'/'+this.domainSuffix
        link = 'http://www.junnuolc.cn'+'/'+'invitation_longcheng'
        var imgUrl = ''
        var shareConfig = {'title':"邀请函",'desc':'给您的邀请函','link':link,'imgUrl':imgUrl}
        this.initConfig().then(() => {
          this.setShareInfo(shareConfig);
        });
      },*/
      getShareInfo() {
        this.getToken();
        /*this.save = {
            url: location.href.split('#')[0] // 只需要传当前页面地址
          };*/
        //shares(this.save).then(res => {
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
            link: 'http://www.junnuolc.cn/invitation_longcheng', // 分享后的地址
            imgUrl:
              ''
          };
          //点击要去分享
          wx.updateAppMessageShareData(shareData);
          wx.updateTimelineShareData(shareData);
        });
        //});
      },

      genTimestamp () {
        return Date.now()
      },

      genNoncestr () {
        var str = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
          var res = "";
          for(var i = 0; i < 16 ; i ++) {
            var id = Math.ceil(Math.random()*35);
            res += str[id];
          }
          return res;
      }
    }
  }
</script>
