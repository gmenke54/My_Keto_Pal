<template>
  <div class="food-card">
    <div >{{food.name}} | Carbs: {{food.carbs.toFixed(1)}}</div>
    <div @click="delFood" class="btn">delete</div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FoodCard',
  props: {
    food: Object
  },
  methods: {
    async delFood(){
      console.log(this.food.id)
      await axios.delete(`http://127.0.0.1:8000/foods/${this.food.id}`)
      let resp = await axios.get('http://127.0.0.1:8000/days')
      console.log(resp.data)
      let id = this.$store.state.user.id
      const result = resp.data.filter(day => day.user_id===id && day.date===this.$store.state.day.date)
      console.log(result[0])
      this.$store.commit('setDay', result[0])
    }
  }
}
</script>

<style scoped>
.food-card{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin: 10px 0
}
.btn{
  cursor: pointer;
  background-color: #0166EE;
  color: white;
  border-radius: 3px;
  padding: 0 4px;
}
.btn:hover{
  background-color: #0048e2;
}
</style>