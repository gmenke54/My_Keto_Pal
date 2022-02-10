<template>
  <div class="add-food">
    <div v-if="dispBtn" @click="dispBtn=false" class="btn">Log Food</div>
    <div v-if="dispBtn===false && dispLoading===false">
      <form @submit.prevent="postFood">
        <input type="text" name="newFood" v-model="newFood" :placeholder="placeholder">
        <button type="submit">Add</button>
      </form>
    </div>
    <div v-if="dispLoading" class="lds-ring"><div></div><div></div><div></div><div></div></div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddFood',
  data: ()=> ({
    dispBtn: true,
    newFood: null,
    placeholder: "1 cup cheddar cheese",
    dispLoading: false
  }),
  props: {
    date: String
  },
  methods: {
    async postFood(){
      this.dispLoading = true
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

      try {
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
		    chol_dv: nutrients.totalDaily.CHOLE.quantity,
		    sodium_dv: nutrients.totalDaily.NA.quantity
      }
      let response = await axios.post(`http://127.0.0.1:8000/foods/`, foodObj)
      let resp = await axios.get('http://127.0.0.1:8000/days')
      console.log(resp.data)
      let id = this.$store.state.user.id
      const result = resp.data.filter(day => day.user_id===id && day.date===this.date)
      console.log(result[0])
      this.$store.commit('setDay', result[0])
      this.newFood = null
      this.placeholder = "1 cup cheddar cheese"
      this.dispLoading=false
      this.dispBtn=true
      } catch {
        this.placeholder = "unknown food - try again"
        this.newFood= null
        console.log('caught error')
      }
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

.lds-ring {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ring div {
  box-sizing: border-box;
  display: block;
  position: absolute;
  width: 64px;
  height: 64px;
  margin: 8px;
  border: 8px solid #0166EE;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #0166EE transparent transparent transparent;
}
.lds-ring div:nth-child(1) {
  animation-delay: -0.45s;
}
.lds-ring div:nth-child(2) {
  animation-delay: -0.3s;
}
.lds-ring div:nth-child(3) {
  animation-delay: -0.15s;
}
@keyframes lds-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>