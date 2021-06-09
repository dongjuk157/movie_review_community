import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/Signup.vue'
import Login from '@/views/Login.vue'
import Movies from '@/views/Movies.vue'
import Community from '@/views/Community.vue'
import MyPage from '@/views/MyPage.vue'
import Recommend from '@/views/Recommend.vue'
import CreateReview from '@/components/CreateReview.vue'
import UpdateReview from '@/components/UpdateReview.vue'
import ReviewDetail from '@/components/ReviewDetail.vue'

Vue.use(VueRouter)

const routes = [
  {
    path:'signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path:'',
    name: 'Login',
    component: Login,
  },
  {
    path:'movies',
    name: 'Movies',
    component: Movies,
  },
  {
    path:'recommend',
    name: 'Recommend',
    component: Recommend,
  },
  {
    path:'community',
    name: 'Community',
    component: Community,
  },
  {
    path:'mypage',
    name: 'MyPage',
    component: MyPage,
  },
  {
    path:'review',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path:'review',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path:'update',
    name: 'UpdateReview',
    component: UpdateReview,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
