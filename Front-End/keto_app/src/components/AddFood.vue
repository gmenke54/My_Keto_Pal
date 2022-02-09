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
  props: {
    date: String
  },
  methods: {
    async postFood(){
      let res = await axios.get(`https://api.edamam.com/api/nutrition-data?app_id=${process.env.VUE_APP_ID}&app_key=${process.env.VUE_APP_KEY}&nutrition-type=cooking&ingr=${this.newFood}`)
      let nutrients = res.data
      let curDay = this.$store.state.day
      if (curDay === null){
        const res = await axios.post(`http://127.0.0.1:8000/days/`, {
          user_id: this.$store.state.user.id,
          date: this.date,
          food_list: []
        })
        curDay = res.data
      }
      let transf = 0.0
      try {
        transf = nutrients.totalNutrients.FATRN.quantity
      } catch {
        transf = 0.0
      }
      let foodObj = {
        days: [curDay.id],
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
      let resp = await axios.get('http://127.0.0.1:8000/days')
      console.log(resp.data)
      let id = this.$store.state.user.id
      const result = resp.data.filter(day => day.user_id===id && day.date===this.date)
      console.log(result[0])
      this.$store.commit('setDay', result[0])
      this.newFood = null
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