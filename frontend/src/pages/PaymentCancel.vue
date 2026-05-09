<template>
  <section
    class="min-h-screen flex flex-col items-center justify-center bg-[#0a0a0a] font-Montserrat"
  >
    <div class="flex flex-col items-center gap-6 text-center px-4">
      <div
        class="w-[72px] h-[72px] rounded-full bg-[#3a3a3a] flex items-center justify-center shadow-[0px_0px_20px_4px_#222]"
      >
        <div class="text-white text-[36px] font-bold leading-none">✕</div>
      </div>
      <h1 class="text-white text-[32px] font-bold">Payment Cancelled</h1>
      <p class="text-[#D9D9D9] text-[18px] max-w-[400px]">
        Your payment was cancelled. You can try again anytime.
      </p>
      <button
        @click="router.push('/#pricing')"
        class="mt-4 px-[48px] py-[12px] bg-[#8B0000] text-white text-[18px] rounded-[12px] hover:bg-[#a00000] transition-colors shadow-[0px_0px_7px_1px_#3E1112]"
      >
        Back to Pricing
      </button>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
</script>
