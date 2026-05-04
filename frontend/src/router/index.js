import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import Auth from "@/pages/Auth.vue";
import NotFound from "@/components/NotFound.vue";
import AOS from "aos";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "Home", component: Home },
    { path: "/Auth", name: "Auth", component: Auth },
    {
      path: "/:pathMatch(.*)*",
      name: "not-found",
      component: NotFound,
    },
  ],
  scrollBehavior(to) {
    if (to.hash) {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve({
            el: to.hash,
            behavior: "smooth",
            top: 100,
          });
        }, 300);
      });
    }
    return { top: 0 };
  },
});

router.afterEach(() => {
  setTimeout(() => {
    AOS.refreshHard();
  }, 300);
});

export default router;
