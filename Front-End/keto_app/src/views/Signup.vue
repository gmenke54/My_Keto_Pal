<template>
  <div>
    <div>Create an Account</div>
    <form @submit.prevent="handleSubmit">
      <input type="email" name="username" placeholder="enter email" v-model="username" />
      <input type="password" name="password" placeholder="enter password" v-model="password"/>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Signup',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleSubmit(e){
      console.log('submitted')
      const formData = {
        email: this.username,
        username: this.username,
        password: this.password
      }
      console.log(formData)
      axios
          .post('/api/v1/users/', formData)
          .then(response => {
            this.$router.push('/signin')
            console.log(response)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>