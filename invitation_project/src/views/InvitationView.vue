<template>
  <div id="message">
    尊贵的当事人：您好！<br/>
    诚邀出席 【北京市盈科（深圳）律师事务所-咨询会议】<br/>
    预订贵宾：{{ gutstName }} <br/>
    预订时间： {{ invitationTime }} <br/>
    预订人数： {{ guestCount }} <br/>
    主办律师：{{ mainLawyer }} <br/>
    团队助理：{{ teamAssistant }} <br/>
    联系电话：<span id='number' v-touch="callPhone">{{ contactNumber }} </span><br/>
    专业保障：团队深耕商事诉讼领域（分行）品质保障：快速响应，真正每天18小时待命，高效响应委托人需求（分行） 绝对保密：签署完善的委托合同，严守客户秘密 （分行）可视化服务：团队化、流程化的科学管理，完善的文档数据
    祝您往返途中平安，心情舒畅！
  </div>
  <div>
    <MapContainer></MapContainer>
  </div>
  <div id="pic_team">
    <img src="../assets/team.jpg">
  </div>
  <div id="pic_loc_china">
    <img src="../assets/locInChina.jpg">
  </div>
  <div id="pic_loc_world">
    <img src="../assets/locInWorld.jpg">
  </div>
  <div id="video_intro">
    <video width=100% controls>
        <source src="../assets/welcome.mp4" type="video/mp4">
    </video>
  </div>
  
  
</template>

<script>
import MapContainer from '@/components/MapContainer.vue'
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: null,
            invitationTime: null,
            guestCount: null,
            mainLawyer: null,
            teamAssistant: null,
            contactNumber: null
        };
    },
    mounted() {
        this.getInviInfo();
    },
    methods: {
        callPhone () {
            window.location.href = 'tel://' + this.contactNumber;
        },
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
            var contactDict = {
                longcheng: "123456789",
                liuliyi: "+4915201028696",
                yuziqing: "13873246454"
            };
            var key = this.$route.params.invitation_name;
            this.gutstName = invitationGuestDict[key];
            this.invitationTime = invitationTimeDict[key];
            this.contactNumber = contactDict[key]
        }
    },
    components: { MapContainer }
}
</script>

<style scoped>
#message{
    text-align: left;
    width: 100%
}

#number{
    color: rgb(19,125,196);
}

img {
    width: 100%;
}

</style>