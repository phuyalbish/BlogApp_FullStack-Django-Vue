<template>
  <div class="containerLayout">
    <div class="header">
      <slot name="header"></slot>
    </div>

    <div class="innercontainer bg-white w-20">
      <div class="sidebar">
        <slot name="sidebar" id="sidebar"></slot>
      </div>
      <div class="main-content">
        <slot name="content"></slot>
      </div>
    </div>
  </div>
</template>

<style>
.containerLayout {
  display: flex;
  flex-direction: column;
  width: 100vw;
}
.sidebar {
  height: 100vh;
  background-color: #fff;
  width: 15vw;
}
.innercontainer {
  width: 100%;
  height: 100vh;
  background-color: cyan;
  display: flex;
  flex-direction: row;
}
.header {
  height: 10vh;
  background-color: #fff;
}
</style>
