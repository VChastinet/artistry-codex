<template>
<v-list three-line>
    <template v-for="(item, index) in items">
      <v-subheader
        v-if="item.header"
        :key="item.header"
        v-text="item.header"
      ></v-subheader>

      <v-divider
        v-else-if="item.divider"
        :key="index"
        :inset="item.inset"
      ></v-divider>

      <v-list-item
        v-else
        :key="item.title"
      >
        <v-list-item-avatar>
          <v-img :src="item.portfolio"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-html="item.name"></v-list-item-title>
          <v-list-item-subtitle v-html="item.state"></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
    </v-list>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import axios from "axios";

interface ServerResponse {
  results,
  count,
  next,
  previous,
}

interface Artist {
    name: string,
    id: number,
    contact: string,
    portfolio: string,
    state: string,
    instagram_username: string,
    tags: Tag[],
}

interface Tag {
  id: number,
  name: string,
  description: string,
}


@Component({
  components: {
    // StartScreen
  },
  data: () => ({
    items: [] as Artist[],
    }),
    mounted: async function() {
      const { data } = await axios.get('http://localhost:8000/api/artists/')
      this.items = data.results;

    }
})
export default class ArtistList extends Vue {}
</script>
