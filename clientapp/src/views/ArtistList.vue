<template>
<v-list three-line>
    <template v-for="(item, index) in items">
      <button :key="item.title" v-on:click="() => openDetails(item.name)" class="text-left">
        <v-list-item>
          <v-list-item-avatar>
            <v-img :src="require(`@/assets/placeholders/profile_placeholder_${randomProfilePlaceholder()}.png`)"></v-img>
          </v-list-item-avatar>

          <v-list-item-content>
              <v-list-item-title v-html="item.name"></v-list-item-title>
              <v-list-item-subtitle v-html="listTags(item.tags)"></v-list-item-subtitle>
              <v-list-item-subtitle class="font-weight-bold" v-html="item.state.name"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </button>
      <v-divider
        :key="index"
        :inset="item.inset"
      ></v-divider>
    </template>
    </v-list>
</template>

<script lang="ts">
import { Artist, Tag } from "../interface";
import axios from "axios";

const randomProfilePlaceholder = () => Math.floor(Math.random() * 8);

const listTags = (tags: Tag[]): string => tags.map(({ name }) => name).join(', ');

function openDetails(details) {
  this.$emit('itemClicked', details);
};

async function loadArtists() {
  const { data } = await axios.get('http://localhost:8000/api/artists/');
  this.items = data.results;
  this.$emit('loaded', !!this.$data.items.length);
}

export default {
  data () {
    return {
      items: [] as Artist[],
      listTags,
    };
  },
  mounted() {
    this.loadArtists();
  },
  methods: {
    randomProfilePlaceholder,
    openDetails,
    loadArtists,
  },
};
</script>
