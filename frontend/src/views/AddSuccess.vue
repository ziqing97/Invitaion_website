<template>
<div id="addmain">
    <div>
    添加成功！
    </div>
    <br/>
    <div id='link'>
        <a @click="toData">邀请链接</a>
    </div>
    <br/>
    <br/>
    <QrcodeVue :value="link" :size=256></QrcodeVue>
</div>
</template>

<script>
import { NavigationFailureType, isNavigationFailure } from 'vue-router'
import QrcodeVue from 'qrcode.vue'
export default{
    name: 'AddSuccess',
    components: {QrcodeVue},
    data() {
        return {
            link:'a'
        };
    },
    mounted(){
        this.getLink()
    },
    methods:{
        toData(){
            var key = this.$route.params.invitation_name;
            this.$router.push(`/invitation/${key}`).catch(failure => {
                if (isNavigationFailure(failure, NavigationFailureType.redirected)) {
                    failure.to.path // '/admin'
                    failure.from.path // '/
                }
            })
        },
        getLink(){
            var key = this.$route.params.invitation_name;
            this.link = `http://www.junnuolc.cn/invitation/${key}`
        }
    },
}
</script>

<style scoped>
#addmain{
    text-align: left;
}

#link{
    text-decoration: underline;
    color: blue
}
</style>
