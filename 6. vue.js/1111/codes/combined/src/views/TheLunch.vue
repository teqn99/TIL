<template>
  <div>
    <h2>점심메뉴 추천</h2>
    <button @click="pickOneInLunchMenu">점심 뭐먹지?</button>
    <h2>
      {{ selectedLunchMenu }} 추천!!!
    </h2>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'TheLunch',
  data: function () {
    return {
      lunch: ['국밥', '짜장면', '햄버거', '타코', '서브웨이', '떡볶이'],
      selectedLunchMenu: '',
      lottoNum: 0,
    }
  },
  methods: {
    pickOneInLunchMenu: function () {
      const randomIndex = _.random(this.lunch.length - 1)
      this.selectedLunchMenu = this.lunch[randomIndex]
    }
  }
}
</script>

<style>

</style>