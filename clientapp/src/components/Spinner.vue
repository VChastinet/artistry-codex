<template>
<div id="loader"></div>
</template>

<style scoped>
#loader {
  margin: auto;
  margin-top: 25%;
  width: 100px;
  height: 100px;
  border-radius: 5px;
  border: solid #e91e63;
  animation: spin 1.5s infinite linear;
  z-index: 100;
}

@keyframes spin {
  0% {
    transform: rotate(0deg) scale(1);
    border-radius: 5px;
  } 50%{
    transform: rotate(360deg) scale(1.5);
    border-radius: 100px;
  } 100% {
    transform: rotate(720deg) scale(1);
    border-radius: 5px;
  }
}
</style>
<script lang="ts">
import Vue from "vue";

export default Vue.extend({
  name: "Spinner"
});
</script>