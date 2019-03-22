const mutations = {
  SET_LOGIN(state, data) {
    state.login = data;
  },
  SET_LOGIN_VISIBLE(state, data) {
    state.loginVisible = data;
  },
  SET_REGISTER_VISIBLE(state, data) {
    state.registerVisible = data;
  },
  SET_ORDER_VISIBLE(state, data) {
    state.orderVisible = data;
  },
  SET_ORDER_INFO(state, data) {
    state.order = data;
  }
};

export default mutations;
