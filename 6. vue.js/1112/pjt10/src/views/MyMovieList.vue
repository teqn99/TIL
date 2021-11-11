<template>
  <div>
    <div style="background-color:lightblue; padding:5rem;" class="mx-5">
      <h1>My Movie List</h1>
      <input
      v-model.trim="movieTitle"
      @keyup.enter="createMovie"
      type="text"
      >
      <button @click="createMovie">+</button>
    </div>
    <div style="padding:0rem;" class="mx-5">
      <MovieList />
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MyMovieList',
  components: {
    MovieList,
  },
  data: function () {
    return {
        movieTitle: null,
    }
  },
  methods: {
    createMovie: function () {
      const movieItem = {
        title: this.movieTitle,
        isWatched: false,
      }
      if (movieItem.title) {
        this.$store.dispatch('createMovie', movieItem)
      }
      this.movieTitle = null
    }
  }
}
</script>

<style>

</style>