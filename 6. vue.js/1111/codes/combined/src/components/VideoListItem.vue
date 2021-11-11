<template>
  <div>
    <li @click="selectVideo(video)">
    <!-- <li @click="selectVideo"> -->
    <img :src="videoImg">
        {{ videoTitle | stringUnescape}}
    </li> 
  </div>
</template>

<script>
import _ from 'lodash'
import { mapActions } from 'vuex'

export default {
  name: 'VideoListItem',
  props: {
    video: Object,
  },
  methods: {
    ...mapActions([
      'selectVideo',
    ])
    // selectVideo: function () {
    // //   console.log('비디오가 선택됨')
    //   this.$store.dispatch('selectVideo', this.video)
    // }
  },
  computed: {
    videoTitle: function () {
      return this.video.snippet.title
    },
    videoImg: function () {
      return this.video.snippet.thumbnails.default.url
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