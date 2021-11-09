<template>
  <div v-if="video">
    <iframe :src="videoURL" frameborder="0"></iframe>
    <h2>Title: {{ video.snippet.title | stringUnescape}}</h2>
    <p>Description: {{ video.snippet.description | stringUnescape}}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'VideoDetail',
  props: {
      video: {
        type: [String, Object]  // String이 올 수도 있고, Object가 올 수도 있다. (처음에 아무것도 안고른 경우=빈문자열(String))
      }
  },
  computed: {
      videoURL: function () {
        // console.log(this.video)
        const videoId = this.video.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
  },
  filters: {
    stringUnescape: function (rawText) {
      return _.unescape(rawText)
    }
  }
}
</script>

<style>

</style>