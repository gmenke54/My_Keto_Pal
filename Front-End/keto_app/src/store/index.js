import { createStore } from 'vuex';

export default createStore({
  state: {
    token: '',
    isAuthenticated: false
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
    }
  },
  actions: {},
  modules: {}
});
