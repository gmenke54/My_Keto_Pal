<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated" class="cont">
      <DatePicker mode="date" v-model="date"/>
      <div>
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

export default {
  name: 'Home',
  components: {
    Calendar,
    DatePicker,
    DayCard,
    MainDay,
    AddFood
  },
  data() {
    return {
      date: new Date(),
    };
  },
  computed: {
    day(){
      // return this.date.toISOString().slice(0,10)
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
  justify-content: space-around;
  align-items: center;
}
.day-head{
  font-weight: 600
}
</style>