import { createApp } from "vue";
import App from "./App.vue";
import "./main.css";
import AOS from "aos";
import "aos/dist/aos.css"; // Импорт стилей обязателен
import router from "./router";

createApp(App).use(router).mount("#app");
router.isReady().then(() => {
  AOS.init({
    once: true,
    duration: 800,
    easing: "ease-out-cubic",
    offset: 120,
    disableMutationObserver: true,
  });
});
if ("scrollRestoration" in history) {
  history.scrollRestoration = "manual";
}

app.mount("#app");
