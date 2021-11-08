<template>
  <div>
      <h1>로또</h1>
      <button @click="getLottoNum">Get Lucky Numbers</button>
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