<template>
  <div class="profile">
    <div v-if="this.$store.state.isAuthenticated">
      <div v-if="this.$store.state.profile">
        <img :src="this.$store.state.profile.img" class="pic" alt="profile picture">
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
    displayForm: false
  }),
  components: {
    AddProfile
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
.pic{
  height: 200px;
  border: 2px solid rgb(68, 133, 170);
  border-radius: 300px
}
.click{
  cursor: pointer;
}
.btn{
  cursor: pointer;
  background-color: #0166EE;
  color: white;
  font-size: 20px;
  font-weight: 500;
  padding: 10px 60px;
  border-radius: 5px;
  width: 30vw
}

.btn:hover{
  background-color: #0048e2;
}

</style>
