import { defineStore } from "pinia";
import { ref } from "vue";
import api from "../services/api";

export const useSubscriptionStore = defineStore("subscription", () => {
  const plan = ref("basic");
  const status = ref("free");
  const isLoading = ref(false);

  const fetchMySubscription = async () => {
    try {
      const { data } = await api.get("/payments/my-subscription/");
      plan.value = data.plan;
      status.value = data.status;
    } catch {}
  };

  const subscribe = async (planName) => {
    isLoading.value = true;
    try {
      const { data } = await api.post("/payments/create-subscription/", {
        plan: planName,
      });
      // Редиректим на PayPal
      window.location.href = data.approval_url;
    } catch (e) {
      alert("Ошибка: " + e.message);
    } finally {
      isLoading.value = false;
    }
  };

  const cancel = async () => {
    isLoading.value = true;
    try {
      await api.post("/payments/cancel-subscription/");
      plan.value = "basic";
      status.value = "free";
    } catch (e) {
      alert("Ошибка: " + e.message);
    } finally {
      isLoading.value = false;
    }
  };

  return { plan, status, isLoading, fetchMySubscription, subscribe, cancel };
});
