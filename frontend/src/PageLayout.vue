<template>
  <div class="containerLayout h-screen flex flex-col">
    <div class="header">
      <slot name="header"></slot>
    </div>

    <div class="innercontainer flex h-lvh flex-row bg-white w-full">
      <div class="sidebar border border-blue-900 md:w-15 hidden md:inline-flex">
        <slot name="sidebar" id="sidebar"></slot>
      </div>
      <div class="main-content">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<style></style>
