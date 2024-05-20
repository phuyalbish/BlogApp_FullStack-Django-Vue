<script>
import Dashboard from "./Dashboard.vue";
import Home from "./Home.vue";
import LoginSignUp from "./pages/LoginSignUp.vue";
import axios from "axios";
import store from "@/store/store";
export default {
  components: {
    LoginSignUp,
    Dashboard,
    Home
    
  },
  data(){
      return {
        API: "http://127.0.0.1:8000/",
        userData:"",
        access_token :localStorage.getItem("access_token"),
        refresh_token : localStorage.getItem("refresh_token"),
      }
  },

  async mounted(){
    if(this.access_token  && this.refresh_token){
          await axios.post(`${this.API}api/checkToken/`, {}, {
          headers: {
          "authorization": localStorage.getItem("access_token"),
          "content-Type": "application/json",
          }}).then(response =>{
              if(response.status == 200){
                // this.$store.userData = response.data.resData
                store.commit('updateUserData', response.data.resData)
                  // console.log(this.$store.userData)
              }
        })
      }
      else{
        this.$router.push('/')
      }
    }

};
</script>

<template>
  <router-view/>
</template>

<style></style>
