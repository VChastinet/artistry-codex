<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <StartScreen msg="Welcome to Your Vue.js + TypeScript App" />
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import StartScreen from "@/components/StartScreen.vue"; // @ is an alias to /src

@Component({
  components: {
    StartScreen
  }
})
export default class Home extends Vue {}
</script>
