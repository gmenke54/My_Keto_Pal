<template>
  <div v-if="this.details" class="link-preview">
    {{details.description}}
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'FeedCard',
  props: {
    link: String
  },
  data: ()=> ({
    details: null
  }),
  mounted(){
    this.getDetails()
  },
  methods: {
    async getDetails(){
      const res = await axios.get(`http://api.linkpreview.net/?key=c98ba09b2e8ead0f3b95ac8ffc7bb966&q=${this.link}`)
      this.details = res.data
    }
  },
  components: {
  }
}
</script>