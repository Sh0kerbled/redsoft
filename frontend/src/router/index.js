import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/Home.vue";
import Auth from "@/pages/auth.vue";
import AOS from "aos";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: Home },
    { path: "/auth", component: Auth },
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
