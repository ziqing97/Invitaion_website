<template>
    <div>
    <!--<wechat-share title="北京市盈科（深圳）律师事务所会议邀请函" desc="您好，您的会议邀请请查收，期待与您会面" picLoc='http://www.junnuolc.cn/download/logo.jpg'></wechat-share>-->
    <div id="video_intro">
        <!--<video id="video" autoplay="autoplay" autobuffer controls webkit-playsinline playsinline x5-playsinline>
            <source src='../assets/welcome.mp4' type="video/mp4">
        </video>-->
        <iframe src="//player.bilibili.com/player.html?bvid=BV1AP4y1z7bN&page=1" scrolling="no" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
    </div>
    <div id="message">
        尊贵的当事人：您好！<br/>
        诚邀出席 【北京市盈科（深圳）律师事务所-咨询会议】<br/>
        预订贵宾：{{gutstName}} <br/>
        预订时间：{{invitationTime}} {{invitationHour}}:{{invitationMinute}} {{getWeekDay}} <br/>
        预订人数：{{guestCount}} <br/>
        主办律师：{{mainLawyer}} <br/>
        团队助理：{{teamAssistant}} <br/>
        联系电话：<span id='number' v-touch="callPhone"> {{contactNumber}} </span><br/>
        请您携带会议/案件相关全部书面材料。祝您往返途中平安，心情舒畅！
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
// import WechatShare from  '@/components/WechatShare.vue'
import axios from 'axios'
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: null,
            invitationTime: null,
            invitationHour: null,
            invitationMinute: null,
            guestCount: null,
            mainLawyer: null,
            teamAssistant: null,
            contactNumber: null,
        };
    },
    mounted() {
        this.getInviInfo();
    },

    computed:{
        getWeekDay () {
            var weekArray = new Array("星期日","星期一", "星期二", "星期三", "星期四", "星期五", "星期六")
            var week  = weekArray[new Date(this.invitationTime).getDay()]
            return week
        },
    },
    
    methods: {
        callPhone () {
            window.location.href = 'tel://' + this.contactNumber;
        },
        
        getInviInfo() {
            axios.post('/invitation/get', 'invitation_id=' + this.$route.params.invitation_name).then(
                res => {
                this.gutstName = res.data.guest_name
                this.invitationTime = res.data.invitation_time
                this.invitationHour = res.data.invitation_hour
                let minTemp = res.data.invitation_minute
                if (minTemp<10){
                    this.invitationMinute = "0".concat(minTemp.toString())
                }
                else{
                    this.invitationMinute = res.data.invitation_minute
                }

                this.guestCount = res.data.guest_count
                this.mainLawyer = res.data.main_lawyer_name
                this.teamAssistant = res.data.assistant_name
                this.contactNumber = Number(res.data.contact_number)
                // eslint-disable-next-line
                console.log(res)
                }
            ).catch(res => {
                // eslint-disable-next-line
                console.log(res)
            })
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
    text-decoration: underline;
    font-weight: bold;
}

#video_intro{
    background-color: black;
    width: 100%;
    object-fit: fill
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