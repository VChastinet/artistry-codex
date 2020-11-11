<template>
  <v-app>
    <v-main>
      <StartScreen />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from "vue";
import StartScreen from "./components/StartScreen.vue";

export default Vue.extend({
  name: "App",

  components: {
    StartScreen
  },

  data: () => ({
    //
  })
});
</script>
