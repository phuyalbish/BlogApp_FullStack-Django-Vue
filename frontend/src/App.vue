<script>
import PageLayout from "./PageLayout.vue";
import Header from "./components/Header.vue";
import Sidebar from "./components/Sidebar.vue";
import Body from "./pages/Body.vue";

export default {
  components: {
    PageLayout,
    Header,
    Sidebar,
    Body,
  },
};
</script>

<template>
  <PageLayout id="display-flex">
    <template #sidebar>
      <Sidebar class="" />
    </template>
    <template #header>
      <Header />
    </template>
    <template #content>
      <Body />
    </template>
  </PageLayout>
</template>

<style></style>
