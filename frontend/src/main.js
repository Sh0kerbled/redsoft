import { createApp } from "vue";
import App from "./App.vue";
import "./main.css";
import AOS from "aos";
import "aos/dist/aos.css";
import router from "./router";
import axios from "axios";

axios.defaults.baseURL = "http://127.0.0.1:5173";

const app = createApp(App);

app.use(router);
app.provide("axios", axios);
app.mount("#app");

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
