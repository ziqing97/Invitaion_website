<template>
<div>
    <h2>新邀请添加</h2>
</div>
<div id="inputarea" class="pad">
    <div id="nameinput">
        <span>姓名：</span> <br/>
        <span></span>
        <input v-model="customerName"><br/>
    </div>
    <div id="datetimeinput">
        <span>日期：</span>
        <Datepicker v-model="date" :time-picker-component="timePicker"></Datepicker> 
    </div>
    </div>
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
    }
}
</script>

<style scoped>
#inputarea {
    text-align: left;
    line-height: 1.4em;
    padding: 10px;
    margin:20px
}
.pad {
    padding: 10px;
    margin:20px;
    width: 80%;
}

#nameinput {
    font-size: 16px;
}
</style>