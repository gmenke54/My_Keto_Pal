<template>
  <div class="home">
    <div v-if="this.$store.state.isAuthenticated">
      Welcome to the home page
    </div>
    <div v-else>
      Please Login
    </div>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
}
</script>
