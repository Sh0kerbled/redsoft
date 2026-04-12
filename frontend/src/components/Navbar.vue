<template>
  <header class="w-full bg-black border-b border-[#434343] font-Montserrat">
    <div
      class="max-w-[1200px] h-[100px] mx-auto px-16 flex items-center justify-between box-border"
    >
      <logo />

      <nav
        class="hidden md:flex items-center px-10 py-2 gap-16 h-[52px] border border-[#434343] rounded-[40px] ml-[200px]"
      >
        <a
          v-for="link in menuLinks"
          :key="link.text"
          href="#"
          @click.prevent="scrollTo(link.id)"
          class="text-[16px] font-medium leading-5 text-[#9D9D9D] hover:text-white transition-colors whitespace-nowrap"
        >
          {{ link.text }}
        </a>
      </nav>

      <div class="flex items-center gap-8">
        <div class="relative inline-block" @mouseleave="isOpen = false">
          <div
            class="flex items-center gap-[3px] cursor-pointer group"
            @click="isOpen = !isOpen"
          >
            <div class="w-6 h-6 flex items-center justify-center">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="#9D9D9D"
                stroke-width="2"
                class="transition-colors group-hover:stroke-white"
                :class="{ 'stroke-white': isOpen }"
              >
                <circle cx="12" cy="12" r="10"></circle>
                <line x1="2" y1="12" x2="22" y2="12"></line>
                <path
                  d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                ></path>
              </svg>
            </div>
            <span
              class="text-[16px] font-medium leading-5 transition-colors group-hover:text-white"
              :class="isOpen ? 'text-white' : 'text-[#9D9D9D]'"
            >
              {{ selectedLang.label }}
            </span>
          </div>

          <transition
            enter-active-class="transition duration-100 ease-out"
            enter-from-class="transform scale-95 opacity-0"
            enter-to-class="transform scale-100 opacity-100"
            leave-active-class="transition duration-75 ease-in"
            leave-from-class="transform scale-100 opacity-100"
            leave-to-class="transform scale-95 opacity-0"
          >
            <div
              v-if="isOpen"
              class="absolute right-0 z-50 mt-2 w-24 overflow-hidden rounded-lg bg-[#1a1a1a] border border-[#333] shadow-lg"
            >
              <ul class="flex flex-col py-1 m-0 list-none pl-0">
                <li
                  v-for="lang in languages"
                  :key="lang.code"
                  @click="selectLanguage(lang)"
                  class="px-4 py-2 text-[15px] font-medium cursor-pointer transition-colors hover:bg-[#333] hover:text-white"
                  :class="
                    selectedLang.code === lang.code
                      ? 'text-white bg-[#2a2a2a]'
                      : 'text-[#9D9D9D]'
                  "
                >
                  {{ lang.label }}
                </li>
              </ul>
            </div>
          </transition>
        </div>

        <RouterLink
          to="/auth"
          class="flex items-center justify-center w-[158px] h-[44px] bg-[#8B0000] hover:bg-[#a80000] rounded-[12px] transition-colors"
        >
          <span class="text-[16px] font-semibold leading-5 text-white">
            Sign in | Sign up
          </span>
        </RouterLink>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useI18n } from "vue-i18n";
import logo from "../assets/logo.vue";

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
</script>
