<template>
  <div class="relative w-full w-[1200px] mx-auto min-h-screen">
    <Navbar />

    <main class="relative w-full bg-black rounded-[20px]">
      <AuthCard />
    </main>

    <Footer />
  </div>
</template>

<script setup>
import Navbar from "../components/authComponents/Navbar.vue";
import AuthCard from "../components/authComponents/AuthCard.vue";
import Footer from "../components/authComponents/Footer.vue";
</script>
<script>
import axios from "axios";

export default {
  name: "SignInSignUp",
};
</script>
