<template>
  <div class="profile">
    <div v-if="this.$store.state.isAuthenticated">
      <div v-if="this.$store.state.profile">
        <img :src="this.$store.state.profile.img" class="pic" alt="profile picture">
        <div>{{this.$store.state.user.email}}</div>
        <div @dblclick="togDisplay">
          <div v-if="displayForm">
            <form @submit.prevent="updateWeight">
              <input type="number" name="newWeight" :placeholder="this.$store.state.profile.cur_weight" v-model="newWeight"/>
              <button type="submit">Update</button>
            </form>
          </div>
          <div v-else>Current Weight: {{this.$store.state.profile.cur_weight}}</div>
          </div>
        <div>Goal Weight: {{this.$store.state.profile.goal_weight}}</div>
      </div>
      <div v-else>

      </div>
    </div>
    <div v-else>
      Please Login!
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'Profile',
  data: ()=>({
    newWeight: null,
    displayForm: false
  }),
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
    }
  }
  // data: () => ({
  //   profile = this.$store.state.profile
  // }),
  // computed(){
  //   this.
  // }
}
</script>

<style scoped>
.pic{
  height: 200px;
  border: 2px solid rgb(68, 133, 170);
  border-radius: 300px
}
</style>
