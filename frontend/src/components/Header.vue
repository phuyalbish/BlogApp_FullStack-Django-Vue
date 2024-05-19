<script>
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      searchName: "",
      is_openPopupSideBar: true,
      is_showSearchPopUp: false,
    };
  },
  mounted(){
    if(this.access_token){
          axios.post(`${this.API}api/checkToken/`, {}, {
          headers: {
          "authorization": localStorage.getItem("access_token"),
          "content-Type": "application/json",
          }}).then(response =>{
              this.userData.fname = response.data.email
              this.is_LoggedIn = true
        })
      }
      else{
        console.log("No Access Token Found")
      }
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
        this.is_showSearchPopUp = true;
      }
    },
    openClosePopupSideBar() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = !this.is_openPopupSideBar;
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
      class="threeBar text-2xl text-blue-900 cursor-pointer select-none"
      @click="openClosePopupSideBar"
    >
      <!-- {{ this.userData.fname }} -->
    </div>
    <div
      v-if="is_showSearchPopUp"
      class="z-20 searchField absolute top-36 z-2 w-5/6 h-20 sm:top-20 border rounded-lg shadow-md bg-white shadow-blue-400"
    ></div>

    
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
      logout
    
    </div>
  </div>
</template>
<style></style>
