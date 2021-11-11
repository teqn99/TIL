<template>
  <div>
    {{ movieCards[$route.params.movieId] }}
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'MyMovieDetail',
  computed: {
    ...mapState(['movieCards'])
  },

}
</script>

<style>

</style>