<template>
  <div class="cont" v-if="food">
    <div>Nutrition Facts</div>
    <div class="name-line flex">
      <div>{{food.name}}</div>
      <div>({{food.weight.toFixed(0)}}g)</div>
    </div>
    <div class="thick line"></div>
    <div class="flex">
      <div>Carbohydrates</div>
      <div>{{food.carbs.toFixed(0)}}</div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div></div>
      <div>% Daily Value*</div>
    </div>
    <div class="flex">
      <div>Total Fat {{food.fat.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Saturated Fat {{food.saturated.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Trans Fat {{food.trans.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Cholesterol {{food.chol.toFixed(0)}}mg</div>
      <div>{{food.chol_dv.toFixed(0)}}%</div>
    </div>
    <div class="flex">
      <div>Sodium {{food.sodium.toFixed(0)}}mg</div>
      <div>{{food.sodium_dv.toFixed(0)}}%</div>
    </div>
    <div class="flex">
      <div>Total Calories {{food.calories.toFixed(0)}}kcal</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Dietary Fiber {{food.fiber.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Total Sugars {{food.sugar.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="flex">
      <div>Protein {{food.protein.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="thick line"></div>
    <div>* The % Daily Value (DV) tells you how much a nutrient contributes to the recommended daily diet. 2,000 calories a day is used for general nutrition advice.</div>
  </div>
</template>

<script>
export default {
  name: 'Label',
  components: {
  },
  props: {
    
  },
  computed: {
    food(){
      return this.$store.state.food
    }
  },
  methods: {
  }
}
</script>

<style scoped>
  .flex{
    display: flex;
    justify-content: space-between;
    width: 300px;
  }
  .cont{
    display: flex;
    flex-direction: column;
    width: 300px;
  }
</style>