<script setup>
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useSubscriptionStore } from "../stores/subscription";
import { CheckCircle } from "lucide-vue-next";

const route = useRoute();
const router = useRouter();
const subStore = useSubscriptionStore();
const isProcessing = ref(true);
const error = ref("");

onMounted(async () => {
  const subscriptionId = route.query.subscription_id;
  const plan = route.query.plan;

  if (!subscriptionId || !plan) {
    error.value = "Неверные параметры";
    isProcessing.value = false;
    return;
  }

  try {
    const { data } = await import("../services/api").then((m) =>
      m.default.post("/payments/activate-subscription/", {
        subscription_id: subscriptionId,
        plan,
      }),
    );
    await subStore.fetchMySubscription();
    isProcessing.value = false;
  } catch (e) {
    error.value = "Ошибка активации: " + e.message;
    isProcessing.value = false;
  }
});
</script>

<template>
  <div
    class="min-h-screen bg-black flex items-center justify-center font-Montserrat"
  >
    <div class="flex flex-col items-center gap-6 text-center px-6">
      <div v-if="isProcessing" class="text-white text-xl">
        Активируем подписку...
      </div>

      <div v-else-if="error" class="text-red-400 text-xl">
        {{ error }}
        <button
          @click="router.push('/')"
          class="block mt-4 text-sm text-[#D9D9D9] underline"
        >
          Вернуться на главную
        </button>
      </div>

      <div v-else class="flex flex-col items-center gap-6">
        <CheckCircle class="w-20 h-20 text-green-400" :stroke-width="1.5" />
        <h1 class="text-white text-3xl font-bold">Подписка активирована!</h1>
        <p class="text-[#D9D9D9] text-lg">
          Добро пожаловать в RedSoft {{ subStore.plan.toUpperCase() }}
        </p>
        <button
          @click="router.push('/')"
          class="px-8 py-3 bg-[#8B0000] rounded-[12px] text-white hover:bg-[#a00000] transition-colors"
        >
          Начать использование
        </button>
      </div>
    </div>
  </div>
</template>
