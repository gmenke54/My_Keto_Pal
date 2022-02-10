<template>
  <div class="cont" v-if="food">
    <div class="header">Nutrition Facts</div>
    <div class="light line"></div>
    <div class="name-line flex">
      <div>{{food.name}}</div>
      <div>({{food.weight.toFixed(0)}}g)</div>
    </div>
    <div class="thick line"></div>
    <div class="flex">
      <div class="carb-title">Carbohydrates</div>
      <div class="carb">{{food.carbs.toFixed(0)}}</div>
    </div>
    <div class="med line"></div>
    <div class="flex">
      <div></div>
      <div class="dv small">% Daily Value*</div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div><span class="dv">Total Fat</span> {{food.fat.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div>Saturated Fat {{food.saturated.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div>Trans Fat {{food.trans.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div><span class="dv">Cholesterol</span> {{food.chol.toFixed(0)}}mg</div>
      <div class="dv">{{food.chol_dv.toFixed(0)}}%</div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div><span class="dv">Sodium</span> {{food.sodium.toFixed(0)}}mg</div>
      <div class="dv">{{food.sodium_dv.toFixed(0)}}%</div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div><span class="dv">Total Calories</span> {{food.calories.toFixed(0)}}kcal</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div>Dietary Fiber {{food.fiber.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div>Total Sugars {{food.sugar.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="light line"></div>
    <div class="flex">
      <div><span class="dv">Protein</span> {{food.protein.toFixed(0)}}g</div>
      <div></div>
    </div>
    <div class="thick line"></div>
    <div class="footer">*The % Daily Value (DV) tells you how much a nutrient contributes to the recommended daily diet. 2,000 calories a day is used for general nutrition advice.</div>
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
    width: 175px;
    align-items: center;
  }
  .cont{
    display: flex;
    flex-direction: column;
    width: 175px;
    font-size: 12px;
    border: 4px solid black;
    padding: 2px 5px 5px 5px;
    background-color: white
  }
  .header{
    width: 175px;
    font-size: 24.65px;
    font-weight: 900;
    text-align: center;
    margin-bottom: -5px
  }
  .footer{
    font-size: 8.6px
  }
  .carb{
    font-weight: 900;
    font-size: 28px;
  }
  .carb-title{
    font-weight: 900;
    font-size: 17px
  }
  .line{
    width: 175px;
    height: 8.5px;
    background-color: black
  }
  .light{
    height: 1px;
  }
  .med{
    height: 6px;
    margin-top: -8px
  }
  .dv{
    font-weight: 900
  }
  .small{
    font-size: 10px
  }
  .name-line{
    font-weight: 600;
    font-size: 12.5px
  }
</style>