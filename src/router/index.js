import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import SettingPage from '../views/SettingPage.vue'
import QuestionPage from '../views/QuestionPage.vue'
import TableView from '../views/TableView.vue'
import InfoTask from '../views/InfoTask.vue'
import OtherPage from '../views/OtherPage'

const routes = [
  {
    path: '/',
    name: 'login',
    component: LoginView
  },
  {
    path: '/home',
    name: 'home',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/HomeView.vue')
  },
  {
    path: '/setting',
    name: 'setting',
    component: SettingPage
  },
  {
    path: '/question',
    name: 'question',
    component: QuestionPage
  },
  {
    path: '/other',
    name: 'other',
    component: OtherPage
  },
  {
    path: '/table',
    name: 'table',
    component: TableView
  },
  {
    path: '/info',
    name: 'info',
    component: InfoTask
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
