<template>
    <div id="nav">
      尊敬的{{ gutstName }}，您好<br />
      感谢您的到来<br />
      <img src="../assets/acknowledgement.png">
    </div>
  </template>
  
  <script>
  export default {
      name: "InvitationView",
      data() {
          return {
              gutstName: "a",
              invitationTime: "n"
          };
      },
      mounted() {
          this.getGuestInfo();
      },
      methods: {
          getGuestInfo() {
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
              var key = this.$route.params.acknowledge_name;
              this.gutstName = invitationGuestDict[key];
              this.invitationTime = invitationTimeDict[key];
          }
      }
  }
  </script>
  