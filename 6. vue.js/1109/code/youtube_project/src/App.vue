<template>
  <div id="app">
    <h1>Youtube project</h1>
    <SearchBar @input-search="onInputSearch" />
    <VideoDetail :video="selectedVideo" />
    <VideoList :videos="videos" @select-video="onVideoSelect"/>
  </div>
</template>

<script>
import axios from 'axios'
import SearchBar from '@/components/SearchBar'
import VideoList from '@/components/VideoList'
import VideoDetail from '@/components/VideoDetail'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY  // .env.local에서 이름 설정 시, VUE_APP_의 부분은 필수이다.
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  components: {
    SearchBar,
    VideoList,
    VideoDetail,
  },
  data: function () {
    return {
      inputValue: '',
      videos: [],
      selectedVideo: '',
    }
  },
  methods: {
    onInputSearch: function (inputText) {
      // console.log('데이터가 searchBar로 부터 올라옴')
      // console.log(inputText)
      this.inputValue = inputText
      // console.log(this.inputValue)

      const params = {
        key: API_KEY, 
        part: 'snippet',
        type: 'video',
        q: this.inputValue,
      }
      axios.get(API_URL, {
        params,
      })
        .then((res) => {
          // console.log(res.data.items)
          this.videos = res.data.items
          // console.log(this.videos)
          if (!this.selectedVideo) {  // selectedVideo가 비어있는 경우
            this.selectedVideo = this.videos[0]
          }
        })
        .catch((err) => {
          console.log(err)
        })
    },
    // payload 데이터를 2개 보내는 방법
    // onInputSearch: function (inputText, payload) {
    //   console.log('데이터가 searchBar로 부터 올라옴')
    //   console.log(inputText)
    //   console.log(payload)
    // },
    onVideoSelect: function (video) {
      this.selectedVideo = video
    },

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
