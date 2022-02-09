<template>
  <div class="food-card">
    <div class="food-line" v-if="dispUpdate===false" @dblclick="updateFood" >{{food.name}} | Carbs: {{food.carbs.toFixed(1)}}</div>
    <div v-if="dispUpdate===false" @click="delFood" class="btn">-</div>
    <div v-if="dispUpdate">
      <form @submit.prevent="postFood">
        <input type="text" name="newFood" v-model="newFood" :placeholder="food.name">
        <button type="submit">Update</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FoodCard',
  props: {
    food: Object
  },
  data: ()=> ({
    dispUpdate: false,
    newFood: null
  }),
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
    },
    updateFood(){
      this.dispUpdate=true
    },
    async postFood(){
      let res = await axios.get(`https://api.edamam.com/api/nutrition-data?app_id=${process.env.VUE_APP_ID}&app_key=${process.env.VUE_APP_KEY}&nutrition-type=cooking&ingr=${this.newFood}`)
      let nutrients = res.data
      console.log('posting food')
      console.log(this.$store.state.day.id)
      let transf = 0.0
      try {
        transf = nutrients.totalNutrients.FATRN.quantity
      } catch {
        transf = 0.0
      }
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
		    trans: transf,
		    chol: nutrients.totalNutrients.CHOLE.quantity,
		    sodium: nutrients.totalNutrients.NA.quantity,
		    added_sugar: 0.0,
		    chol_dv: nutrients.totalNutrients.CHOLE.quantity,
		    sodium_dv: nutrients.totalNutrients.NA.quantity
      }
      let response = await axios.post(`http://127.0.0.1:8000/foods/`, foodObj)
      this.delFood()
      let resp = await axios.get('http://127.0.0.1:8000/days')
      console.log(resp.data)
      let id = this.$store.state.user.id
      const result = resp.data.filter(day => day.user_id===id && day.date===this.$store.state.day.date)
      console.log(result[0])
      this.$store.commit('setDay', result[0])
      this.newFood = null
      this.dispUpdate=false
    }
  }
}
</script>

<style scoped>
.food-card{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  /* margin: 10px 0; */
  padding: 4px 5px;
  border-radius: 3px;
}
.food-card:hover{
  background-color:rgb(240, 240, 240)
}

.btn{
  cursor: pointer;
  background-color: #0166EE;
  color: white;
  border-radius: 3px;
  padding: 0 10px;
  font-weight: 900
}
.btn:hover{
  background-color: #0048e2;
}
.food-line{
  cursor: pointer;
}
</style>