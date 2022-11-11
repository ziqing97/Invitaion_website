<template>
  <div>
    <wechat-share domainSuffix='AllInvitation'></wechat-share>
  </div>
  <div>
    <li id="all_inv_list" v-for="item in Invitation" v-bind:key="item">
      <router-link :to="{ name: 'InvitationRoute', params: { invitation_name: item.invitation_id }}">{{ item.invitation_time }}: {{item.guest_name }}</router-link><br/>
    </li>
  </div>
  </template>
  
  <script>
  import axios from 'axios'
  import WechatShare from  '@/components/WechatShare.vue'
  export default {
    name: 'AllInvitation',
    components: { WechatShare },
    data(){
      return{
        Invitation: {}
      }
    },
    mounted () {
      this.getAllInvi()
    },
    methods:{
      getAllInvi () {
        axios.get('/invitation/all').then(
        res => {
          this.Invitation = res.data
          // eslint-disable-next-line
          console.log(res)
        }
        ).catch(res => {
          // eslint-disable-next-line
          console.log(res)
        })
      }
      
    }
  }
  </script>
  
  <style scoped>
  .all_inv_list{
    text-align: left;
  }
  </style>