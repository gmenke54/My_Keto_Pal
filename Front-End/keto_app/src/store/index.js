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
    }
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
    }
  },
  actions: {
    async setUserId(state) {
      const res = await axios.get('api/v1/users/');
      console.log(res.data[0]);
      const curUser = {
        id: res.data[0].id,
        email: res.data[0].email
      };
      state.commit('setUser', curUser);
      try {
        const resp = await axios.get(
          `http://127.0.0.1:8000/profiles/${this.state.user.id}`
        );
        console.log(resp.data);
        state.commit('setProfile', resp.data);
      } catch {
        console.log('no profile found');
      }
    }
  },
  modules: {}
});
