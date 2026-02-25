<template>
  <div class="relative w-full w-[1200px] mx-auto min-h-screen">
    <!-- Navigation -->
    <Navbar />

    <!-- Main Content -->
    <main class="relative w-full bg-black rounded-[20px]">
      <!-- Auth Card -->
      <AuthCard />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import Navbar from "../components/authComponents/Navbar.vue";
import AuthCard from "../components/authComponents/AuthCard.vue";
import Footer from "../components/authComponents/Footer.vue";
</script>
