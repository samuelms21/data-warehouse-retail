<template>
  <v-snackbar
    v-model="visible"
    :color="color"
    :timeout="timeout"
    class="text-caption"
  >
    {{ message }}
  </v-snackbar>
</template>
<script>
import { useFetchedStore } from "../stores/fetched";
import { ref, watch } from "vue";

export default {
  props: {
    message: {
      type: String,
      default: "Unknown error",
    },
    color: {
      type: String,
      default: "red", // Change the default color as needed
    },
    timeout: {
      type: Number,
      default: 5000, // Default timeout in milliseconds (adjust as needed)
    },
  },
  setup(props) {
    const myStore = useFetchedStore();
    const visible = ref(false);
    const message = ref("");

    // Watch for changes in apiErrorMessage and show the alert
    watch(
      () => myStore.apiErrorMessage,
      (newMessage) => {
        if (newMessage) {
          message.value = newMessage;
          visible.value = true;

          // Automatically hide the alert after the specified timeout
          setTimeout(() => {
            visible.value = false;
          }, props.timeout);
        }
      }
    );

    return { visible, message };
  },
};
</script>
<style></style>
