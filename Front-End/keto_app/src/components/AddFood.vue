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
      let nutrients = await axios.get(`https://api.edamam.com/api/nutrition-data?app_id=${process.env.VUE_APP_ID}&app_key=${process.env.VUE_APP_KEY}&nutrition-type=cooking&ingr=${this.newFood}`)
      console.log(nutrients)
      // let foodObj = {
      //   days: [],
		  //   name: "Test",
		  //   weight: 0.0,
		  //   carbs: 1.0,
		  //   calories: 0.0,
	    // 	 fat: 0.0,
		  //   protein: 0.0,
		  //   sugar: 0.0,
		  //   fiber: 0.0,
		  //   saturated: 0.0,
		  //   "trans": 0.0,
		  //   "chol": 0.0,
		  //   "sodium": 0.0,
		  //   "added_sugar": 4.0,
		  //   "chol_dv": 0.0,
		  //   "sodium_dv": 0.0
      // }
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