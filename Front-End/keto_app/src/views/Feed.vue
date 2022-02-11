<template>
  <div class="feed-page">
  <AddFeed />
  <div :key=element.id v-for="element in this.$store.state.feed" >
    <FeedCard :element="element" />
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import FeedCard from '../components/FeedCard.vue'
import AddFeed from '../components/AddFeed.vue'
export default {
  name: 'Feed',
  components: {
    FeedCard,
    AddFeed,
  },
  methods: {
    handleClick(preview) {
      console.log('click', preview.domain, preview.title, preview.description, preview.img)
    }
  }

}
</script>