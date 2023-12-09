<template>
  <v-app>
    <MyNavigation />
    <v-main class="mx-5 my-2">
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import MyNavigation from "@/components/MyNavigation.vue";

export default {
  components: { MyNavigation },
};
</script>
