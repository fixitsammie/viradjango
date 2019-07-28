import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import TVChartContainer from '@/components/TVChartContainer'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'tv',
      component: TVChartContainer
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/tv',
      name: 'tv',
      component: TVChartContainer
    }
  ]
})
