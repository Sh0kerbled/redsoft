<script setup>
import { useRouter } from "vue-router";
import { XCircle } from "lucide-vue-next";
const router = useRouter();
</script>

<template>
  <div
    class="min-h-screen bg-black flex items-center justify-center font-Montserrat"
  >
    <div class="flex flex-col items-center gap-6 text-center px-6">
      <XCircle class="w-20 h-20 text-red-500" :stroke-width="1.5" />
      <h1 class="text-white text-3xl font-bold">Оплата отменена</h1>
      <p class="text-[#D9D9D9] text-lg">
        Вы можете попробовать снова в любое время
      </p>
      <button
        @click="router.push('/')"
        class="px-8 py-3 bg-[#8B0000] rounded-[12px] text-white hover:bg-[#a00000] transition-colors"
      >
        Вернуться назад
      </button>
    </div>
  </div>
</template>
