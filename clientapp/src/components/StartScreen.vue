<template>
<div class="component-container" id="componentContainer">
  <v-container>
    <v-icon class="logo" :class="{shrink: hide}" color="pink pink-3">
      mdi-palette
    </v-icon>
    <div class="title">
      <h1>Art Codex</h1>
      <h3>Welcome to the Art Codex</h3>
    </div>
    <Spinner class="spinner" />
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
</div>
</template>

<style scoped>
:root {
  --icon-top: 20;
  --icon-left: 20;
}
.component-container {
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 99;
  background-color: #FFF;
}

.title {
  position: fixed !important;
  text-align: center;
  left: calc(50% - 148px);
  top: calc(35% - 17px);
}

.logo {
  position: fixed !important;
  font-size: 130px !important;
  left: calc(50% - 65px);
  top: calc(25% - 65px);
}

.spinner {
  position: fixed !important;
  left: calc(50% - 50px);
  top: calc(60% - 50px);
}

.shrink {
  animation: shrink 1s 1s ease-in-out forwards;
}

@keyframes shrink {
  100% {
    opacity: .5;
    transform: scale(.2); 
    left: calc(var(--icon-left) - 53px );
    top: calc(var(--icon-top) - 53px);
  }
}

</style>

<script lang="ts">
import Vue from "vue";
import Spinner from "./Spinner.vue";

const hideScreen = (hide) => {
    let showComponent = false;
    if (hide) {
      setTimeout(() => {
        showComponent = hide;
        document.getElementById('componentContainer').classList.add('d-none');
      }, 2010);
    }
    return showComponent;
}

export default Vue.extend({
  name: 'StartScreen',
  components: { Spinner },
  props:['hide'],
  mounted: function() {
    hideScreen(this.hide);
    const root = document.documentElement;
    const iconTop = document.getElementById('logo-icon').getBoundingClientRect().top;
    const iconleft = document.getElementById('logo-icon').getBoundingClientRect().left;
    root.style.setProperty('--icon-top', `${iconTop}px`);
    root.style.setProperty('--icon-left', `${iconleft}px`);

  }
});
</script>
