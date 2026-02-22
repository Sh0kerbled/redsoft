<template>
  <section class="container mx-auto px-6 pt-20 pb-32 text-center relative">
    <div
      class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-64 bg-purple-900/20 blur-[120px] rounded-full pointer-events-none"
    ></div>

    <h1
      class="text-5xl md:text-6xl font-extrabold uppercase tracking-wide mb-2"
    >
      <span class="text-white">Your Steam</span><br />
      <span
        class="bg-clip-text text-transparent bg-gradient-to-r from-purple-400 via-purple-500 to-indigo-500"
        >Your Rules</span
      >
    </h1>

    <p
      class="text-gray-400 max-w-2xl mx-auto mt-6 text-sm md:text-base leading-relaxed"
    >
      REDSOFT is the ultimate tool for those who value their time and want to
      get the most out of their profile. Automate hour boosting, unlock any
      achievements, and manage your account collection in a single click.
    </p>

    <button
      class="mt-8 bg-red-700 hover:bg-red-600 text-white px-10 py-3 rounded-md font-bold transition shadow-[0_0_20px_rgba(220,38,38,0.5)]"
    >
      Download
    </button>

    <div class="relative mx-auto">
      <Main></Main>
    </div>
  </section>
</template>

<script setup>
import Main from "../assets/Main.vue";
</script>
