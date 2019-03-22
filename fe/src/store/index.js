import Vue from 'vue';
import Vuex from 'vuex';
import * as actions from './action';
import * as getters from './getters';
import mutations from './mutations';

Vue.use(Vuex);

const state = {
    login: false,
    loginVisible: false,
    registerVisible: false,
    orderVisible: false,
    order: {}
}

export default function() {
    return new Vuex.Store({
        state,
        actions,
        mutations,
        getters
    })
}
