import { createStore } from "vuex";
export default createStore({
  state: {
    navbarState: "home",
    userData: Object,
  },
  mutations:{
    updateUserData(state, userData) {
    state.userData =  userData;
    },
  },
  getters:{
    getUserData: state =>  state.userData
  }
});
