<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/signup">Sign Up</router-link> | 
    <router-link to="/signin">Login</router-link>
    <div @click="logout">Logout</div>
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
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
