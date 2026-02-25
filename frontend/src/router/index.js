import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import auth from "@/pages/auth.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/auth", component: auth },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
