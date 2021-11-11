<template>
  <div>
    <div class="card mx-auto" style="width: 400px;" v-if="flag">
      <button class="btn btn-success" @click="makeRandom">PICK</button>
      <img :src="movieImg" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ selectedMovieCard.title }}</h5>
      </div>
    </div>
    <div class="card mx-auto" style="width: 400px;" v-else>
      <button class="btn btn-success" @click="makeRandom">PICK</button>
      <div style="width: 400px; height: 600px; justify-content: center;" class="d-flex align-items-center">
        <h3>PICK a MOVIE</h3>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import { mapState } from 'vuex'

export default {
  name: 'Random',
  data: function () {
    return {
      selectedMovieCard: [],
      flag: false,
    }
  },
  methods: {
    makeRandom: function () {
      const randomIndex = _.random(this.movieCards.length - 1)
      this.selectedMovieCard = this.movieCards[randomIndex]
      this.flag = true
    }
  },
  created: function () {
    this.$store.dispatch('LoadMovieCards')
  },
  computed: {
    ...mapState(['movieCards']),
    movieImg: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.selectedMovieCard.poster_path
    }
  }
}
</script>

<style>

</style>