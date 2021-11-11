<template>
  <div>
    <h1>Video List</h1>
    <ul>
      <VideoListItem
      v-for="(video, idx) in videoList" :key="idx"
      :video="video"
      />
      <!-- :key에서 :은 v-bind의 축약형 == :이 있으면 뒤에 나오는 부분을 문자열이 아니라 변수로 받아들이는 것이라 생각하기 -->
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
  computed: {
      videoList: function () {
          return this.$store.state.searchResult
      }
  }
}
</script>

<style>

</style>