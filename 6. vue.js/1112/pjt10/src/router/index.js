import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Random from '../views/Random.vue'
import MyMovieList from '../views/MyMovieList'
import MyMovieDetail from '../views/MyMovieDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
  {
    path: '/my-movie-list',
    name: 'MyMovieList',
    component: MyMovieList
  },
  {
    path: '/my-movie-detail/:movieId',
    name: 'MyMovieDetail',
    component: MyMovieDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
