<template>
<div id="inputarea" class="pad">
    <span>姓名：</span> <br/>
    <span></span>
    <input v-model="customerName"><br/> <br/>
    <span>日期：</span>
    <Datepicker v-model="date"></Datepicker> 
</div>
</template>

<script>
import Datepicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref, onMounted } from 'vue';
export default {
    name: 'SubmitInvitation',
    components: { Datepicker },
    setup() {
        const date = ref();
        // For demo purposes assign range from the current date
        onMounted(() => {
            const startDate = new Date();
            const endDate = new Date(new Date().setDate(startDate.getDate() + 7));
            date.value = [startDate, endDate];
        })
        return {
            date,
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
</style>