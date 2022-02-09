<template>
  <div class="main-day">
    <div :key="food.id" v-for="food in this.$store.state.day.food_list">
      <FoodCard  :food="food" />
    </div>
    <div>Total Daily Carbs: {{carbs}}</div>
  </div>
</template>

<script>
import FoodCard from '../components/FoodCard.vue'

export default {
  name: 'MainDay',
  components: {
    FoodCard
  },
  data:()=> ({
    carbs: null
  }),
  mounted(){
    this.countCarbs()
  },
  updated(){
    this.countCarbs()
  },
  methods: {
    countCarbs(){
      let arr = this.$store.state.day.food_list
      console.log('running')
      let totalCarbs = arr.reduce(function (accumulator, food) {
        return accumulator + food.carbs;
      }, 0);
      this.carbs = totalCarbs
    }
  }
}
</script>
