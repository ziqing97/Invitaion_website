import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeRoute',
    component: Home
  },
  {
    path: '/newyearwish',
    name: 'NewYearRoute',
    component: () => import('../views/NewYear.vue')
  },
  {
    path: '/moonfestivalwish',
    name: 'MoonFestivalRoute',
    component: () => import('../views/MoonFestival.vue')
  },
  {
    path: '/addinvitation',
    name: 'AddInvitationRoute',
    component: () => import('../views/AddInvitation.vue')
  },
  {
    path: '/AllInvitation',
    name: 'AllInvitationRoute',
    component: () => import('../views/AllInvitation.vue')
  },
  {
    path: '/invitation/:invitation_name',
    name: 'InvitationRoute',
    component: () => import('../views/InvitationView.vue')
  },
  {
    path: '/acknowledge/:acknowledge_name',
    name: 'AcknowledgementRoute',
    component: () => import('../views/AcknowledgementView.vue')
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
