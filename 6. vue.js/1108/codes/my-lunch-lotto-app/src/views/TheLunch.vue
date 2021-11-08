<template>
  <div>
      <h1>점심 메뉴</h1>
      <button @click="getLunch">Pick Lunch</button>
      <p>{{ selected }}</p>
      <h2>로또를 뽑아보자</h2>
      <button @click="moveToLotto">Pick Lotto</button>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
    name: 'TheLunch',
    data: function () {
        return {
            lunchList: ['돈까스', '짜장면', '햄버거', '치킨', '마라탕', '라면', '김밥'],
            selected: '',
        }
    },
    methods: {
        getLunch: function () {
            const numbers = _.range(0, 7)
            const idx = _.sampleSize(numbers, 1)
            console.log(idx)
            this.selected = this.lunchList[idx]
        },
        moveToLotto: function () {
            this.$router.push({ name: 'TheLotto', params: { lottoNum: 6 } })
        }
    }
}
</script>

<style>

</style>