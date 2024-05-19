<template>
    <div class=" flex  justify-center mt-5 align-middle">

    <div
      v-if="is_shownLoginForm"
      class="LoginInSignUp z-50 flex flex-col items-center m-10 gap-4 p-10 md:w-4/6 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">Login to an Account</h3>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="loginData.email"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="loginData.password"
      />
      <p
        class="text-blue-900 cursor-pointer underline underline-offset-1"
        @click="ToggleSignUpDiv"
      >
        Create a new account
      </p>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="LoginSubmit"
      >
        Login
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>

    <div
      v-if="is_shownSignUpForm"
      class="LoginInSignUp z-50 flex flex-col items-center m-10 gap-4 p-10 md:w-4/6 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">Create New Account</h3>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="signUpData.email"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="signUpData.password"
      />
      <p
        class="text-blue-900 cursor-pointer underline underline-offset-1"
        @click="ToggleLoginDiv"
      >
        Already have an account?
      </p>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="RegisterSubmit"
      >
        SignUp
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
    </div>
</template>
<script>
import axios from 'axios';
export default{
        data(){
            return {
                access_token :localStorage.getItem("access_token"),
                refresh_token :localStorage.getItem("refresh_token"),
                API: "http://127.0.0.1:8000/",
                is_errorOccured : "",
                is_shownSignUpForm : false,
                is_shownLoginForm :true,
                is_LoggedIn: false,
                loginData: {
                    email: "",
                    password: "",
                },
                signUpData: {
                    email: "",
                    password: "",
                },
            }
        },
        mounted(){
            if(this.refresh_token){
                axios.post(`${this.API}api/checkToken/`, {}, {
                headers: {
                'RefreshToken': localStorage.getItem("refresh_token"),
                "authorization": localStorage.getItem("access_token"),
                "content-Type": "application/json",
                }}).then(response =>{
                    if(!this.access_token){
                        localStorage.setItem("refresh_token",response.data.resData.refreshJWT);
                        localStorage.setItem("access_token",response.data.resData.accessJWT);
                    }
                    if(response.status == 200){
                        this.$router.push('/dashboard')
                    }
                })
            }
            else{
                console.log("No Access Token Found")
            }
        },

         methods: {
            LoginSubmit() {


              if(this.loginData.email && this.loginData.password){
                axios
                  .post(`${this.API}api/logins/`, this.loginData, {
                    headers: {
                    "authorization": localStorage.getItem("access_token"),
                    "content-Type": "application/json",
                    },
                  })
                  .then((response) => {
                  if(response.status == 200){
                      localStorage.setItem("refresh_token",response.data.jwt.refreshJWT);
                      localStorage.setItem("access_token",response.data.jwt.accessJWT);
                      this.$router.push('/dashboard')
                      this.is_LoggedIn = true
                  }
                  }).catch(error => {
                        this.is_errorOccured = error.response.data
                  })
                }
        
    },

    RegisterSubmit() {
      axios({
        method: "post",
        url: `${this.API}api/register/`,
        headers: {
          "Content-Type": "application/json",
        },
        data: this.signUpData,
      }).then(response => {
        if (response.data.refreshJWT != undefined || response.data.accessJWT != undefined){
        localStorage.setItem("refresh_token",response.data.refreshJWT);
        localStorage.setItem("access_token",response.data.accessJWT);
        this.is_LoggedIn = true
        console.log(response)
        }
      });
    },
    ToggleLoginDiv() {
      this.is_shownSignUpForm = false;
      this.is_shownLoginForm = !this.is_shownLoginForm;
    },
    ToggleSignUpDiv() {
      this.is_shownLoginForm = false;
      this.is_shownSignUpForm = !this.is_shownSignUpForm;
    },
}

}
</script>