<template>
  <div class="profile">
    <div v-if="this.$store.state.isAuthenticated">
      <div v-if="this.$store.state.profile">
        <div class="pic-cont">
          <div class="activity" :class="color">{{this.activity}}</div>
          <img @mouseover="dispEdit=true" @mouseleave="dispEdit=false" :src="this.$store.state.profile.img" class="pic" alt="profile picture">
          <div v-if="dispEdit" class="edit">click to edit</div>
          
        </div>
        <div class="name">{{ this.$store.state.profile.name}}, {{this.$store.state.profile.age}}</div>
        <div>{{this.$store.state.user.email}}</div>
        <div @dblclick="togDisplay" class="click">
          <div v-if="displayForm">
            <form @submit.prevent="updateWeight">
              <input type="number" name="newWeight" :placeholder="this.$store.state.profile.cur_weight" v-model="newWeight"/>
              <button type="submit">Update</button>
            </form>
          </div>
          <div v-else>Current Weight: {{this.$store.state.profile.cur_weight}}</div>
          </div>
        <div>Goal Weight: {{this.$store.state.profile.goal_weight}}</div>
        <div class="btn" @click="delProfile">Clear Profile</div>
      </div>
      <div v-else>
        <AddProfile/>
      </div>
    </div>
    <div v-else>
      Please Login!
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import AddProfile from '@/components/AddProfile.vue'

export default {
  name: 'Profile',
  data: ()=>({
    newWeight: null,
    displayForm: false,
    dispEdit: false,
    color: 'blue'
  }),
  components: {
    AddProfile
  },
  computed: {
    activity(){
      if (this.$store.state.profile.activ === 'low'){
        this.color = "red"
        return "Not Very Active"
      } else if (this.$store.state.profile.activ === 'med'){
        this.color = "blue"
        return "Moderately Active"
      } else {
        this.color = "gold"
        return "Very Active"
      }
    }
  },
  methods: {
    togDisplay(){
      console.log('displaying')
      this.displayForm=true
    },
    async updateWeight(){
      const id = this.$store.state.user.id
      const update = {
        user: id,
	      user_id: id,
	      cur_weight: this.newWeight
      }
      const res = await axios.put(`http://127.0.0.1:8000/profiles/${id}`, update)
      console.log(res)
      this.newWeight = null
      this.$store.dispatch('setUserId')
      this.displayForm=false
    },
    async delProfile(){
      const id = this.$store.state.user.id
      await axios.delete(`http://127.0.0.1:8000/profiles/${id}`)
      this.$router.go()
    }
  }
}
</script>

<style scoped>
.profile{
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pic-cont{
  position: relative;
  text-align: center;
  color: white;
}

.edit{
  position: absolute;
  top: 90%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.pic{
  height: 200px;
  border: 2px solid #3181CE;
  border-radius: 300px
}
.click{
  cursor: pointer;
}
.btn{
  cursor: pointer;
  background-color: #3181CE;
  color: white;
  font-size: 20px;
  font-weight: 500;
  padding: 10px 60px;
  border-radius: 5px;
  width: 30vw
}
.btn:hover{
  background-color: #338ee2;
}
.name{
  font-weight: 600
}
.activity{
  border-radius: 5px;
  color: white;
  width: 90px;
  padding: 5px 0;
  position: absolute;
  /* left: 60%;
  top: 70% */
}
.red{
  background-color: rgb(165, 70, 70);
}
.blue{
  background-color: #3181CE;
}
.gold{
  background-color: rgb(224, 198, 46)
}
</style>
