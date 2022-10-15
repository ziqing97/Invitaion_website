<template>
  <div>
    <li id="all_inv_list" v-for="item in AllInvitation" v-bind:key="item">
      <router-link :to="{ name: 'InvitationRoute', params: { invitation_name: item }}">{{item}}</router-link>
    </li>
    
  </div>
  </template>
  
  <script>
  // import axios from 'axios'
  export default {
    name: 'AllInvitation',
    data(){
      return{
        AllInvitation:['yuziqing','liuliyi','longcheng']
      }
    }
  }
  </script>
  
  <style scoped>
  .all_inv_list{
    text-align: left;
  }
  </style>