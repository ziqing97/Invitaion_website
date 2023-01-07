<template>
    <div>
    <wechat-share></wechat-share>
    <div id="video_intro">
        <!--<video id="video" autobuffer controls webkit-playsinline playsinline x5-playsinline>
            <source src='../assets/welcome.mp4' type="video/mp4">
        </video>-->
        <iframe src="//player.bilibili.com/player.html?bvid=BV1AP4y1z7bN&page=1" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
    </div>
    <div id="message">
        尊贵的当事人：您好！<br/>
        诚邀出席 【北京市盈科（深圳）律师事务所-咨询会议】<br/>
        预订贵宾：余紫清 <br/>
        预订时间：2023-01-03 星期二 <br/>
        预订人数：4 <br/>
        主办律师：龙成 <br/>
        团队助理：何律师 <br/>
        联系电话：<span id='number' v-touch="callPhone">13873246454 </span><br/>
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
        <img src="http://www.junnuolc.cn/download/locInChina.jpg" class="picture_intro">
    </div>
    <div>
        <img src="http://www.junnuolc.cn/download/locInWorld.jpg" class="picture_intro">
    </div>
  </div>
</template>

<script>
import MapContainer from '@/components/MapContainer.vue'
import WechatShare from  '@/components/WechatShare.vue'
//import axios from 'axios'
//import { reactive } from "vue";
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: null,
            invitationTime: null,
            guestCount: null,
            mainLawyer: null,
            teamAssistant: null,
            contactNumber: 13873246454,
        };
    },
    /*mounted() {
        //this.getInviInfo();
    },*/
    methods: {
        callPhone () {
            window.location.href = 'tel://' + this.contactNumber;
        },
        
        /* getInviInfo() {
            axios.post('/invitation/get', 'invitation_id=' + this.$route.params.invitation_name).then(
                res => {
                this.gutstName = res.data.guest_name
                this.invitationTime = res.data.invitation_time
                this.guestCount = res.data.guest_count
                this.mainLawyer = res.data.main_lawyer_name
                this.teamAssistant = res.data.assistant_name
                this.contactNumber = res.data.contact_number
                // eslint-disable-next-line
                console.log(res)
                }
            ).catch(res => {
                // eslint-disable-next-line
                console.log(res)
            })
        } */
    },
    components: { MapContainer, WechatShare }
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