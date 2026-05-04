<script setup>
import { ref } from "vue";
import { Plus, Minus } from "lucide-vue-next";

const faqs = [
  // ... ваш массив faqs остается без изменений
  {
    id: 1,
    question: "What is RedSoft?",
    answer:
      "RedSoft is a professional Steam account management system designed for safe automation and farming. It provides a centralized dashboard to control multiple accounts and game sessions simultaneously.",
  },
  {
    id: 2,
    question: "How many accounts can I manage?",
    answer:
      "The software is optimized to handle 10+ accounts simultaneously. The actual limit depends only on your hardware and your subscription plan.",
  },
  {
    id: 3,
    question: "Does the software need to stay open?",
    answer:
      "Yes, RedSoft must remain active in the background to maintain connection with Steam and continue the automation processes.",
  },
  {
    id: 4,
    question: "Is there a risk of a Steam ban?",
    answer:
      "We use advanced simulation algorithms that mimic real human behavior. While no third-party tool is 100% risk-free, RedSoft is designed to stay within safe operation limits.",
  },
  {
    id: 5,
    question: "Where are my login credentials stored?",
    answer:
      "All sensitive data is stored locally on your machine in an encrypted format. We do not have access to your passwords or Steam Guard files.",
  },
  {
    id: 6,
    question: "Does it support Steam Guard?",
    answer:
      "Yes, RedSoft fully supports Steam Guard, including mobile authenticators (SDA) for seamless and automated login.",
  },
  {
    id: 7,
    question: "What are the benefits of the Pro plan?",
    answer:
      'The Pro plan unlocks unlimited accounts, priority proxy support, advanced "Ghost Mode" features, and 24/7 technical assistance.',
  },
  {
    id: 8,
    question: "Can I run multiple games at once?",
    answer:
      "Absolutely. You can configure different games for each account or run the same game across your entire farm simultaneously.",
  },
  {
    id: 9,
    question: 'How does the "Advice" system work?',
    answer:
      "Our AI-driven engine analyzes your current farming progress and market trends to suggest the most profitable games and optimal timing for your sessions.",
  },
];

const activeId = ref(null);

const toggleFaq = (id) => {
  if (activeId.value === id) {
    activeId.value = null;
  } else {
    activeId.value = id;
  }
};
</script>

<template>
  <!-- УБРАН класс overflow-hidden, чтобы свет мог "вытекать" за пределы секции -->
  <section id="faq" class="flex flex-col items-center py-24 w-full my-20">
    <div class="relative w-full max-w-[1200px] flex flex-col items-center">
      <!-- Фоновые размытые пятна -->
      <div
        class="absolute w-[452px] h-[452px] -left-[240px] -top-[52px] bg-[linear-gradient(180deg,#1100CC_0%,#A50003_100%)] rounded-full blur-[210px] pointer-events-none z-0 mix-blend-screen"
      ></div>
      <div
        class="absolute w-[400px] h-[400px] left-[920px] top-[699px] bg-[linear-gradient(180deg,#A71613_0%,#2600FF_100%)] rounded-full blur-[210px] pointer-events-none z-0 mix-blend-screen"
      ></div>

      <!-- Заголовок и подзаголовок -->
      <div class="flex flex-col items-center gap-4 mb-16 z-10 w-full">
        <h2
          class="text-white text-[32px] font-bold font-['Montserrat'] leading-[39px] text-center"
        >
          Frequently Asked Questions
        </h2>
        <p
          class="text-[#D9D9D9] text-[20px] font-normal font-['Montserrat'] leading-[24px] text-center"
        >
          Here you can see frequently asked questions about our program.
        </p>
      </div>

      <!-- Список вопросов -->
      <div class="w-full max-w-[960px] flex flex-col gap-4 z-10 px-5 relative">
        <div v-for="faq in faqs" :key="faq.id" class="flex flex-col w-full">
          <button
            @click="toggleFaq(faq.id)"
            class="flex flex-row justify-between items-center p-6 w-full text-left transition-all duration-300"
            :class="[
              'border-2 border-[#434343] hover:border-white/50 group',
              activeId === faq.id
                ? 'rounded-t-[20px] rounded-b-none'
                : 'rounded-[20px]',
            ]"
          >
            <span
              class="text-white text-[20px] font-normal font-['Montserrat'] leading-[24px]"
            >
              {{ faq.question }}
            </span>
            <div class="flex-shrink-0 ml-4">
              <Minus v-if="activeId === faq.id" class="w-6 h-6 text-white" />
              <Plus
                v-else
                class="w-6 h-6 text-white group-hover:scale-110 transition-transform"
              />
            </div>
          </button>

          <transition name="accordion" @enter="onEnter" @leave="onLeave">
            <div
              v-show="activeId === faq.id"
              class="w-full px-6 py-6 border-b-2 border-x-2 border-[#434343] rounded-b-[20px] bg-transparent"
            >
              <p
                class="text-white text-[20px] font-normal font-['Montserrat'] leading-[24px]"
              >
                {{ faq.answer }}
              </p>
            </div>
          </transition>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.accordion-enter-active,
.accordion-leave-active {
  transition: all 0.3s ease-in-out;
  overflow: hidden;
}
.accordion-enter-from,
.accordion-leave-to {
  opacity: 0;
  max-height: 0;
  padding-top: 0;
  padding-bottom: 0;
  border-bottom-width: 0;
}
.accordion-enter-to,
.accordion-leave-from {
  opacity: 1;
  max-height: 300px;
}
</style>
