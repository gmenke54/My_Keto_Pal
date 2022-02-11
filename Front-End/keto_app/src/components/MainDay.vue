<template>
  <div class="main-day">
    <div :key="food.id" v-for="food in this.$store.state.day.food_list">
      <FoodCard  :food="food" />
    </div>
    <div class="total">Total Daily Carbs: {{carbs.toFixed(1)}}</div>
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
    carbs: 0.0
  }),
  mounted(){
    this.countCarbs()
    this.countSugar()
    this.countFat()
  },
  updated(){
    this.countCarbs()
    this.countSugar()
    this.countFat()
  },
  methods: {
    countCarbs(){
      let arr = this.$store.state.day.food_list
      // console.log('running')
      let totalCarbs = arr.reduce(function (accumulator, food) {
        return accumulator + food.carbs;
      }, 0);
      this.carbs = totalCarbs
      this.$store.commit("setCurCarbs", totalCarbs)
    },
    countSugar(){
      let arr = this.$store.state.day.food_list
      let totalSugar = arr.reduce(function (accumulator, food) {
        return accumulator + food.sugar;
      }, 0);
      this.$store.commit("setCurSugar", totalSugar)
    },
    countFat(){
      let arr = this.$store.state.day.food_list
      let totalFat = arr.reduce(function (accumulator, food) {
        return accumulator + food.fat;
      }, 0);
      this.$store.commit("setCurFat", totalFat)
    }
  }
}
</script>

<style scoped>
.total{
  font-weight: 600;
}
</style>