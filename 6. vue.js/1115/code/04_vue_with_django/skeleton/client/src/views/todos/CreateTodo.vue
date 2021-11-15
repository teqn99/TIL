<template>
  <div>
    <input 
      type="text" 
      v-model.trim="title" 
      @keyup.enter="createTodo"
    >
    <button @click="createTodo">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateTodo',
  data: function () {
    return {
      title: null,
    }
  },
  methods: {
    // JWT 요청을 보내는 방법 - Authorization: `JWT ${token}}`의 형식으로 보내야 함
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    createTodo: function () {
      const todoItem = {
        title: this.title,
      }

      if (todoItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/todos/',
          data: todoItem,
          headers: this.setToken(),  // Authorization: `JWT ${token}}`
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'TodoList' })
          })
          .catch(err => {
            console.log(err)
          })
        }
    },
  }
}
</script>
