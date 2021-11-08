<template>
  <div id="app">
    <h1>My first Youtube Project</h1>
    <header>
      <the-search-bar @input-change="onInputChange"></the-search-bar>
    </header>
    <section>
      <video-detail :video="selectedVideo"></video-detail>
      <video-list :videos="videos" @select-video="onSelectVideo"></video-list>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
import TheSearchBar from '@/components/TheSearchBar'  // @는 src와 같은 뜻으로 쓰임
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'


const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyD5tuK-q7chm86Uhm-mTUjfq4qRwxLxGGA'

export default {
  name: 'App',
  components: {
    TheSearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: null,
      videos: [],
      selectedVideo: null,
    }
  },
  methods: {
    onInputChange: function (inputText) {
      // console.log(inputText)
      this.inputValue = inputText

      const params = {
        key: API_KEY,
        part: 'snippet',
        q: this.inputValue,
        type: 'video',
      }

      axios({
        method: 'get',
        url: API_URL,
        params,
      })
        .then(res => {
          console.log(res)
          this.videos = res.data.items
        })
        .catch(err => {
          console.log(err)
        })
    },
    onSelectVideo: function (video) {
      this.selectedVideo = video
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
