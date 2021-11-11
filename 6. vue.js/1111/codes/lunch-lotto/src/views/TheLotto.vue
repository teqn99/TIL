<template>
  <div>
    <h2>로또 번호 추천</h2>
    <button @click="getLuckyNum">로또 번호 추천좀...</button>
    <p>로또 추천 번호 {{ $route.params.lottoNum }}개</p>
    <p>{{ $route.params }}</p>
    <ul>
      <li v-for="(num, idx) in selectedLuckyNum" :key="idx"> {{ num }}</li>
    </ul>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLotto',
  data: function () {
    return {
      selectedLuckyNum: [],      
    }
  },
  methods: {
      getLuckyNum: function () {
        const numbers = _.range(1, 46)
        this.sampleNums = _.sampleSize(numbers, this.$route.params.lottoNum)
        this.selectedLuckyNum = _.sortBy(this.sampleNums)
      }
  }
}
</script>

<style>

</style>