<script>
export default {
  components: {},
};
</script>
<template>
  <div class="header flex items-center p-5 justify-evenly">
    <div class="headerTitleAndTag flex flex-col align-middle">
      <div class="headerTitle text-2xl font-mono">AwsomeArticle</div>
      <div class="headerTag text-xs text-slate-500">
        Where articles gets shared
      </div>
    </div>
    <div
      class="searchbar flex align-middle border border-gray-500 rounded-full overflow-hidden shadow-inner shadow-gray-400"
    >
      <input type="text" class="outline-none px-4 bg-transparent" />
      <p class="p-1">&#128269;</p>
    </div>
    <div class="login_signup flex items-center gap-2">
      <p>Login</p>
      <div class="signup bg-blue-500 py-2 px-4 rounded-full text-white">
        Signup
      </div>
    </div>
  </div>
</template>
<style></style>
