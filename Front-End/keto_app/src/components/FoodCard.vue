<template>
<div>
    <div v-if="showLabel">
      <Label class="label" />
    </div>
    <div class="food-card" @mouseover="setLabel" @mouseleave="hideLabel">
      <div class="food-line" v-if="dispUpdate===false" @dblclick="updateFood" >{{food.name}} | Carbs: {{food.carbs.toFixed(1)}}</div>
      <div v-if="dispUpdate===false" @click="delFood" class="btn">-</div>
      <div v-if="dispLoading" class="lds-ring"><div></div><div></div><div></div><div></div></div>
      <div v-if="dispUpdate && dispLoading===false">
        <form @submit.prevent="postFood">
          <input type="text" name="newFood" v-model="newFood" :placeholder="placeholder">
          <button type="submit">Update</button>
        </form>
      </div>
      <button v-if="dispCancel" @click="cancel">Cancel</button>
  </div>
</div>

</template>

<script>
import axios from 'axios'
import Label from '../components/Label.vue'
export default {
  name: 'FoodCard',
  components: {
    Label
  },
  props: {
    food: Object
  },
  data: ()=> ({
    dispUpdate: false,
    newFood: null,
    showLabel: false,
    dispLoading: false,
    error: false,
    dispCancel: false
  }),
  computed:{
    placeholder(){
      if (this.error===true){
        return "unknown food - try again"
      } else {
        return this.food.name
      }
    }
  },
  methods: {
    cancel(){
      this.dispCancel = false
      this.dispUpdate = false
    },
    setLabel(){
      this.showLabel = true
      this.$store.commit("setFood", this.food)
    },
    hideLabel(){
      this.showLabel = false
    },
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
      this.error=false
      this.dispLoading = true
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
      try {
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
		    chol_dv: nutrients.totalDaily.CHOLE.quantity,
		    sodium_dv: nutrients.totalDaily.NA.quantity
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
      this.dispLoading=false
      this.dispUpdate=false
      } catch {
        this.dispCancel = true
        this.error = true
        this.dispLoading=false
        this.newFood= null
        console.log('caught error')
      }

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
  cursor: pointer;
}
.food-card:hover{
  background-color:rgb(240, 240, 240)
}

.btn{
  cursor: pointer;
  background-color: #3181CE;
  color: white;
  border-radius: 30px;
  padding: 0 10px;
  font-weight: 900
}
.btn:hover{
  background-color: #338ee2;;
}
.label{
  /* works but sucks: */
  position: fixed;
  right: 29vw;
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
  border: 8px solid #3181CE;
  border-radius: 50%;
  animation: lds-ring 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  border-color: #3181CE transparent transparent transparent;
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