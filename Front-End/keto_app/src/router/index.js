import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import Signin from '../views/Signin.vue';
import Signup from '../views/Signup.vue';
import Profile from '../views/Profile.vue';
import Feed from '../views/Feed.vue';
import About from '../views/About.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/signin',
    name: 'Signin',
    component: Signin
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed
  },
  {
    path: '/about',
    name: 'About',
    component: About
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
