<template>
  <div class="feed-card">
    <div class="text">{{element.text}}</div>
    <img v-if="element.img" :src="element.img" alt="">
    <div v-if="element.link">
      <LinkPreview :link="element.link"/>
    </div>
  </div>
</template>

<script>
import LinkPreview from '../components/LinkPreview.vue'
export default {
  name: 'FeedCard',
  methods: {},
  props: {
    element: Object
  },
  components: {
    LinkPreview,
  }
}
</script>