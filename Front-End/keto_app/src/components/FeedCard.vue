<template>
  <div class="feed-card">
    <div class="text">{{element.text}}</div>
    <img v-if="element.img" :src="element.img" alt="">
    <!-- <div ><link-prevue url="https://vuejs.org/"></link-prevue></div> -->
  </div>
</template>

<script>
export default {
  name: 'FeedCard',
  methods: {},
  props: {
    element: Object
  },
  components: {
  }
}
</script>