<template>
  <section
    class="min-h-screen flex flex-col items-center justify-center bg-[#0a0a0a] font-Montserrat"
  >
    <div class="flex flex-col items-center gap-6 text-center px-4">
      <div
        class="w-[72px] h-[72px] rounded-full bg-[#8B0000] flex items-center justify-center shadow-[0px_0px_20px_4px_#3E1112]"
      >
        <div
          class="w-[28px] h-[18px] border-l-[3px] border-b-[3px] border-white -rotate-45 -translate-y-[3px]"
        ></div>
      </div>
      <h1 class="text-white text-[32px] font-bold">Payment Successful!</h1>
      <p class="text-[#D9D9D9] text-[18px] max-w-[400px]">
        Your subscription has been activated. Enjoy your plan!
      </p>
      <button
        @click="router.push('/')"
        class="mt-4 px-[48px] py-[12px] bg-[#8B0000] text-white text-[18px] rounded-[12px] hover:bg-[#a00000] transition-colors shadow-[0px_0px_7px_1px_#3E1112]"
      >
        Go Home
      </button>
    </div>
  </section>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import axios from "axios";

const router = useRouter();
const route = useRoute();

onMounted(async () => {
  const subscriptionId = route.query.subscription_id;
  const plan = route.query.plan;

  if (!subscriptionId || !plan) return;

  try {
    const token = localStorage.getItem("access");
    await axios.post(
      "/payments/activate-subscription/",
      { subscription_id: subscriptionId, plan },
      { headers: { Authorization: `Bearer ${token}` } },
    );
  } catch (err) {
    console.error("Activation error:", err);
  }
});
</script>
