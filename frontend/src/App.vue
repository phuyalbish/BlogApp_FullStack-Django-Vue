<script>
import Dashboard from "./Dashboard.vue";
import Home from "./Home.vue";
import LoginSignUp from "./components/LoginSignUp.vue";
import axios from "axios";
export default {
  components: {
    LoginSignUp,
    Dashboard,
    Home
    
  },
  data(){
      return {
      }
  },

};
</script>

<template>
  <router-view/>
</template>

<style></style>
