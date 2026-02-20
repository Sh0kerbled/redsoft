<template>
  <section class="container mx-auto px-6 py-24 max-w-3xl">
    <div class="text-center mb-12">
      <h2 class="text-3xl font-bold mb-4">Frequently Asked Questions</h2>
      <p class="text-gray-400 text-sm">
        Here you can see frequently asked questions about our program.
      </p>
    </div>

    <div class="space-y-3">
      <details
        v-for="(item, index) in faqs"
        :key="index"
        class="group bg-[#0e0716] border border-gray-800 rounded-lg cursor-pointer open:bg-[#150a21] transition-colors"
      >
        <summary
          class="flex items-center justify-between p-5 font-medium list-none text-sm md:text-base"
        >
          {{ item.question }}
          <span class="transition group-open:rotate-45 text-gray-500">
            <svg
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M12 6v6m0 0v6m0-6h6m-6 0H6"
              ></path>
            </svg>
          </span>
        </summary>
        <div class="px-5 pb-5 text-gray-400 text-sm leading-relaxed">
          {{ item.answer }}
        </div>
      </details>
    </div>
  </section>
</template>

<script setup>
const faqs = [
  {
    question: "What is RedSoft?",
    answer:
      "RedSoft is an automation tool designed to help you manage your Steam accounts, track progress, and unlock achievements efficiently.",
  },
  {
    question: "How many accounts can I manage?",
    answer:
      "The number of accounts depends on your pricing plan. Basic allows 2 accounts, Pro allows 5, and Ultimate supports up to 50 accounts.",
  },
  {
    question: "Does the software need a proxy soon?",
    answer:
      "Depending on your usage volume, proxies might be recommended to ensure optimal performance and security. See our documentation for details.",
  },
  {
    question: "Is there a risk of a Steam ban?",
    answer:
      "We use advanced stealth modes and secure hashing algorithms to minimize any risks, making it extremely safe compared to alternative methods.",
  },
  {
    question: "Where can I log in to download our client?",
    answer:
      "You can download the client directly from your user dashboard after logging into your account on our website.",
  },
  {
    question: "Does it support Steam Guard?",
    answer:
      "Yes, full support for Steam Guard (both email and mobile authenticator) is integrated into the client.",
  },
  {
    question: "What are the hardware running the app?",
    answer:
      "Our app is lightweight and optimized. It can run on any modern Windows OS with minimal CPU and RAM footprint.",
  },
  {
    question: "Can it run multiple games at once?",
    answer:
      "Yes, our Pro and Ultimate plans support simultaneous sessions and running multiple games across different accounts.",
  },
  {
    question: 'How does the "Advice" system work?',
    answer:
      "The system analyzes your gaming library and provides actionable insights on which games to boost to maximize your profile value.",
  },
];
</script>
