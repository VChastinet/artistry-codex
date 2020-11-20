<template>
  <v-app>
    <StartScreen v-bind:hide="shouldHide" />
    <div>
    <div class="app-bar-bg"></div>
      <artistCard v-bind:artistDetails="artistDetails" />
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
      <div class="app-bar-cover" :class="{'reveal-bar': shouldHide}"></div>
    </div>
    <v-main>
      <ArtistList @loaded="hideStart" @itemClicked="showDetails" />
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

<script lang="ts">
import StartScreen from "@/components/StartScreen.vue";
import ArtistCard from "@/components/ArtistCard.vue";
import ArtistList from "@/views/ArtistList.vue";

function hideStart(isLoaded) {
  this.$data.shouldHide = isLoaded;
}

function showDetails(details) {
  console.log('details: ', details);
  this.artistDetails = details;
}

export default {
  name: "App",
  components: {
    StartScreen,
    ArtistList,
    ArtistCard,
  },
  methods: {
    hideStart,
    showDetails,
  },
  data () {
    return {
      shouldHide: false,
      artistDetails: null,
    }
  }
};
</script>

<style scoped>

footer {
  z-index: 99;
}

.v-main, .v-app-bar {
  max-width: 800px;
  margin: auto;
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