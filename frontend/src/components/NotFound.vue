<script setup>
import { useRouter } from "vue-router";
import { Globe } from "lucide-vue-next";
import logo from "../assets/logo.vue";
import { RouterLink } from "vue-router";
import { ref } from "vue";
import { useI18n } from "vue-i18n";
import Navbar from "./Navbar.vue";
const { locale } = useI18n();

const menuLinks = [
  { text: "About us", id: "about" },
  { text: "Features", id: "features" },
  { text: "FAQ", id: "faq" },
  { text: "Pricing", id: "pricing" },
];

function scrollTo(id) {
  const el = document.getElementById(id);
  if (el) {
    el.scrollIntoView({ behavior: "smooth", block: "start" });
  }
}

const isOpen = ref(false);

const languages = [
  { code: "kk", label: "Kaz" },
  { code: "ru", label: "Rus" },
  { code: "en", label: "Eng" },
  { code: "zh", label: "Chi" },
];

const selectedLang = ref(languages[2]);

const selectLanguage = (lang) => {
  selectedLang.value = lang;
  isOpen.value = false;

  locale.value = lang.code;
  localStorage.setItem("lang", lang.code);
};
const router = useRouter();
const goHome = () => router.push("/");

import { onMounted, onUnmounted } from "vue";

const ellipseRef = ref(null);
let animFrame = null;
let startTime = null;

const ORBIT_RADIUS_X = 250; // радиус орбиты по X
const ORBIT_RADIUS_Y = 180; // радиус орбиты по Y
const DURATION = 10000; // 10 секунд на круг

function animateOrbit(timestamp) {
  if (!startTime) startTime = timestamp;
  const elapsed = timestamp - startTime;
  const progress = (elapsed % DURATION) / DURATION;
  const angle = progress * Math.PI * 2;

  const x = Math.cos(angle) * ORBIT_RADIUS_X;
  const y = Math.sin(angle) * ORBIT_RADIUS_Y;

  if (ellipseRef.value) {
    ellipseRef.value.style.transform = `translate(${x}px, ${y}px)`;
  }

  animFrame = requestAnimationFrame(animateOrbit);
}

onMounted(() => {
  animFrame = requestAnimationFrame(animateOrbit);
});

onUnmounted(() => {
  if (animFrame) cancelAnimationFrame(animFrame);
});
</script>

<template>
  <Navbar class="z-30"></Navbar>
  <div
    class="relative min-h-screen bg-black overflow-x-hidden flex flex-col items-center"
  >
    <!-- Страница 404 (Ошибка 404) -->
    <div class="relative w-full max-w-[1200px] h-[761px] mx-auto">
      <!-- Ellipse 161: фоновое свечение -->
      <div
        ref="ellipseRef"
        class="absolute rounded-full pointer-events-none z-0"
        style="
          width: 1014px;
          height: 1014px;
          left: 94px;
          top: -463px;
          background: linear-gradient(180deg, #990000 19.38%, #1000c4 138.02%);
          filter: blur(100px);
          will-change: transform;
        "
      ></div>

      <!-- 404 -->
      <h1
        class="absolute left-[321px] right-[320px] top-[120px] font-extrabold text-[200px] leading-[242px] text-center bg-clip-text z-10"
        style="
          background: linear-gradient(180deg, #ffffff 0%, #c4c4c4 100%);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
          background-clip: text;
          filter: drop-shadow(-24px 20px 52px rgba(0, 0, 0, 0.5));
        "
      >
        404
      </h1>

      <!-- We can't find that page -->
      <h2
        class="absolute w-[559px] left-[321px] top-[362px] font-Montserrat font-bold text-[24px] leading-[29px] text-center text-white z-10"
      >
        We can't find that page
      </h2>

      <!-- Описание -->
      <p
        class="absolute w-[559px] left-[321px] top-[415px] font-Montserrat font-normal text-[20px] leading-[24px] text-center text-white z-10"
      >
        The page has been deleted or never existed. Try to start the search
        again.
      </p>

      <!-- Btn enter -->
      <button
        @click="goHome"
        class="absolute w-[175px] h-[56px] top-[503px] left-1/2 -translate-x-1/2 flex items-center justify-center bg-[#8B0000] rounded-xl font-Montserrat font-bold text-[20px] leading-[24px] text-white z-10 hover:bg-[#A00000] transition-colors"
        style="box-shadow: 0px 0px 7px 1px #3e1112"
      >
        Sign in
      </button>
    </div>

    <!-- Footer -->
    <footer class="w-full bg-black border-t border-[#434343] z-10">
      <div
        class="w-full max-w-[1200px] mx-auto px-[80px] py-[96px] flex flex-row justify-between items-center gap-[181px]"
      >
        <!-- Frame 103: внутренний контейнер -->
        <div
          class="flex flex-row justify-between items-start flex-1 gap-[177px]"
        >
          <!-- Frame 100: Лого + описание -->
          <div class="flex flex-col gap-[24px] w-[383px] shrink-0">
            <!-- Frame 99: Лого -->
            <div class="flex flex-row items-center gap-[12px] h-[56px]">
              <div class="w-[56px] h-[56px] shrink-0"><logo /></div>
              <span
                class="font-Montserrat font-semibold text-[24px] leading-[26px] text-white"
                >REDSOFT</span
              >
            </div>
            <!-- Описание -->
            <p
              class="font-Montserrat font-normal text-[20px] leading-[26px] text-[#D9D9D9] w-[383px]"
            >
              Advanced automation and management tools for Steam. Professional
              dashboard, real-time monitoring, and secure stealth algorithms.
              Take full control of your assets.
            </p>
          </div>

          <!-- Frame 98: Навигация -->
          <div class="flex flex-row items-start gap-[120px] w-[415px] shrink-0">
            <!-- Frame 96: Product -->
            <div class="flex flex-col gap-[52px] w-[120px]">
              <span
                class="font-Montserrat font-semibold text-[24px] leading-[29px] text-white"
                >Product</span
              >
              <!-- Frame 95 -->
              <div class="flex flex-col gap-[24px]">
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >About us</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Features</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Advantages</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >FAQ</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Pricing</a
                >
              </div>
            </div>

            <!-- Frame 97: Legal & Safety -->
            <div class="flex flex-col gap-[52px] w-[175px]">
              <span
                class="font-Montserrat font-semibold text-[24px] leading-[29px] text-white"
                >Legal & Safety</span
              >
              <!-- Frame 95 -->
              <div class="flex flex-col gap-[24px]">
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Terms of Service</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Privacy Policy</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Cookie Policy</a
                >
                <a
                  href="#"
                  class="font-Montserrat font-normal text-[20px] leading-[24px] text-[#D9D9D9] hover:text-white transition-colors"
                  >Refund Policy</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<!-- Оставляем scoped для обычных стилей -->
<style scoped>
/* остальные ваши стили если есть */
</style>

<!-- Отдельный глобальный блок ТОЛЬКО для keyframes -->
<style>
@keyframes orbitLight {
  0% {
    transform: translate(0px, 0px);
  }
  25% {
    transform: translate(200px, 250px);
  }
  50% {
    transform: translate(0px, 300px);
  }
  75% {
    transform: translate(-200px, 150px);
  }
  100% {
    transform: translate(0px, 0px);
  }
}
</style>
