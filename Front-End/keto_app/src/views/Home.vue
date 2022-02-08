<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated">
      <DatePicker v-model="date"/>
      <!-- <div @click="postDay">Log Food</div> -->
      <div v-if="this.day && this.$store.state.user.id" >
        <DayCard :date="this.day" />
      </div>
      <div v-if="this.$store.state.day">
        show day
      </div>
      <div v-else>
        log some food
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

export default {
  name: 'Home',
  components: {
    Calendar,
    DatePicker,
    DayCard,
  },
  data() {
    return {
      date: new Date(),
    };
  },
  computed: {
    day(){
      return this.date.toISOString().slice(0,10)
    }
  },
  methods: {
    postDay(){
      console.log(this.day)
    }
  }
}
</script>
