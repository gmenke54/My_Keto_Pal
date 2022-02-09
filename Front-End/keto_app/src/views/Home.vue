<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated" class="cont">
      <DatePicker v-model="date"/>
      <div>
        <div class="day-head">{{header}}</div>
        <div v-if="this.day && this.$store.state.user.id" >
          <DayCard :date="this.day" />
        </div>
        <div v-if="this.$store.state.day">
          <MainDay />
        </div>
          <AddFood />
      </div>
    </div>
    <div v-else>
      Please Login
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
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
      return this.date.toISOString().slice(0,10)
    },
    header(){
      return this.date.toString().slice(0,15)
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
</style>