<template>
  <div>
    <div id="video_intro">
        <video id="video" autobuffer controls webkit-playsinline playsinline x5-playsinline>
            <source src="../assets/welcome.mp4#t=0.8" type="video/mp4">
        </video>
    </div>
    <div id="message">
        尊贵的当事人：您好！<br/>
        诚邀出席 【北京市盈科（深圳）律师事务所-咨询会议】<br/>
        预订贵宾：{{ gutstName }} <br/>
        预订时间：{{ invitationTime }} <br/>
        预订人数：{{ guestCount }} <br/>
        主办律师：{{ mainLawyer }} <br/>
        团队助理：{{ teamAssistant }} <br/>
        联系电话：<span id='number' v-touch="callPhone">{{ contactNumber }} </span><br/>
        祝您往返途中平安，心情舒畅！
    </div>
    <br/>
    <Suspense>
        <div>
            <MapContainer></MapContainer>
        </div>
    </Suspense>
    <br/>
    <br/>
    <div>
        <img src="../assets/team.jpg" class="picture_intro">
    </div>
    <div id="intro">
        <img src="../assets/intro.png" class="picture_intro">
    </div>
    <div>
        <img src="../assets/locInChina.jpg" class="picture_intro">
    </div>
    <div>
        <img src="../assets/locInWorld.jpg" class="picture_intro">
    </div>
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
    width: 100%;
}

#number{
    color: rgb(19,125,196);
}

#video_intro{
    background-color: black;
}

#video{
    width: 100%;
}

#locationdescription{
    text-align: left;
}

#intro{
    width: 100%;
    text-align: left;
}

.picture_intro{
    width: 100%
}
</style>