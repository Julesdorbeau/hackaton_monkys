import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from "../components/Homepage/Login";
import Dashboard from "../components/DashBoard/DashBoard";

import TasteTest from "../components/TestPersonality/TasteTest";
import Homepage from "../components/Homepage/Homepage";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
    props: {}
  }, {
    path: '/TasteTest',
    name: 'TasteTest',
    component: TasteTest,
    props: {}
  },
  {
    path: '/Login',
    name: 'Login',
    component: Login,
    props: {}
  }]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
