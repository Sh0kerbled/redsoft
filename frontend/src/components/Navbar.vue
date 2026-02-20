<template>
  <header
    class="container mx-auto px-6 py-6 flex items-center justify-between w-300"
  >
    <logo />

    <nav
      class="hidden md:flex items-center gap-16 text-sm font-medium text-gray-300 border border-gray-300 px-16 py-3.5 rounded-[40px] ml-[150px]"
    >
      <a
        v-for="link in links"
        :key="link.text"
        :href="link.href"
        class="hover:text-white transition text-[16px]"
      >
        {{ link.text }}
      </a>
    </nav>

    <div class="flex items-center gap-4">
      <button
        class="flex items-center gap-1 text-sm text-gray-300 hover:text-white transition"
      >
        <svg
          class="w-4 h-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M3 5h12M9 3v2m1.048 9.5A18.022 18.022 0 016.412 9m6.088 9h7M11 21l5-10 5 10M12.751 5C11.783 10.77 8.07 15.61 3 18.129"
          ></path>
        </svg>
        Eng
      </button>
      <button
        class="bg-red-700 hover:bg-red-600 text-white px-6 py-3 rounded-xl text-sm font-semibold transition shadow-[0_0_15px_rgba(220,38,38,0.4)]"
      >
        Sign in | Sign up
      </button>
    </div>
  </header>
</template>

<script setup>
import logo from "../assets/logo.vue";
const links = [
  { text: "About us", href: "#" },
  { text: "Features", href: "#" },
  { text: "FAQ", href: "#" },
  { text: "Pricing", href: "#" },
];
</script>
