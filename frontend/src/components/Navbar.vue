<template>
  <header class="w-full bg-black border-b border-[#434343] font-['Montserrat']">
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
          class="text-[16px] font-medium leading-5 text-[#9D9D9D] hover:text-white transition-colors whitespace-nowrap"
        >
          {{ link.text }}
        </a>
      </nav>

      <div class="flex items-center gap-8">
        <div class="flex items-center gap-[3px] cursor-pointer group">
          <div class="w-6 h-6 flex items-center justify-center">
            <svg
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="#9D9D9D"
              stroke-width="2"
              class="group-hover:stroke-white transition-colors"
            >
              <circle cx="12" cy="12" r="10"></circle>
              <line x1="2" y1="12" x2="22" y2="12"></line>
              <path
                d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
              ></path>
            </svg>
          </div>
          <span
            class="text-[16px] font-medium leading-5 text-[#9D9D9D] group-hover:text-white transition-colors"
            >Eng</span
          >
        </div>

        <button
          class="flex items-center justify-center w-[158px] h-[44px] bg-[#8B0000] hover:bg-[#a80000] rounded-[12px] transition-colors"
        >
          <span class="text-[16px] font-semibold leading-5 text-white">
            Sign in | Sign up
          </span>
        </button>
      </div>
    </div>
  </header>
</template>

<script setup>
import logo from "../assets/logo.vue";
const menuLinks = [
  { text: "About us" },
  { text: "Features" },
  { text: "FAQ" },
  { text: "Pricing" },
];
</script>

<style>
body {
  margin: 0;
  background-color: #1a1a1a;
}
</style>
