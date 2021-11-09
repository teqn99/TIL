<template>
  <div>
    <h1>This is VideoList</h1>
    <ul>
      <VideoListItem
       v-for="(video, idx) in videos" :key="idx" :video="video" 
       @select-video="onSelectVideo"/>
    </ul>
  </div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'

export default {
  name: 'VideoList',
  components: {
    VideoListItem,
  },
  props: {
    videos: Array,
  },
  methods: {
    onSelectVideo: function (video) {
      this.$emit('select-video', video)
    }
  },
}
</script>

<style>

</style>