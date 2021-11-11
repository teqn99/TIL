<template>
  <div>
    <table class="table table-striped d-flex">
        <tbody>
        <MovieListItem
        v-for="(movie, idx) in movieWanted"
        :key="idx"
        :movie="movie"
        />
        </tbody>
    </table>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem'
import { mapState } from 'vuex'

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    ...mapState(['movieWanted']),

  },
}
</script>

<style>

</style>