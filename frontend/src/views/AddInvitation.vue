<template>
<div id="inputarea">
    <div id="datetimeinput">
        <span>日期</span>
        <Datepicker v-model="date" :time-picker-component="timePicker" locale="cn" selectText="确定" cancelText="取消"></Datepicker> 
    </div>
    <div id="nameinput">
        <span>姓名：</span><br/>
        <input v-model="customerName"/>
    </div>
    <div id="guestcount">
        <span>人数：</span> <br/>
        <input v-model="customerCount"/>
    </div>
    <div id="mainLawyer">
        <span>主办律师：</span> <br/>
        <input v-model="mainLawyer"/>
    </div>
    <div id="teamAssistant">
        <span>团队助理：</span> <br/>
        <input v-model="teamAssistant"/>
    </div>
    <div id="phoneNumber">
        <span>电话号码：</span> <br/>
        <input v-model="phoneNumber"/><br/>
    </div>
    <div>{{ customerName }}</div>
</div>
<button @click="showSuccess">确定</button>
</template>

<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref, onMounted, defineAsyncComponent, computed } from 'vue';
const TimePicker = defineAsyncComponent(() => import('../components/TimePickerCustom.vue'));
export default {
    name: 'SubmitInvitation',
    components: { Datepicker },
    setup() {
        const date = ref();
        const timePicker = computed(() => TimePicker);
        // For demo purposes assign range from the current date
        onMounted(() => {
            const startDate = new Date();
            const endDate = new Date(new Date().setDate(startDate.getDate() + 7));
            date.value = [startDate, endDate];
        })
        return {
            date,
            timePicker
        }
    },
    data() {
        return {
            customerName: null,
            customerCount: null,
            mainLawyer: null,
            teamAssistant: null,
            phoneNumber: null
        }
    },
    computed:{
        generatedKey(){
            var str = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
            var res = "";
            for(var i = 0; i < 20 ; i ++) {
                var id = Math.ceil(Math.random()*35);
                res += str[id];
            }
            return res;
        }
    },
    methods: {
        sentData(){
            
        },
        showSuccess(){
            this.$router.push({name: 'AddSuccess', params: { invitation_name: 'yuziqing'}}) // here should be a variable
        }
    }
}
</script>

<style scoped>
button{
    font-size:medium;
    align-items: center;
}

#inputarea {
    text-align: left;
    line-height: 1.6em;
    padding: 10px;
    margin:20px;
    font-size: 120%;
}
.pad {
    padding: 10px;
    margin:20px;
    width: 80%;
}
</style>