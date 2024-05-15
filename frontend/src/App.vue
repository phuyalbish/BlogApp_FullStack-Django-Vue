<script>
import PageLayout from "./PageLayout.vue";
import Header from "./components/Header.vue";
import Sidebar from "./components/Sidebar.vue";

export default {
  components: {
    PageLayout,
    Header,
    Sidebar,
  },
};
</script>

<template>
  <PageLayout id="display-flex">
    <template #sidebar>
      <Sidebar />
    </template>
    <template #header>
      <Header />
    </template>
    <template #content>
      <router-view />
    </template>
  </PageLayout>
</template>

<style></style>
