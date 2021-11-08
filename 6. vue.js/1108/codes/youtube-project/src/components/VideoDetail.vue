<template>
  <div v-if="video">
    <iframe :src="videoURI" frameborder="0"></iframe>
    <!-- 밑을 통해 video 정보 출력 -->
    <!-- {{ video }} -->
  </div>
</template>

<script>
export default {
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
    
    
  },
  computed: {
    videoURI: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>
