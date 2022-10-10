<template>
  <div id="message">
    尊敬的贵宾：您好！<br/>
    诚邀出席 <br/>
    贵宾：{{ gutstName }} <br/>
    预定时间： {{ invitationTime }} <br/>
    预定位置：雅间 <br/>
    专属律师：龙成 <br/>
    联系电话：*********** <br/>
    盈科团队，为您服务
  </div>
  <div>
    <MapContainer></MapContainer>
  </div>
  
</template>

<script>
import MapContainer from '@/components/MapContainer.vue'
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: "",
            invitationTime: ""
        };
    },
    mounted() {
        this.getInviInfo();
    },
    methods: {
        getInviInfo() {
            var invitationGuestDict = {
                longcheng: "龙成",
                liuliyi: "刘俐伊",
                yuziqing: "余紫清"
            };
            var invitationTimeDict = {
                longcheng: "2020-10-03",
                liuliyi: "2020-10-01",
                yuziqing: "2020-10-02"
            };
            var key = this.$route.params.invitation_name;
            this.gutstName = invitationGuestDict[key];
            this.invitationTime = invitationTimeDict[key];
        }
    },
    components: { MapContainer }
}
</script>

<style scoped>
#message{
    text-align: left;
}
</style>