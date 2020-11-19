<template>
<v-list three-line>
    <template v-for="(item, index) in items">
      <v-list-item
        :key="item.title"
      >
        <v-list-item-avatar>
          <v-img :src="require(`@/assets/placeholders/profile_placeholder_${randomProfilePlaceholder()}.png`)"></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title v-html="item.name"></v-list-item-title>
          <v-list-item-subtitle v-html="listTags(item.tags)"></v-list-item-subtitle>
          <v-list-item-subtitle class="font-weight-bold" v-html="item.state.name"></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
      <v-divider
        :key="index"
        :inset="item.inset"
      ></v-divider>
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
    state: State,
    instagram_username: string,
    tags: Tag[],
}

interface Tag {
  id: number,
  name: string,
  description?: string,
}

interface State {
  id: number,
  uf: string,
  name: string,
}

const randomProfilePlaceholder = () => Math.floor(Math.random() * 8);

const listTags = (tags: Tag[]): string => tags.map(({ name }) => name).join(', ');

@Component({
  components: {
    // StartScreen
  },
  data: () => ({
    items: [] as Artist[],
    randomProfilePlaceholder,
    listTags
    }),
    mounted: async function() {
      const { data } = await axios.get('http://localhost:8000/api/artists/')
      this.items = data.results;

    }
})
export default class ArtistList extends Vue {}
</script>
