<template>
  <div class="addprofile">
    <div class="cont">
      <div class="slide" v-if="slide===1">
        <div>Welcome! Just a few quick questions so we can customize MyKetoPal for you.</div>
        <div @click="slide++" class="btn">continue</div>
      </div>
      <div class="slide" v-if="slide===2">
        <div>What is your goal weight?</div>
        <input type="number" name="goal_weight" placeholder="Goal weight Ibs" v-model="goal_weight"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===3">
        <div>What is your current weight?</div>
        <input type="number" name="cur_weight" placeholder="Current weight Ibs" v-model="cur_weight"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===4">
        <div>How many weeks to you plan to maintain a ketogenic diet for?</div>
        <input type="number" name="keto_weeks" placeholder="Weeks until goal weight" v-model="keto_weeks"/>
        <div class="btnBar">
          <div class="btn hollow" @click="slide--">back</div>
          <div class="btn" @click="slide++">next</div>
        </div>
      </div>
      <div class="slide" v-if="slide===5">
        <div>Please provide some more information:</div>
        <input type="text" name="name" placeholder="Full Name" v-model="name"/>
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
    name: null
  }),
  methods: {
    async submit(){
      const newProf = {
        user_id: this.$store.state.user.id,
        user: this.$store.state.user.id,
        cur_weight: this.cur_weight,
        goal_weight: this.goal_weight,
        img: this.img,
        keto_weeks: this.keto_weeks,
        name: this.name
      }
      const res = await axios.post('http://127.0.0.1:8000/profiles/', newProf)
      this.$router.go()
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
  border: 2px solid #0166EE;
  background-color: white;
  color: #0166EE
}

.hollow:hover{
  background-color: #F0F2F4;
  border: 2px solid #0048e2;
  color: #0048e2;
}

.addprofile{
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh
}

</style>
