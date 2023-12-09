import { createRouter, createWebHistory } from "vue-router";
import DemoView from "../views/DemoView.vue";
import ReportView from "../views/ReportView.vue";

const routes = [
  {
    path: "/",
    name: "Demo",
    component: DemoView,
    alias: ["/demo"],
  },
  {
    path: "/report",
    name: "Report",
    component: ReportView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
