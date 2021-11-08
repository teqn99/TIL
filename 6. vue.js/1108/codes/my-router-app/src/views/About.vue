<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="moveToHome">Home으로 이동</button>
  </div>
</template>

<script>
export default {
  name: 'About',
  methods: {
    moveToHome: function () {
      // this.$router.push('/')  // 아래와 같은 방법
      this.$router.push({ name: 'Home' })
    }
  }
}
</script>

