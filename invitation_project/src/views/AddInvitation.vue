<template>
<div id="inputarea">
    <div id="datetimeinput">
        <span>日期：</span>
        <Datepicker v-model="date" :time-picker-component="timePicker" locale="cn" selectText="确定" cancelText="取消"></Datepicker> 
    </div>
    <div id="nameinput">
        <span>姓名：</span> <br/>
        <span></span>
        <input v-model="customerName"><br/>
    </div>
    <div id="guestcount">
        <span>人数：</span> <br/>
        <span></span>
        <input v-model="customerCount"><br/>
    </div>
    <div id="mainLawyer">
        <span>主办律师：</span> <br/>
        <span></span>
        <input v-model="mainLawyer"><br/>
    </div>
    <div id="teamAssistant">
        <span>团队助理：</span> <br/>
        <span></span>
        <input v-model="teamAssistant"><br/>
    </div>
    <div id="phoneNumber">
        <span>电话号码：</span> <br/>
        <span></span>
        <input v-model="phoneNumber"><br/>
    </div>
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
    methods:{
        showSuccess(){
            this.$router.push({name: 'AddSuccess'})
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