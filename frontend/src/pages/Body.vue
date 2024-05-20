<script>
import axios from 'axios';
export default{

    data(){
        return {
            articleData: [],
            API: "http://127.0.0.1:8000/",
         }
    },
    mounted(){
          axios.get(`${this.API}api/articles/getAllArticle/`).then(response =>{
              console.log(response)
              this.articleData = response.data
        })
      }
}

</script>
<template>

    <div class="mt-10 articleContainer flex gap-5 flex-wrap flex-shrink">
        <div v-for="x in articleData" class="flex flex-col flex-wrap w-100  p-10 m-1 hover:p-11 hover:m-0 border bg-white rounded-lg shadow-md shadow-blue-400">
            <h2 class="text-2xl text-blue-900">{{x.title}}</h2>
            <p class="text-sm text-blue-400">{{ x.description }}</p>
            <div class="otherDetail flex justify-between  pt-5 align-middle">
                        <div class="detail flex flex-col align-middle">
                        <p class="text-sm text-blue-900">19th May,  0 likes </p>
                        <p class="text-sm">Bishal</p>
                        </div>
                        <div class="cursor-pointer  text-black text-lg  border hover:border-black-500  rounded-full px-2 align-middle">&#x1F44D;</div>
            </div>

        </div>

    </div>
</template>
<style></style>
