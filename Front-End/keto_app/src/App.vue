<template>
  <div>
    <div class="nav">
      <router-link v-if="this.$store.state.isAuthenticated" to="/">myketopal</router-link>
      <router-link v-if="this.$store.state.isAuthenticated" to="/profile">Profile</router-link>
      <router-link v-if="this.$store.state.isAuthenticated === false" to="/signup">Sign Up</router-link> 
      <router-link v-if="this.$store.state.isAuthenticated === false" to="/signin">Login</router-link>
      <div v-if="this.$store.state.isAuthenticated" class="a" @click="logout">Logout</div>
    </div>
    <router-view/>
  </div>

</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if ( token ) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ''
    }
    this.$store.dispatch('setUserId')
  },
  methods: {
    logout(){
      const token = this.$store.state.token
      console.log(token)
        axios
          .post('/api/v1/token/logout', token)
          .then(response => {
            this.$store.commit('removeToken')
            localStorage.setItem("token", '')
            axios.defaults.headers.common['Authorization'] = ''
            this.$router.push('/signin')
            this.$store.commit('setUser', {id:null, email:null})
            this.$store.commit('setProfile', null)
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>


<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #F0F2F4;
  height: 100vh;
}

body{
  margin: 0
}

a, .a{
  text-decoration: none;
  color: #2c3e50;
  &.router-link-exact-active {
    color: #0166EE;
  }
  cursor: pointer;
  border-radius: 5px;
  padding: 8px 12px;
  background-color: white;
}

a:hover, .a:hover {
  background-color: rgb(233, 233, 233);
}

.nav {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding: 5px 0 5px 0;
  font-weight: bold;
  background-color: white;
  border-bottom: 0.5px solid #E7E9EB;
  margin-bottom: 10px;
}
</style>
