import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

export default function() {
  return new VueRouter({
    mode: 'history',
    scrollBehavior: () => ({
      x: 0,
      y: 0
    }),
    routes: [
      {
        path: '/',
        component: () => import('../pages/index/index.vue')
      },
      {
        path: '/view/:courseid/video/:videoid',
        component: () => import('../pages/video/index.vue'),
        props: true
      },
      {
        path: '/view/:id',
        component: () => import('../pages/view/index.vue'),
        props: true
      },
      {
        path: '/payment',
        component: () => import('../pages/payment/index.vue')
      }
    ]
  });
}
