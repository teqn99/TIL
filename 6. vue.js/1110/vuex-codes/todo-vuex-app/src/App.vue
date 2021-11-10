<template>
  <div id="app">
    <h1>Todo List</h1>
    <h2>All Todos: {{ allTodosCount }} </h2>
    <h2>완료된 TODO 개수: {{ completedTodoscount }}</h2>
    <h2>완료되지 않은 TODO 개수: {{ uncompletedTodoscount }}</h2>
    <todo-list></todo-list>
    <todo-form></todo-form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoList from '@/components/TodoList'
import TodoForm from '@/components/TodoForm'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm,
  },
  // computed: {
  //   completedTodoscount: function () {
  //     return this.$store.getters.completedTodoscount
  //   },
  //   uncompletedTodoscount: function () {
  //     return this.$store.getters.uncompletedTodoscount
  //   },
  //   allTodosCount: function () {
  //     return this.$store.getters.allTodosCount
  //   }
  // }
  // 위와 아래는 동일하게 진행되는 코드
  computed: {
    ...mapGetters([
      'completedTodoscount',
      'uncompletedTodoscount',
      'allTodosCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
