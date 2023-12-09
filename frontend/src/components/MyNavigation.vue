<template>
  <!-- navigation -->
  <v-navigation-drawer
    :rail="rail"
    v-model="drawer"
    :model-value="getDrawer"
    class="bg-primary"
  >
    <v-list density="comfortable" nav>
      <v-list-item
        prepend-icon="mdi-menu"
        @click="drawer = !drawer"
        @click.stop="screenWidth >= 1280 ? (rail = !rail) : (rail = false)"
      ></v-list-item>
    </v-list>

    <!-- nav-menus -->
    <v-list density="comfortable" nav>
      <v-list-item
        prepend-icon="mdi-play-box"
        title="Demo"
        :to="{ name: 'Demo' }"
      ></v-list-item>
      <v-list-item
        prepend-icon="mdi-view-column"
        title="Report"
        :to="{ name: 'Report' }"
      ></v-list-item>
    </v-list>
  </v-navigation-drawer>

  <!-- app bar -->
  <v-app-bar flat class="bg-primary">
    <v-app-bar-title class="text-center pe-5">{{ getTitle }}</v-app-bar-title>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      rail: true,
      screenWidth: window.innerWidth,
    };
  },
  methods: {
    updateScreenWidth() {
      this.screenWidth = window.innerWidth;
    },
  },
  computed: {
    getDrawer() {
      if (this.screenWidth < 1280) {
        return this.drawer;
      } else {
        return true;
      }
    },
    getTitle() {
      return this.$route.name;
    },
  },
  mounted() {
    window.addEventListener("resize", this.updateScreenWidth);
  },
};
</script>

<style></style>
