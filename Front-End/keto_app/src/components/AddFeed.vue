<template>
  <div class="cont">
    <div class="add-post">
      <form @submit.prevent="submitPost">
        <input type="text" name="text" placeholder="share some words of encouragement!" v-model="text" />
        <input type="text" name="image" placeholder="share an image url" v-model="image"/>
        <input type="text" name="link" placeholder="share a helpful link" v-model="link"/>
        <button type="submit">Post</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddFeed',
  data:() => ({
    text: null,
    image: null,
    link: null,
  }),
  methods: {
    async submitPost(){
      const newPost = {
        type: "post",
        profile: this.$store.state.profile.user,
        text: this.text,
        img: this.image,
        link: this.link
      }
    this.text = null
    this.image = null
    this.link = null
    await axios.post(`http://127.0.0.1:8000/posts/`, newPost)
    this.$store.dispatch('getFeed')
    }
  }

}
</script>