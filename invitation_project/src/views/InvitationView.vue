<template>
  <div id="nav">
    {{ gutstName }} 于 {{ invitationTime }} 被邀请参加高级座谈会
  </div>
  <MapContainer></MapContainer>
</template>

<script>
import MapContainer from '@/components/MapContainer.vue'
export default {
    name: "InvitationView",
    data() {
        return {
            gutstName: "a",
            invitationTime: "n"
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
