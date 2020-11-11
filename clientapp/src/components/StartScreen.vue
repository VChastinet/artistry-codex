<template>
<v-container>
  <div class="title-container">
    <v-icon class="logo" x-large color="pink pink-3">
      mdi-palette
    </v-icon>
    <h1>Art Codex</h1>
    <h3>Welcome to the Art Codex</h3>
  </div>
  <Spinner />
  <v-footer
    absolute
    class="font-weight-medium"
  >
    <v-col
      class="text-center"
      cols="12"
    >
      Coded with <v-icon color="pink pink-3">mdi-heart-circle</v-icon> by <a class="font-weight-bold pink--text accent-3" href="http://chastinet.dev" target="_blank">Victor Chastinet</a>
    </v-col>
  </v-footer>
</v-container>
</template>

<style scoped>
.title-container {
  margin: auto;
  text-align: center;
  margin-top: 30%
}
.logo {
  font-size: 130px !important;
}
</style>

<script lang="ts">
import Vue from "vue";
import Spinner from "./Spinner.vue";

export default Vue.extend({
  name: "StartScreen",
  components: { Spinner }
});
</script>
