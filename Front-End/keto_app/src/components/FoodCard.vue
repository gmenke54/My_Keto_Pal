<template>
  <div class="food-card">
    <div>{{food.name}}</div>
    <div>Carbs: {{food.carbs}}</div>
  </div>
</template>

<script>

export default {
  name: 'FoodCard',
  props: {
    food: Object
  },
  methods: {
  }
}
</script>
