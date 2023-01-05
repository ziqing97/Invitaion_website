import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'HomeRoute',
    component: Home,
    meta: {
      auth: true,
      title: '主页'
    }
  },
  {
    path: '/newyearwish',
    name: 'NewYearRoute',
    component: () => import('../views/NewYear.vue'),
    meta: {
      auth: true,
      title: '新年祝福'
    }
  },
  {
    path: '/moonfestivalwish',
    name: 'MoonFestivalRoute',
    component: () => import('../views/MoonFestival.vue'),
    meta: {
      auth: true,
      title: '中秋祝福'
    }
  },
  {
    path: '/addinvitation',
    name: 'AddInvitationRoute',
    component: () => import('../views/AddInvitation.vue'),
    meta: {
      auth: true,
      title: '添加新邀请'
    }
  },
  {
    path: '/AllInvitation',
    name: 'AllInvitationRoute',
    component: () => import('../views/AllInvitation.vue'),
    meta: {
      auth: true,
      title: '所有邀请'
    }
  },
  {
    path: '/invitation/:invitation_name',
    name: 'InvitationRoute',
    component: () => import('../views/InvitationView.vue'),
    meta: {
      auth: true,
      title: '邀请函'
    }
  },
  {
    path: '/invitation_longcheng',
    name: 'InvitationLongCheng',
    component: () => import('../views/invitation_longcheng.vue'),
    meta: {
      auth: true,
      title: '邀请函'
    }
  },
  {
    path: '/acknowledge/:acknowledge_name',
    name: 'AcknowledgementRoute',
    component: () => import('../views/AcknowledgementView.vue'),
    meta: {
      auth: true,
      title: '致谢函'
    }
  },
  {
    path: '/addsuccess/:invitation_name',
    name: 'AddSuccess',
    component: () => import('../views/AddSuccess.vue'),
    meta: {
      auth: true,
      title: '成功'
    }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'ErrorRoute',
    component: () => import('../views/ErrorView.vue'),
    meta: {
      auth: true,
      title: '错误'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
