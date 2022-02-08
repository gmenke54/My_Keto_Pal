<template>
  <div class="day-card">
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: 'DayCard',
  props: {
    date: String
  },
  mounted() {
    this.getCurrentDay()
  },
  updated(){
    this.getCurrentDay()
  },
  methods: {
    async getCurrentDay(){
      let id = this.$store.state.user.id
      console.log(this.date, id)
      let res = await axios.get('http://127.0.0.1:8000/days')
      console.log(res.data)
      const result = res.data.filter(day => day.user_id===id && day.date===this.date)
      console.log(result[0])
      if (result.length>0){
        this.$store.commit('setDay', result[0])
      } else {
        this.$store.commit('setDay', null)
      }
    }
  }
}
</script>