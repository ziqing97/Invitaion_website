<template>
    <div>
    <!--<wechat-share domainSuffix='AllInvitation'></wechat-share>-->
    </div>
    <div>
    <div id="video_intro">
        <video id="video" autobuffer controls webkit-playsinline playsinline x5-playsinline>
            <source src='https://www.bilibili.com/video/av776569997?t=4.6' type="video/mp4">
        </video>
        <!--<vue3VideoPlay v-bind="options"/>-->
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
        <img src="../assets/locInChina.jpg" class="picture_intro">
    </div>
    <div>
        <img src="../assets/locInWorld.jpg" class="picture_intro">
    </div>
  </div>
</template>

<script>
import MapContainer from '@/components/MapContainer.vue'
//import WechatShare from  '@/components/WechatShare.vue'
//import "vue3-video-play/dist/style.css"
//import vue3VideoPlay from "vue3-video-play"
// import axios from 'axios'
import { reactive } from "vue";
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: null,
            invitationTime: null,
            guestCount: null,
            mainLawyer: null,
            teamAssistant: null,
            contactNumber: null,
            options:  reactive({
                    width: "100%", //播放器高度
                    color: "#000000", //主题色
                    title: "", //视频名称
                    /*sources: [
                        {
                            type: "video/mp4",
                            src: require("../assets/aa.mp4")
                        }
                    ],*/
                    src: "../static/aa.mp4",
                    muted: false, //静音
                    webFullScreen: false,
                    speedRate: ["0.75", "1.0", "1.25", "1.5", "2.0"], //播放倍速
                    autoPlay: false, //自动播放
                    loop: false, //循环播放
                    mirror: false, //镜像画面
                    currentTime: 1,
                    ligthOff: false, //关灯模式
                    volume: 0.3, //默认音量大小
                    control: true, //是否显示控制
                    controlBtns: [
                        "audioTrack",
                        "quality",
                        "speedRate",
                        "volume",
                        "setting",
                        "pip",
                        "pageFullScreen",
                        "fullScreen",]
            })
        };
    },
    mounted() {
        this.getInviInfo();
    },
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