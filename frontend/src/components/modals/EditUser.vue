<template>
  <!-- <div class="mainFormClass">
    <div class="dialogue">
      

      <div class="bgImg">
        <div class="innerFormClass">
          <component
            v-bind:is="shownPage"
            :userdetailData="userdetail"
            @next="nextFormPage"
            @back="previousFormPage"
          />
        </div>
      </div>
    </div>
  </div> --> 



  <div class="LoginInSignUp absolute z-50 flex flex-col items-center right-10 m-auto gap-4 p-10 md:w-6/6 border bg-white rounded-lg shadow-md shadow-blue-400">
      
      <div class="flex  w-full justify-between">
          <h3 class="text-2xl text-blue-900">Edit Account</h3>
            <div class="text-2xl text-blue-900 cursor-pointer" @click="toggleCloseEdit">
                &#x274c;
            </div>

      </div>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Email"
        v-model="userData.email"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Password"
        v-model="signUpData.password"
        @focus="validatePassword"
      />
      <input
        type="password"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="re-type Password"
        v-model="signUpData.repassword"
      />
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Full Name"
        v-model="userData.fname"
      />
      
      <div class="genderField  flex gap-6 outline-none p-3 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900">
              <label for="male"><input
        type="radio"
        id="male"
        value="male"
        name="gender"
        selected="selected"
        v-model="userData.gender"
      /> 
       Male</label>  
      
      <label for="female">
       <input
        type="radio"
        id="male"
        value="female"
        name="gender" selected="selected"
        v-model="userData.gender" 
      /> 
       Female</label>
      </div>

      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="editProfile"
      >
       Edit Profile
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
</template>

<script>
import store from '@/store/store';
export default {
  components: {
  },
  emits: ["editShow"],
  
  data() {
    return {

        API: "http://127.0.0.1:8000/",
      userData:"",
      signUpData:{
          password:"",
          repassword:""
      },
      gender:"",
      is_changeData: false,
      is_errorOccured: false,
      errorMessage: "",
      changedData: {},
      checkAvailability: false,
    };
  },

  computed:{
  getData(){
      return store.getters.getUserData
  }
  },
  watch: {
     getData(newVal){
        this.userData = newVal.resData
        this.gender = newVal.resData.gender
        console.log(this.gender)
    },
  },

  mounted() {
    console.log("Top Page mounted");
  },
  methods: {
    closeModal() {
      this.showModal = false;
    },
    toggleCloseEdit() {
      this.$emit("editShow");
    },

    editProfile(){
       axios.post(`${this.API}api/updateProfile/`, {}, {
              headers: {
              "content-Type": "application/json",
              }}).then(response =>{
                  if(response.status == 200){
                      console.log(response.data)
                  }
            })
    }

  },
};
</script>

<style>
</style>
