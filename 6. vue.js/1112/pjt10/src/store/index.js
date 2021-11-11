import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieCards: [],
    movieWanted: []
  },
  mutations: {
    LOAD_MOVIE_CARDS: function (state, results) {
      state.movieCards = results
    },
    CREATE_MOVIE: function (state, movieItem) {
      state.movieWanted.push(movieItem)
    }
  },
  actions: {
    LoadMovieCards: function ({commit}) {
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: {
          api_key: '2176e678f7fd85bcdcc3c92afb413dbe',
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res)
          commit('LOAD_MOVIE_CARDS', res.data.results)
        })
    },
    createMovie: function ({commit}, movieItem) {
      commit('CREATE_MOVIE', movieItem) 
    }
  },
  modules: {
  }
})
