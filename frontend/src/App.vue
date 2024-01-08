<template>
    <v-app>
        <MyNavigation />
        <v-main class="mx-5 my-2">
            <router-view />
        </v-main>
        <MyAlert />
    </v-app>
</template>

<script>
import MyNavigation from "@/components/MyNavigation.vue";
import MyAlert from "@/components/MyAlert.vue";
import { useFetchedStore } from "./stores/fetched";

export default {
    setup() {
        const myStore = useFetchedStore();
        myStore.getInitData();
        return { myStore };
    },
    components: { MyAlert, MyNavigation },
};
</script>
