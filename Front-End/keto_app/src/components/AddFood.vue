<template>
  <div class="add-food">
    <div v-if="dispBtn" @click="dispBtn=false" class="btn">Log Food</div>
    <div v-if="dispBtn===false">
      <form @submit.prevent="postFood">
        <input type="text" name="newFood" v-model="newFood" placeholder="1 cup cheddar cheese">
        <button type="submit">Add</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddFood',
  data: ()=> ({
    dispBtn: true,
    newFood: null
  }),
  methods: {
    async postFood(){
      let res = await axios.get(`https://api.edamam.com/api/nutrition-data?app_id=${process.env.VUE_APP_ID}&app_key=${process.env.VUE_APP_KEY}&nutrition-type=cooking&ingr=${this.newFood}`)
      let nutrients = res.data
      console.log(nutrients)
      console.log(this.$store.state.day.id)
      let foodObj = {
        days: [this.$store.state.day.id],
		    name: this.newFood,
		    weight: nutrients.totalWeight,
		    carbs: nutrients.totalNutrients.CHOCDF.quantity,
		    calories: nutrients.calories,
	    	fat: nutrients.totalNutrients.FAT.quantity,
		    protein: nutrients.totalNutrients.PROCNT.quantity,
		    sugar: nutrients.totalNutrients.SUGAR.quantity,
		    fiber: nutrients.totalNutrients.FIBTG.quantity,
		    saturated: nutrients.totalNutrients.FASAT.quantity,
		    trans: nutrients.totalNutrients.FATRN.quantity,
		    chol: nutrients.totalNutrients.CHOLE.quantity,
		    sodium: nutrients.totalNutrients.NA.quantity,
		    added_sugar: 0.0,
		    chol_dv: nutrients.totalNutrients.CHOLE.quantity,
		    sodium_dv: nutrients.totalNutrients.NA.quantity
      }
      console.log(foodObj)
      this.dispBtn=true
    }
  }
}
</script>

<style scoped>
.btn{
  cursor: pointer;
  background-color: #0166EE;
  color: white;
  font-size: 20px;
  font-weight: 500;
  padding: 10px 60px;
  border-radius: 5px;
}

.btn:hover{
  background-color: #0048e2;
}
</style>