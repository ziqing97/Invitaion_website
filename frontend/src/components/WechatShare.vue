<template>
    <div>{{ apiToken }}</div>
    <div>{{ apiId }}</div>
    <div>{{ domainSuffix }}</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'WechatShare',
    data(){
      return{
        apiId: "wxf28427bb825d7a37",
        apiToken: null
      }
    },

    props: {
      domainSuffix: String
    },

    mounted () {
      this.getToken()
    },

    computed:{
      Timestamp () {
        return Date.now()
      },
    },
    methods:{
      getToken () {
        var data = {'appid':this.apiId, 'noncestr': this.genNoncestr(), 'timestamp': this.genTimestamp(), 'domainSuffix': this.domainSuffix}
        axios.post('/wechat/apitoken', data).then(
        res => {
          this.appToken = res
          // eslint-disable-next-line
          console.log(res)
        }
        ).catch(res => {
          // eslint-disable-next-line
          console.log(res)
        })
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
