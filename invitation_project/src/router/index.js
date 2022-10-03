import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeRoute',
    component: Home
  },
  {
    path: '/invitation/:invitation_name',
    name: 'InvitationRoute',
    component: () => import('../views/InvitationView.vue')
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'ErrorRoute',
    component: () => import('../views/ErrorView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  mode: 'history',
  routes
})

export default router
