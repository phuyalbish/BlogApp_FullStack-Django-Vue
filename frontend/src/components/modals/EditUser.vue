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



  <div class="LoginInSignUp z-50 flex flex-col items-center m-auto gap-4 p-10 md:w-4/6 border bg-white rounded-lg shadow-md shadow-blue-400">
      
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
        v-model="signUpData.email"
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
        v-model="signUpData.fname"
      />
      
      <div class="genderField  flex gap-6 outline-none p-3 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900">
              <label for="male"><input
        type="radio"
        id="male"
        value="male"
        name="gender"
        v-model="signUpData.gender"
      /> 
       Male</label>  
      
      <label for="female">
       <input
        type="radio"
        id="male"
        value="female"
        name="gender" selected="selected"
        v-model="signUpData.gender" 
      /> 
       Female</label>
      </div>

      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="RegisterSubmit"
      >
       Edit
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
</template>

<script>

export default {
  components: {
  },
  emits: ["editShow"],
  
  data() {
    return {

                signUpData: {
                    email: "",
                    password: "",
                    repassword:"",
                    fname:"",
                    // link:"",
                    gender:"male",
                    // img_src:"",

                },
      shownPage: "ZeroPageForm",
      is_changeData: false,
      is_errorOccured: false,
      errorMessage: "",
      userId: localStorage.getItem("userId"),
      API: import.meta.env.VITE_BACKEND_API_URL,
      userData: [],
      changedData: {},
      checkAvailability: false,
    };
  },
  watch: {
    userdetail(newVal) {
      console.log(newVal.email);
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

    nextFormPage() {
      if (this.shownPage === "FirstPageForm") this.shownPage = "SecondPageForm";
      else if (this.shownPage === "ZeroPageForm")
        this.shownPage = "FirstPageForm";
      else if (this.shownPage === "SecondPageForm")
        this.shownPage = "ThirdPageForm";
      else if (this.shownPage === "ThirdPageForm")
        this.shownPage = "FourthPageForm";
    },
    previousFormPage() {
      if (this.shownPage === "FourthPageForm") this.shownPage = "ThirdPageForm";
      else if (this.shownPage === "ThirdPageForm")
        this.shownPage = "SecondPageForm";
      else if (this.shownPage === "SecondPageForm")
        this.shownPage = "FirstPageForm";
    },
  },
};
</script>

<style>
</style>
