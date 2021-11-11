import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

Vue.use(Vuex)

export default new Vuex.Store({
  // 변수
  state: {
    searchResult: [],
    selectedVideo: null,
  },
  // ORM 동기
  mutations: {
    ADD_SEARCH_RESULT: function (state, items) {
      state.searchResult = items
    },
    SELECT_VIDEO: function (state, video) {
      state.selectedVideo = video
    },
  },
  // 비동기
  actions: {
    onSearch: function ({ commit }, query) {
      axios.get(API_URL, {
        params: {
          part: 'snippet',
          q: query,
          key: API_KEY,
          type: 'video',
        }
      })
      .then(res => {
        commit('ADD_SEARCH_RESULT', res.data.items)
        // console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    },

    selectVideo: function ({ commit }, video) {
      commit('SELECT_VIDEO', video)
    }
  },
  // computed와 비슷한 getters(비디오 상세 설명, 비디오 url 등 미리 만들어둬서 중앙 저장소에서 계산을 끝내놓은 것)
  // 가져다 쓰기만 하면 됨.
  getters: {
    // 선택된 비디오가 있는 지 확인하기
    isSelected: function (state) {
      return state.selectedVideo !== null
    },

    // Video url 만들기
    videoUrl: function (state) {
      if (state.selectedVideo) {
        const videoId = state.selectedVideo.id.videoId
        return `https://www.youtube.com/embed/${videoId}`
      }
      return ''
    },

    // 선택된 비디오 제목 리턴
    videoTitle: function (state) {
      if (state.selectedVideo) {
        const title = state.selectedVideo.snippet.title
        return _.unescape(title)  // unescape를 통해 글자 깨지기 방지
      }
      return ''
    },

    videoDesc: function (state) {
      if (state.selectedVideo) {
        const desc = state.selectedVideo.snippet.description
        return _.unescape(desc)
      }
      return ''
    },
  },
  modules: {
  }
})
