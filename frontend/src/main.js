import { createPinia } from "pinia";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

// icons
import "@mdi/font/css/materialdesignicons.css";

const myCustomLightTheme = {
  dark: false,
  colors: {
    background: "#FFFFFF",
    surface: "#FFFFFF",
    primary: "#7B1113",
    // "primary-darken-1": "#3700B3",
    secondary: "#FCAF17",
    // "secondary-darken-1": "#018786",
    error: "#B00020",
    info: "#2196F3",
    success: "#4CAF50",
    warning: "#FB8C00",
  },
};

const vuetify = createVuetify({
  components,
  directives,
  icons: {
    defaultSet: "mdi", // This is already the default value - only for display purposes
  },
  theme: {
    defaultTheme: "myCustomLightTheme",
    themes: {
      myCustomLightTheme,
    },
  },
});

const pinia = createPinia();

createApp(App).use(pinia).use(vuetify).use(router).mount("#app");
