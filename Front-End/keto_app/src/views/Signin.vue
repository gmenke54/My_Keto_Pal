<template>
  <div>
    <div>Login to an Existing Account</div>
    <form @submit.prevent="submitForm">
      <input type="email" name="username" placeholder="enter email" v-model="username" />
      <input type="password" name="password" placeholder="enter password" v-model="password"/>
      <button type="submit">Login</button>
    </form>
    
  </div>
</template>

<script>
import axios from 'axios'


export default {

  name: 'Signin',
  data: () => ({
    username: '',
    password: ''
  }),
  methods: {
    submitForm(e){
      const formData = {
        username: this.username,
        password: this.password
      }
      axios
          .post('/api/v1/token/login', formData)
          .then(response => {
            console.log(response)
            const token = response.data.auth_token
            this.$store.commit('setToken', token)
            axios.defaults.headers.common['Authorization'] = "Token " + token
            localStorage.setItem("token", token)
            this.$router.push('/')
            this.$store.dispatch('setUserId')
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>