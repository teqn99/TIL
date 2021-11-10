import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [
      {
        title: '할 일1',
        isCompleted: false,
        date: new Date().getTime(),
      },
      {
        title: '할 일2',
        isCompleted: false,
        date: new Date().getTime(),
      },
    ]
  },
  mutations: {
    CREATE_TODO: function (state, todoItem) {
      // console.log(state)
      // console.log(todoItem)
      state.todos.push(todoItem)
    },
    DELETE_TODO: function (state, todoItem) {
      // todoItem이 첫 번째로 만나는 요소의 index를 가져옴
      const index = state.todos.indexOf(todoItem)
      // 해당 index 1개만 삭제하고 나머지 요소를 토대로 새로운 배열 생성
      state.todos.splice(index, 1)
    },
    UPDATE_TODO_STATUS: function (state, todoItem) {
      // 3. 배열의 각 요소에 함수가 적용될 새로운 배열을 state의 todos에 할당
      state.todos = state.todos.map(todo => {
        // 1. 넘어온 todoItem과 현재 있는 status의 todos의 요소가 일치하면
        if (todo === todoItem) { 
          // completed의 상대를 변경한 새로운 object return
          return {
            ...todo,  // JS spread syntax
            isCompleted: !todo.isCompleted
          }
        } else {
          // 2. 일치하지 않으면 기존 배열 return
          return todo
        }
      })
    }
  },
  actions: {
    // createTodo: function (context, todoItem) {
    // createTodo: function ({ commit, state }, todoItem) {
    createTodo: function ({ commit }, todoItem) {  // 구조 분해 할당
      // console.log(context)
      // console.log(todoItem)
      // context.commit('CREATE_TODO', todoItem)
      commit('CREATE_TODO', todoItem)
    },

    deleteTodo: function ({ commit }, todoItem) {
      commit('DELETE_TODO', todoItem)
    },

    updateTodoStatus: function ({ commit }, todoItem) {
      commit('UPDATE_TODO_STATUS', todoItem)
    }
  },
  getters: {
    completedTodoscount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === true
      }).length
    },
    uncompletedTodoscount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
    allTodosCount: function (state) {
      return state.todos.length
    }
  },
  modules: {
  }
})
