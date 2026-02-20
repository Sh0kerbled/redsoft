<template>
  <div
    class="bg-[#07030A] min-h-screen text-white font-montserrat selection:bg-red-600 selection:text-white"
  >
    <Navbar />
    <main>
      <Hero />
      <About />
      <Features />
      <Advantages />
      <FAQ />
      <Pricing />
    </main>
  </div>
</template>

<script setup>
import Navbar from "./components/Navbar.vue";
import Hero from "./components/Hero.vue";
import About from "./components/About.vue";
import Features from "./components/Features.vue";
import Advantages from "./components/Advantages.vue";
import FAQ from "./components/FAQ.vue";
import Pricing from "./components/Pricing.vue";
</script>
