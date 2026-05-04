<script setup>
import { ref, computed } from "vue";
import { ChevronLeft, ChevronRight } from "lucide-vue-next";
import MainPage from "../assets/Main page 1.svg";
import Game from "../assets/Game 3.svg";
import Accounts from "../assets/Accounts 1.svg";
const slides = [
  {
    id: "main",
    title: "Main page",
    image: MainPage,
    description:
      "The main page is an interactive dashboard for complete control over gaming processes and accounts. It centralizes the monitoring of launched games, personal user statistics, and the latest system news in a single workspace. Featuring a built-in advice block and a status bar with region and software version data, the dashboard provides instant access to all automation and security tools in real time.",
  },
  {
    id: "game",
    title: "Game page",
    image: Game,
    description:
      "The Games page is a high-performance control center designed for the seamless execution and management of automated gaming sessions. It enables users to initialize processes across multiple accounts, monitor real-time farm progress, and manage active game instances with precision. By integrating granular session controls with instant status feedback, the page ensures a streamlined transition from account activation to full-scale automation and performance tracking.",
  },
  {
    id: "accounts",
    title: "Accounts page",
    image: Accounts,
    description:
      "The Accounts page is a robust management hub for the secure organization and synchronization of all linked profiles. It provides a structured environment for adding, authenticating, and categorizing multiple Steam accounts with end-end data integrity. With a focus on intuitive navigation and rapid profile switching, this workspace allows users to maintain full control over their account database, ensuring that every identity is verified and ready for seamless integration.",
  },
];

const currentIndex = ref(0);

// Переключение слайдов (User Flow: бесконечный цикл)
const nextSlide = () => {
  currentIndex.value = (currentIndex.value + 1) % slides.length;
};

const prevSlide = () => {
  currentIndex.value = (currentIndex.value - 1 + slides.length) % slides.length;
};

// Вычисление позиций слайдов (что слева, что по центру, что справа)
const getSlideClass = (index) => {
  if (index === currentIndex.value) {
    return "slide-active";
  } else if (
    index ===
    (currentIndex.value - 1 + slides.length) % slides.length
  ) {
    return "slide-prev";
  } else {
    return "slide-next";
  }
};
</script>

<template>
  <section
    id="features"
    class="flex flex-col items-center justify-center py-24 px-5 relative bg-[#000000] w-full max-w-[1200px] mx-auto rounded-[40px] overflow-hidden my-20"
  >
    <!-- Красный Blur эффект на фоне -->
    <div
      class="absolute w-[736px] h-[563px] top-24 left-1/2 -translate-x-1/2 bg-[#560000] blur-[60px] rounded-full z-0 pointer-events-none"
    ></div>

    <!-- Заголовок -->
    <h2
      class="text-white text-[32px] font-bold font-['Montserrat'] leading-[39px] text-center z-10 mb-16"
    >
      Features
    </h2>

    <div
      class="relative w-full max-w-[1040px] h-[620px] flex flex-col items-center z-10"
    >
      <!-- Контейнер с изображениями (Карусель) -->
      <div class="relative w-full h-[421px] flex justify-center items-center">
        <div
          v-for="(slide, index) in slides"
          :key="slide.id"
          class="absolute transition-all duration-500 ease-in-out rounded-[20px] overflow-hidden bg-black"
          :class="getSlideClass(index)"
        >
          <img
            :src="slide.image"
            :alt="slide.title"
            class="w-full h-full object-cover"
          />

          <!-- Градиент для неактивных слайдов -->
          <div
            v-if="index !== currentIndex"
            class="absolute inset-0 bg-black/60 pointer-events-none transition-opacity duration-500"
          ></div>
        </div>
      </div>

      <!-- Текстовое описание активного слайда -->
      <div
        class="w-full mt-10 px-8 flex flex-col gap-4 text-center items-center h-[175px]"
      >
        <transition name="fade" mode="out-in">
          <div
            :key="currentIndex"
            class="w-full max-w-[976px] flex flex-col gap-4"
          >
            <h3
              class="text-white text-[32px] font-semibold font-['Montserrat'] leading-[39px]"
            >
              {{ slides[currentIndex].title }}
            </h3>
            <p
              class="text-[#F5F5F5] text-[20px] font-normal font-['Montserrat'] leading-[24px] text-justify"
            >
              {{ slides[currentIndex].description }}
            </p>
          </div>
        </transition>
      </div>

      <!-- Кнопки навигации -->
      <button
        @click="prevSlide"
        class="absolute left-[80px] top-[180px] w-[64px] h-[62px] bg-[#1F1E1E] border-2 border-[#434343] rounded-full flex items-center justify-center hover:border-white transition-colors duration-300 z-20 group"
      >
        <ChevronLeft
          class="text-white w-8 h-8 group-hover:-translate-x-1 transition-transform"
        />
      </button>

      <button
        @click="nextSlide"
        class="absolute right-[80px] top-[180px] w-[64px] h-[62px] bg-[#1F1E1E] border-2 border-[#434343] rounded-full flex items-center justify-center hover:border-white transition-colors duration-300 z-20 group"
      >
        <ChevronRight
          class="text-white w-8 h-8 group-hover:translate-x-1 transition-transform"
        />
      </button>
    </div>
  </section>
</template>

<style scoped>
/* Анимации текста */
.fade-enter-active,
.fade-leave-active {
  transition:
    opacity 0.3s ease,
    transform 0.3s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(10px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

/* Стили для Карусели изображений */
.slide-active {
  width: 736px;
  height: 421px;
  z-index: 10;
  transform: translateX(0) scale(1);
  box-shadow:
    -32px -20px 120px rgba(121, 91, 255, 0.24),
    32px 20px 120px rgba(121, 91, 255, 0.24);
  opacity: 1;
}

.slide-prev {
  width: 600px;
  height: 338px;
  z-index: 5;
  transform: translateX(-220px) scale(0.9);
  opacity: 0.8;
}

.slide-next {
  width: 600px;
  height: 338px;
  z-index: 5;
  transform: translateX(220px) scale(0.9);
  opacity: 0.8;
}
</style>
