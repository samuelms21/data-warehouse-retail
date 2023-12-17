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
import { useFetchedStore } from "./stores/fetched";

export default {
  setup() {
    const myStore = useFetchedStore();
    myStore.callAPIs();
    return { myStore };
  },
  components: { MyNavigation },
};
</script>
