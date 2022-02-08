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
    day: null
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
