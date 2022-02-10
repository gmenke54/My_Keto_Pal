<template>
  <div class="addprofile">
    <div class="cont">
      <div class="slide" v-if="slide===1">
        <div>Welcome! Just a few quick questions so we can customize MyKetoPal for you.</div>
        <div @click="slide++" class="btn">continue</div>
      </div>
      <div class="slide" v-if="slide===2">
        <div class="flex-col">
          <div>What is your baseline activity level?</div>
          <div class="small">Not including workouts</div>
        </div>
        <div @click="setActiv('low')" class="btn hollow grey" :class="low">
          <div class="bold">Not Very Active</div>
          <div class="small">Spend most of the day sitting (e.g., bankteller, desk job)</div>
        </div>
        <div @click="setActiv('med')" class="btn hollow grey" :class="med">
          <div class="bold">Active</div>
          <div class="small">Spend a good part of the day doing some physical activity (e.g., food server, teacher)</div>
        </div>
        <div @click="setActiv('high')" class="btn hollow grey" :class="high">
          <div class="bold">Very Active</div>
          <div class="small">Spend a good part of the day doing heavy physical activity (e.g., bike messenger, carpenter)</div>
        </div>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===3">
        <div>What is your goal weight?</div>
        <input type="number" name="goal_weight" placeholder="Goal weight Ibs" v-model="goal_weight"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===4">
        <div>What is your current weight?</div>
        <input type="number" name="cur_weight" placeholder="Current weight Ibs" v-model="cur_weight"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===5">
        <div>How many weeks to you plan to maintain a ketogenic diet for?</div>
        <input type="number" name="keto_weeks" placeholder="Weeks until goal weight" v-model="keto_weeks"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===6">
        <div>Please provide some more information:</div>
        <input type="text" name="name" placeholder="Full Name" v-model="name"/>
        <input type="number" name="age" placeholder="Age (yrs)" v-model="age">
        <input type="text" name="img" placeholder="Profile Picture URL" v-model="img"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="submit">submit</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddProfile',
  data: () => ({
    slide: 1,
    cur_weight: null,
    goal_weight: null,
    keto_weeks: null,
    img: null,
    name: null,
    age: null,
    activ: 'med',
    low: 'grey',
    med: 'grey',
    high: 'grey'
  }),
  methods: {
    async submit(){
      let loss = ((this.goal_weight - this.cur_weight) / this.keto_weeks) * -1;
      let i_carbs = loss * (40 / loss ** 2) * (1 + this.age / 60);
      switch (this.activ) {
        case 'high':
          i_carbs *= 1.2;
        case 'med':
          i_carbs *= 1;
        case 'low':
          i_carbs *= 0.8;
      }
      console.log(i_carbs)
      let fat = i_carbs * 5;
      let sugar = i_carbs / 3;
      let carb = i_carbs;
      const newProf = {
        user_id: this.$store.state.user.id,
        user: this.$store.state.user.id,
        cur_weight: this.cur_weight,
        goal_weight: this.goal_weight,
        img: this.img,
        keto_weeks: this.keto_weeks,
        name: this.name,
        age: this.age,
        activ: this.activ,
        daily_carb: carb,
        daily_fat: fat,
        daily_sugar: sugar
      }
      const res = await axios.post('http://127.0.0.1:8000/profiles/', newProf)
      this.$router.go()
    },
    setActiv(level){
      this.activ = level
      if (level === 'low'){
        this.low='blue'
        this.med='grey'
        this.high='grey'
      } else if (level === 'med'){
        this.low='grey'
        this.med='blue'
        this.high='grey'
      } else {
        this.low='grey'
        this.med='grey'
        this.high='blue'
      }
    }
  }
}
</script>


<style scoped>

.btnBar{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 372px
}

.btn{
  cursor: pointer;
  background-color: #3181CE;
  color: white;
  font-size: 20px;
  font-weight: 500;
  padding: 10px 60px;
  border-radius: 5px;
}

.btn:hover{
  background-color: #358bdb;
}

input{
  width: 200px;
}

.slide{
  font-size: 19px;
  font-weight: 600;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  height: 600px;
  align-items: center;
}

.cont{
  width: 372px;
  height: 400px;
  padding: 48px 64px;
  background-color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  box-shadow: 0px 0px 12px -5px rgba(0,0,0,0.7)
}

.hollow{
  border: 2px solid #3181CE;
  background-color: white;
  color: #3181CE
}

.hollow:hover{
  background-color: #F0F2F4;
  border: 2px solid #338ee2;;
  color: #338ee2;;
}

.addprofile{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh
}
.small{
  font-size: 12px;
  color: rgb(156, 156, 156)
}
.bold{
  color: black
}
.grey{
  border-color: rgb(182, 182, 182)
}
.grey:hover{
  background-color: white;
}
.blue{
  border-color: #3181CE
}
.grey:hover{
  border-color: rgb(141, 141, 141)
}
.blue:hover{
  border-color: #3181CE
}

</style>
