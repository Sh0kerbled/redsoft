<template>
  <header class="w-full bg-black border-b border-[#434343]">
    <div
      class="max-w-[1200px] h-[100px] mx-auto px-[64px] flex items-center justify-between box-border relative"
    >
      <logo />

      <nav
        class="hidden md:flex items-center px-[40px] py-[8px] gap-[40px] h-[52px] border border-[#434343] rounded-[40px] absolute left-1/2 -translate-x-1/2"
      >
        <a
          v-for="link in menuLinks"
          :key="link.text"
          href="#"
          @click.prevent="scrollTo(link.id)"
          class="text-[#9D9D9D] hover:text-white font-medium text-[16px] leading-[20px] transition-colors whitespace-nowrap"
        >
          {{ link.text }}
        </a>
      </nav>

      <div class="flex items-center gap-8">
        <div class="relative inline-block" @mouseleave="isLangOpen = false">
          <div
            class="flex items-center gap-[3px] cursor-pointer group"
            @click="isLangOpen = !isLangOpen"
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
                :class="{ 'stroke-white': isLangOpen }"
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
              :class="isLangOpen ? 'text-white' : 'text-[#9D9D9D]'"
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
              v-if="isLangOpen"
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
          v-if="!isLoggedIn"
          to="/auth"
          class="flex items-center justify-center w-[158px] h-[44px] bg-[#8B0000] hover:bg-[#a80000] rounded-[12px] transition-colors"
        >
          <span class="text-[16px] font-semibold leading-5 text-white">
            Sign in | Sign up
          </span>
        </RouterLink>

        <div v-else class="relative" @mouseleave="isProfileOpen = false">
          <button
            @click="isProfileOpen = !isProfileOpen"
            class="flex items-center justify-center gap-[4px] w-[158px] h-[48px] bg-[#8B0000] hover:bg-[#a80000] rounded-[12px] transition-colors px-[12px]"
          >
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
              stroke="white"
              stroke-width="2"
            >
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
              <circle cx="12" cy="7" r="4" />
            </svg>
            <span
              class="text-[16px] font-semibold leading-[20px] text-white truncate max-w-[90px]"
            >
              {{ username }}
            </span>
          </button>

          <transition
            enter-active-class="transition duration-150 ease-out"
            enter-from-class="transform scale-95 opacity-0"
            enter-to-class="transform scale-100 opacity-100"
            leave-active-class="transition duration-100 ease-in"
            leave-from-class="transform scale-100 opacity-100"
            leave-to-class="transform scale-95 opacity-0"
          >
            <div
              v-if="isProfileOpen"
              class="absolute right-0 top-[56px] z-50 w-[264px] bg-white rounded-[20px] shadow-xl overflow-hidden"
            >
              <div class="flex flex-col p-[20px_24px] gap-3">
                <div
                  class="flex items-center gap-3 pb-3 border-b border-gray-200"
                >
                  <div
                    class="w-10 h-10 rounded-full bg-[#8B0000] flex items-center justify-center shrink-0"
                  >
                    <span class="text-white font-bold text-[16px]">{{
                      username[0]?.toUpperCase()
                    }}</span>
                  </div>
                  <div class="flex flex-col">
                    <span
                      class="font-semibold text-[16px] text-black leading-5"
                      >{{ username }}</span
                    >
                    <span class="text-[13px] text-gray-500">Steam account</span>
                  </div>
                </div>

                <button
                  @click="logout"
                  class="w-full flex items-center justify-center gap-2 h-[44px] bg-black hover:bg-[#1a1a1a] rounded-[12px] transition-colors mt-1"
                >
                  <svg
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="white"
                    stroke-width="2"
                  >
                    <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" />
                    <polyline points="16 17 21 12 16 7" />
                    <line x1="21" y1="12" x2="9" y2="12" />
                  </svg>
                  <span class="text-white font-semibold text-[16px]"
                    >Sign out</span
                  >
                </button>
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { useI18n } from "vue-i18n";
import logo from "../assets/logo.vue";

const { locale } = useI18n();
const router = useRouter();

const isLoggedIn = ref(
  !!(
    localStorage.getItem("auth_token") || localStorage.getItem("access_token")
  ),
);
const username = ref(localStorage.getItem("username") || "Profile");

const syncAuth = () => {
  isLoggedIn.value = !!(
    localStorage.getItem("auth_token") || localStorage.getItem("access_token")
  );
  username.value = localStorage.getItem("username") || "Profile";
};

onMounted(() => window.addEventListener("auth-changed", syncAuth));
onUnmounted(() => window.removeEventListener("auth-changed", syncAuth));

const isProfileOpen = ref(false);

const logout = () => {
  localStorage.removeItem("auth_token");
  localStorage.removeItem("access_token");
  localStorage.removeItem("refresh_token");
  localStorage.removeItem("username");
  isProfileOpen.value = false;
  window.dispatchEvent(new CustomEvent("auth-changed"));
  router.push("/auth");
};

const menuLinks = [
  { text: "About us", id: "about" },
  { text: "Features", id: "features" },
  { text: "FAQ", id: "faq" },
  { text: "Pricing", id: "pricing" },
];

function scrollTo(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
}

const isLangOpen = ref(false);

const languages = [
  { code: "kk", label: "Kaz" },
  { code: "ru", label: "Rus" },
  { code: "en", label: "Eng" },
  { code: "zh", label: "Chi" },
];

const savedLang =
  languages.find((l) => l.code === localStorage.getItem("lang")) ||
  languages[2];
const selectedLang = ref(savedLang);

const selectLanguage = (lang) => {
  selectedLang.value = lang;
  isLangOpen.value = false;
  locale.value = lang.code;
  localStorage.setItem("lang", lang.code);
};
</script>
