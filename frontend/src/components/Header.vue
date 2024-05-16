<script>
export default {
  components: {},
  data() {
    return {
      searchName: "",
      is_openPopupSideBar: true,
      is_showSearchPopUp: false,
      is_shownLoginForm: false,
      is_shownSignUpForm: false,
      is_errorOccured: "",
      loginData: {
        email: "",
        password: "",
      },
    };
  },
  watch: {
    searchName(newVal) {
      if (newVal == "") {
        this.is_showSearchPopUp = false;
      } else {
        this.is_showSearchPopUp = true;
        console.log(newVal);
      }
    },
  },
  methods: {
    searchArticles() {
      console.log(this.searchName);
    },
    offFocusSearchBar() {
      this.is_showSearchPopUp = false;
    },
    onFocusSearchBar() {
      if (this.searchName != "") {
        this.is_shownLoginForm = false;
        this.is_shownSignUpForm = false;
        this.is_showSearchPopUp = true;
      }
    },
    openClosePopupSideBar() {
      this.is_showSearchPopUp = false;
      this.is_shownLoginForm = false;
      this.is_shownSignUpForm = false;
      this.is_openPopupSideBar = !this.is_openPopupSideBar;
    },
    ToggleLoginDiv() {
      this.is_showSearchPopUp = false;
      this.is_shownSignUpForm = false;
      this.is_shownLoginForm = !this.is_shownLoginForm;
    },
    ToggleSignUpDiv() {
      this.is_showSearchPopUp = false;
      this.is_shownLoginForm = false;
      this.is_shownSignUpForm = !this.is_shownSignUpForm;
    },
  },
};
</script>
<template>
  <div
    class="header flex flex-wrap gap-4 items-center p-5 justify-between sm:justify-evenly"
  >
    <div class="headerTitleAndTag flex flex-col align-middle">
      <div class="headerTitle text-2xl text-blue-900 font-mono">
        AwsomeArticle
      </div>
      <div class="headerTag text-xs text-slate-500">
        Where articles gets shared
      </div>
    </div>

    <div
      class="hidden sm:flex searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400"
    >
      <input
        type="text"
        class="outline-none px-4 bg-transparent"
        placeholder="Search articles"
        v-model="searchName"
        @blur="offFocusSearchBar"
        @focus="onFocusSearchBar"
      />
      <p class="p-2">&#128269;</p>
    </div>

    <div
      class="threeBar md:invisible text-4xl text-blue-900 cursor-pointer select-none"
      @click="openClosePopupSideBar"
    >
      &Congruent;
    </div>
    <div class="login_signup hidden items-center gap-2 md:flex">
      <p class="text-blue-900 cursor-pointer" @click="ToggleLoginDiv">Login</p>
      <div
        class="signup bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="ToggleSignUpDiv"
      >
        Signup
      </div>
    </div>
    <div
      v-if="is_showSearchPopUp"
      class="z-20 searchField absolute top-36 z-2 w-5/6 h-20 sm:top-20 border rounded-lg shadow-md bg-white shadow-blue-400"
    ></div>

    <div
      v-if="is_shownLoginForm"
      class="LoginInSignUp z-40 flex flex-col items-center gap-4 p-10 w-5/6 absolute top-60 sm:top-40 md:top-20 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">LogIn to an Account</h3>

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
      >
        Login
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>

    <div
      v-if="is_shownSignUpForm"
      class="LoginInSignUp z-50 flex flex-col items-center gap-4 p-10 w-5/6 absolute top-60 sm:top-40 md:top-20 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <h3 class="text-2xl text-blue-900">Create New Account</h3>

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
        @click="ToggleLoginDiv"
      >
        Already have an account?
      </p>
      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
      >
        SignUp
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
    <div
      v-if="is_openPopupSideBar"
      class="flex flex-col items-center gap-4 z-10 p-5 popUpSidebar md:hidden w-5/6 absolute top-20 border bg-white rounded-lg shadow-md shadow-blue-400"
    >
      <div
        class="flex justify-between sm:hidden searchbar align-middle rounded-full overflow-hidden shadow-inner shadow-blue-400"
      >
        <input
          type="text"
          class="outline-none px-4 bg-transparent flex-grow"
          placeholder="Search articles"
          v-model="searchName"
          @blur="offFocusSearchBar"
          @focus="onFocusSearchBar"
        />
        <p class="p-2">&#128269;</p>
      </div>
      <div class="login_signup items-center gap-2 flex">
        <p class="text-blue-900 cursor-pointer" @click="ToggleLoginDiv">
          Login
        </p>
        <div
          class="signup bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
          @click="ToggleSignUpDiv"
        >
          Signup
        </div>
      </div>
    </div>
  </div>
</template>
<style></style>
