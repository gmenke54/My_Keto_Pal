<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated" class="cont">
      <div class="flex-row">
        <DatePicker class="cal" mode="date" v-model="date"/>
        <div class="day-card">
          <div class="day-head">{{header}}</div>
          <div v-if="this.day && this.$store.state.user.id" >
            <DayCard :date="this.day" />
          </div>
          <div v-if="this.$store.state.day">
            <MainDay />
          </div>
            <AddFood :date="this.day"/>
        </div>
      </div>
      <div class="flex-row dough">
        <div class="nut">
          <DoughnutChart class="nut" :chartData="testData" />
        </div>
        <div class="nut">
          <DoughnutChart :chartData="testData" />
        </div>
        <div class="nut">
          <DoughnutChart :chartData="testData" />
        </div>
      </div>
    </div>
    <div v-else>
      Please Login
    </div>
  </div>
</template>

<script>
import { Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/dist/style.css';
import DayCard from '../components/DayCard.vue'
import MainDay from '../components/MainDay.vue'
import AddFood from '../components/AddFood.vue'

import { DoughnutChart } from 'vue-chart-3';

export default {
  name: 'Home',
  components: {
    Calendar,
    DatePicker,
    DayCard,
    MainDay,
    AddFood,
    DoughnutChart
  },
  data() {
    return {
      date: new Date(),
    }
  },
  computed: {
    testData(){
      let color = '#3181CE'
      let rem_carbs = this.$store.state.profile.daily_carb-this.$store.state.curCarbs
      if (rem_carbs<= 0){
        rem_carbs = 0
        color = 'rgb(165, 70, 70)';
      }
      return {
        labels: ['Carbs', 'Remaining Carbs'],
        datasets: [
          {
            data: [this.$store.state.curCarbs, (rem_carbs)],
            backgroundColor: [color, 'white'],
          },
        ],
      }
    },
    day(){
      let date =  this.date.toLocaleString('en-US').slice(0,9)
      console.log(date)
      let newDate = date.replace(',', '')
      let splitArr = newDate.split("/")
      let month = ''
      let day = ''
      if (splitArr[0].length === 1){
        month = `0${splitArr[0]}`
      } else{
        month = `${splitArr[0]}`
      }
      if (splitArr[1].length === 1){
        day = `0${splitArr[1]}`
      } else {
        day = `${splitArr[1]}`
      }
      let finalDate = `${splitArr[2]}-${month}-${day}`
      console.log(finalDate)
      return finalDate
    },
    header(){
      let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
      return this.date.toLocaleString('en-US', options)
    }
  },
  methods: {
    postDay(){
      console.log(this.day)
    }
  }
}
</script>

<style scoped>
.cont{
  display: flex;
  flex-direction: column;
}
.flex-row {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex: wrap;
}
.dough{
  display: flex;
  margin-top: 20px;
  align-items: center;
}
.day-head{
  font-weight: 600
}
.day-card{
  padding: 10px;
  background-color: white;
  border-radius: 8px;
  border: 1px solid rgb(214, 214, 214);
  box-shadow: 0px 0px 12px -5px rgba(0,0,0,0.7)
}
.cal{
  box-shadow: 0px 0px 12px -5px rgba(0,0,0,0.7)
}
</style>