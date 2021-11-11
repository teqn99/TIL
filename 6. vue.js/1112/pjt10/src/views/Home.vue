<template>
  <div class="home">
    <div class="row row-cols-1 row-cols-md-3 g-4 mx-2">
      <movie-card
        v-for="(movieCard, idx) in movieCards"
        :key="idx"
        :idx="idx"
        :movieCard="movieCard"
      >
      </movie-card>
    </div>
      
  </div>
</template>

<script>
// @ is an alias to /src
import MovieCard from '@/components/MovieCard.vue'
import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    MovieCard,
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards'])
  },

}
</script>


