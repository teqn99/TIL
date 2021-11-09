<template>
  <div>
    <input @keypress.enter="onInputKeyword" type="text">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
      onInputKeyword: function (event) {
        // console.log(event.target.value)
        this.$emit('input-search', event.target.value)
        // this.$emit('input-search', event.target.value, 'additional payload')  // 2개 값을 넘기는 방법
      }
  }
}
</script>

<style>

</style>