<template>
  <div>
      <h1>로또 번호 추첨</h1>
      <h2>{{ $route.params.lottoNum }}개의 번호를 추첨합니다.</h2>
      <button @click="getLottoNum">PICK</button>
      <p>오늘의 로또 번호</p>
      <p>{{ seletedLottoNum }}</p>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLotto',
    data: function () {
        return {
            seletedLottoNum: [],
        }
    },
    methods: {
        getLottoNum: function () {
            const numbers = _.range(1, 46)
            this.seletedLottoNum = _.sampleSize(numbers, this.$route.params.lottoNum)
        }
    }
}
</script>

<style>

</style>