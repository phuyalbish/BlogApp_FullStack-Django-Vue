<script>
import axios from "axios";
import TopPage from "./modals/EditUser.vue";
import AddArticle from "./AddArticle.vue"
import store from "@/store/store";
import { mapGetters } from "vuex";

export default {
  components: {TopPage, AddArticle},
  props:[
      'user'
  ],
  data() {
    return {
      userData:"",
      articleData:"",
      searchName: "",
      is_openPopupSideBar: false,
      is_showSearchPopUp: false,
      editShow: false,
      addShow: false
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
    },
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
    logOut(){
         localStorage.removeItem("refresh_token");
         localStorage.removeItem("access_token");
         this.$router.push('/')
    },
    editClickOn() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = false;
      this.editShow = true;
    },

    editClickOff() {
      this.editShow = false;
    },
   addClickOn() {
      this.is_showSearchPopUp = false;
      this.is_openPopupSideBar = false;
      this.editShow = false;
      this.addShow = true;
    },

    addClickOff() {
      this.addShow = false;
    },

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
      {{userData.email }}
    </div>
    <div
      v-if="is_showSearchPopUp"
      class="z-20 searchField absolute top-36 z-2 w-5/6 h-20 sm:top-20 border rounded-lg shadow-md bg-white shadow-blue-400"
    ></div>
    
    <div
      v-if="is_openPopupSideBar"
      class="flex flex-col items-center gap-4 z-10 p-5 popUpSidebar w-5/6 absolute top-20 border bg-white rounded-lg shadow-md shadow-blue-400"
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
      <div class="addArticle" @click="addClickOn">Add Article</div>
      <div class="addProfile "  @click="editClickOn" >Edit Profile</div>
      <div class="addProfile "  @click="logOut" >LogOut</div>
    </div>
  </div>

  <AddArticle 
  v-show="addShow === true"
    @addShow="addClickOff"
    :articleData="articleData"
    />
  <TopPage
    class="EditProfile"
    v-show="editShow === true"
    @editShow="editClickOff"
    :userData="userData"
  />
</template>
<style></style>
