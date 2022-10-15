<template>
<div id="addmain">
    <div>
    添加成功！
    </div>
    <div>
        <router-link :to="{ name: 'InvitationRoute', params: { invitation_name: getInvitation() }}">邀请链接</router-link>
    </div>
</div>

</template>

<script>
export default{
    name: 'AddSuccess',
    methods:{
        getInvitation(){
            var key = this.$route.params.invitation_name;
            return key;
        }
    },
    mounted() {
        this.getInvitation();
    },
}
</script>

<style scoped>
#addmain{
    text-align: left;
}
</style>
