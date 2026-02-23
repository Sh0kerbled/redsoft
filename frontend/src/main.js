import { createApp } from "vue";
import App from "./App.vue";
import "./main.css";
import AOS from "aos";
import "aos/dist/aos.css"; // Импорт стилей обязателен
createApp(App).mount("#app");

AOS.init({
  duration: 800,
  once: true,
});

app.mount("#app");
