<template>
  <div
    class="bg-black min-h-screen text-white font-montserrat selection:bg-red-600 selection:text-white"
  >
    <Navbar class="sticky top-0 z-50" />
    <main>
      <Hero />
      <About class="relative z-40" />
      <Features />
      <Advantages />
      <FAQ />
      <Pricing />
    </main>
    <Footer />
  </div>
</template>

<script setup>
import Navbar from "@/components/Navbar.vue";
import Hero from "@/components/Hero.vue";
import About from "@/components/About.vue";
import Features from "@/components/Features.vue";
import Advantages from "@/components/Advantages.vue";
import FAQ from "@/components/FAQ.vue";
import Pricing from "@/components/Pricing.vue";
import Footer from "@/components/Footer.vue";
</script>
