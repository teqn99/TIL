import Vue from 'vue'
import VueRouter from 'vue-router'
import TheLunch from '@/views/TheLunch'
import TheLotto from '@/views/TheLotto'
import TheYoutube from '@/views/TheYoutube'

Vue.use(VueRouter)

const routes = [
  {
    path: '/lunch',
    name: 'TheLunch',
    component: TheLunch,
  },
  {
    path: '/lotto',
    name: 'TheLotto',
    component: TheLotto,
  },
  {
    path: '/youtube',
    name: 'TheYoutube',
    component: TheYoutube,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
