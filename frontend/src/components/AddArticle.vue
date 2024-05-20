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

 <div class="LoginInSignUp right-10 z-50 absolute flex flex-col items-center m-auto gap-4 p-10 border bg-white rounded-lg shadow-md shadow-blue-400">
      
      <div class="flex  w-full justify-between">
          <h3 class="text-2xl text-blue-900">Add Article</h3>
            <div class="text-2xl text-blue-900 cursor-pointer" @click="toggleCloseAdd">
                &#x274c;
            </div>

      </div>

      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Title"
        v-model="article.title"
      />
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Description"
        v-model="article.description"
      />
      <input
        type="text"
        class="outline-none p-2 flex-grow rounded-full overflow-hidden shadow-inner shadow-blue-400 text-blue-900"
        placeholder="Further Reading(Link)"
        v-model="article.further_readings"
      />

      <div
        class="LoginSubmit bg-blue-800 py-2 px-4 rounded-full text-white shadow-blue-400 cursor-pointer hover:bg-white hover:text-blue-800 shadow-md"
        @click="addArticle"
      >
       Add Article
      </div>
      <p v-if="is_errorOccured != false" class="text-red-900 text-sm">
        {{ is_errorOccured }}
      </p>
    </div>
</template>

<script>
import axios from 'axios';
export default {
  components: {
  },
  emits: ["addShow"],
  props: {

  },
  data() {
    return {

        API: "http://127.0.0.1:8000/",

        article: {
            title:"",
            description:"",
            further_readings:"",
        },
      shownPage: "ZeroPageForm",
      is_changeData: false,
      is_errorOccured: false,
      errorMessage: "",
      userId: localStorage.getItem("userId"),
      changedData: {},
      checkAvailability: false,

    };
  },
  watch: {
  },

  mounted() {
  },
  methods: {
    addArticle(){
       axios.post(`${this.API}api/articles/addArticle/`, this.article, {
          headers: {
          }}).then(response =>{
              console.log(response)
              this.toggleCloseAdd()
        })
    },
    toggleCloseAdd() {
      this.$emit("addShow");
    },

  },
};
</script>

<style>
</style>
