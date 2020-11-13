<template>
  <v-app>
    <StartScreen v-bind:hide="hideStart" />
    <div>
    <div class="app-bar-bg"></div>
      <v-app-bar
        colapse="true"
        color="pink pink-3"
        dense
        dark
        flat
      >
        <v-icon id="logo-icon">mdi-palette</v-icon>

        <v-spacer></v-spacer>

        <v-toolbar-title>Artist Alley</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-app-bar>
      <div class="app-bar-cover" :class="{'reveal-bar': hideStart}"></div>
    </div>
    <v-main>
      <ArtistList />
    </v-main>
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
  </v-app>
</template>

<style scoped>
.v-main, .v-app-bar {
  max-width: 800px;
  margin: auto;
  z-index: 98;
}

.app-bar-bg {
  width: 100%;
  height: 48px;
  background-color: #e91e63;
  position: absolute;
  top: 0;
  left: 0;
}

.app-bar-cover {
  width: 100%;
  height: 48px;
  background-color: #FFF;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 98;
}

.reveal-bar {
  animation: reveal-bar .6s 1.7s linear forwards;
}

@keyframes reveal-bar {
  to {
    opacity: 0;
  }
}

</style>

<script lang="ts">
import Vue from "vue";
import StartScreen from "@/components/StartScreen.vue";
import ArtistList from "@/views/ArtistList.vue";

const hideStart = true;

export default Vue.extend({
  name: "App",

  components: {
    StartScreen,
    ArtistList,
  },

  data: () => ({
    hideStart,
  })
});
</script>
