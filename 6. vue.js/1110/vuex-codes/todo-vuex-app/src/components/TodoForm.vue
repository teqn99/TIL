<template>
  <div>
    <input
     v-model.trim="todoTitle"
     @keyup.enter="createTodo"
     type="text"
     >
     <button @click="createTodo">+</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
        todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
      title: this.todoTitle,
      isCompleted: false,
      date: new Date().getTime(),
      }
      // console.log('Todo Create!!')
      // this.$store.commit('CREATE_TODO', todoItem) // mutations 호출 - commit('호출 mutation', payload)
    
      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem)  // actions 호출 - state를 변경하는 것 외에 다른 모든 동작을 수행
      }
      this.todoTitle = null
    }
  }
}
</script>

<style>

</style>