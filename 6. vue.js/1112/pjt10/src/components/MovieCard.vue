<template>
  <div class="col">
    <div class="card" @click="gogo">
      <img :src="movieImg" class="card-img-top">
      <div class="card-body">
        <h5 class="card-title">{{ movieCard.title }}</h5>
        <p class="card-text">{{ movieCard.overview }}</p>
      </div>
      <div class="card-footer">
        <small class="text-muted">개봉일: {{ movieCard.release_date }}</small>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movieCard: Object,
    idx: Number,
  },
  methods: {
    show: function () {
      console.log(this.movieCard)
    },
    gogo: function () {
      console.log(this.idx)
      this.$router.push({ name: "MyMovieDetail", params: { movieId: this.idx } })  // 버튼 클릭 시 TheLotto로 페이지 이동
    }
  },
  computed: {
    movieTitle: function () {
      return this.movieCard.title
    },
    movieImg: function () {
      return 'https://image.tmdb.org/t/p/w500' + this.movieCard.poster_path
    }
  }
}
</script>

<style>

</style>


