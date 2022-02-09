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

export default {
  name: 'AddFood',
  data: ()=> ({
    dispBtn: true,
    newFood: null
  }),
  methods: {
    async postFood(){
      console.log('posting food')
      // if I get an error, try unsetting then resetting the auth header and the default base url
      nutrients = await axios.get(``)
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