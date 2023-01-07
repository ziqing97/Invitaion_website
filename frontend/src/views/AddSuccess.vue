<template>
<div id="addmain">
    <div>
    添加成功！
    </div>
    <br/>
    <div id='link'>
        <a @click="toData">邀请链接</a>
    </div>
</div>

</template>

<script>
import { NavigationFailureType, isNavigationFailure } from 'vue-router'
export default{
    name: 'AddSuccess',
    methods:{
        toData(){
            var key = this.$route.params.invitation_name;
            this.$router.push(`/invitation/${key}`).catch(failure => {
                if (isNavigationFailure(failure, NavigationFailureType.redirected)) {
                    failure.to.path // '/admin'
                    failure.from.path // '/
                }
            })
        }
    }
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
