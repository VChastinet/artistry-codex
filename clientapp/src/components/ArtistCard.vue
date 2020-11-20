<template>
  <v-overlay :z-index="zIndex" :value="!!artistDetails">
    <v-card class="mx-auto" max-width="344">
      <v-img
        :src="require('@/assets/placeholders/image_placeholder.png')"
        height="200px"
      ></v-img>

      <v-avatar size="56">
        <img
          alt="user"
          :src="require(`@/assets/placeholders/profile_placeholder_${randomProfilePlaceholder()}.png`)"
        />
      </v-avatar>

      <v-card-title>
        Top western road trips
      </v-card-title>

      <v-card-subtitle>
        1,000 miles of wonder
      </v-card-subtitle>

      <v-card-actions>
        <v-btn color="orange lighten-2" text>
          Explore
        </v-btn>

        <v-spacer></v-spacer>

        <v-btn icon @click="show = !show">
          <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
        </v-btn>
      </v-card-actions>

      <v-expand-transition>
        <div v-show="show">
          <v-divider></v-divider>

          <v-card-text>
            I'm a thing. But, like most politicians, he promised more than he
            could deliver. You won't have time for sleeping, soldier, not with
            all the bed making you'll be doing. Then we'll go with that data
            file! Hey, you add a one and two zeros to that or we walk! You're
            going to do his laundry? I've got to find a way to escape.
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </v-overlay>
</template>
<script>

const randomProfilePlaceholder = () => Math.floor(Math.random() * 8);

export default {
  name: 'artistCard',
  props: ['artistDetails'],
  data () {
    return {
      zIndex: 100,
      show: false,
    };
  },

  methods: {
    randomProfilePlaceholder,
  },
};
</script>
