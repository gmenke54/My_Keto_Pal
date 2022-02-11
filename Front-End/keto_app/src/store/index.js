import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    token: '',
    isAuthenticated: false,
    profile: null,
    user: {
      id: null,
      email: null
    },
    day: null,
    dispLabel: false,
    food: {
      days: [],
      name: 'Hover over a food to see details',
      weight: 0.0,
      carbs: 0.0,
      calories: 0.0,
      fat: 0.0,
      protein: 0.0,
      sugar: 0.0,
      fiber: 0.0,
      saturated: 0.0,
      trans: 0.0,
      chol: 0.0,
      sodium: 0.0,
      added_sugar: 0.0,
      chol_dv: 0.0,
      sodium_dv: 0.0
    },
    curCarbs: 0.0,
    curSugar: 0.0,
    curFat: 0.0,
    allDays: null,
    feed: []
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token');
        state.isAuthenticated = true;
      } else {
        state.token = '';
        state.isAuthenticated = false;
      }
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.isAuthenticated = false;
      state.token = '';
      console.log('removing token');
    },
    setUser(state, payload) {
      state.user = payload;
    },
    setProfile(state, payload) {
      state.profile = payload;
    },
    setDay(state, payload) {
      state.day = payload;
    },
    setFood(state, payload) {
      state.food = payload;
    },
    setDispLabel(state, payload) {
      state.dispLabel = payload;
    },
    setCurCarbs(state, payload) {
      state.curCarbs = payload;
    },
    setCurSugar(state, payload) {
      state.curSugar = payload;
    },
    setCurFat(state, payload) {
      state.curFat = payload;
    },
    setAllDays(state, payload) {
      state.allDays = payload;
    },
    setFeed(state, payload) {
      state.feed = payload;
    }
  },
  actions: {
    async setUserId(state) {
      const res = await axios.get('api/v1/users/');
      const curUser = {
        id: res.data[0].id,
        email: res.data[0].email
      };
      state.commit('setUser', curUser);
      try {
        const resp = await axios.get(
          `http://127.0.0.1:8000/profiles/${this.state.user.id}`
        );
        state.commit('setProfile', resp.data);
      } catch {}
    },
    async getFeed(state) {
      const posts = await axios.get('http://127.0.0.1:8000/posts');
      // const recipes = await axios.get('http://127.0.0.1:8000/recipes');
      // console.log(posts.data, recipes.data);
      // let feed = concat(posts.data, recipes.data);
      state.commit('setFeed', posts.data);
    }
  },
  modules: {}
});
