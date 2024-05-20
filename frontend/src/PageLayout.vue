<template>
  <div class="containerLayout h-screen flex flex-col">
    <div class="header">
      <slot name="header"></slot>
    </div>

    <div class="innercontainer flex h-lvh flex-row bg-white w-full">
      <div class="sidebar  md:w-15 hidden md:inline-flex">
        <slot name="sidebar" id="sidebar"></slot>
      </div>
      <div class="main-content px-10">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<style></style>
