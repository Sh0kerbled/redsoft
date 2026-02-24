<template>
  <section id="faq">
    <div
      class="w-full flex justify-center relative font-['Montserrat'] bg-transparent"
    >
      <div class="relative w-[1200px] h-[1047px] shrink-0">
        <div
          class="absolute w-[452px] h-[452px] -left-[240px] -top-[52px] bg-[linear-gradient(180deg,#1100CC_0%,#A50003_100%)] rounded-full blur-[210px] pointer-events-none z-0 mix-blend-screen"
        ></div>
        <div
          class="absolute w-[400px] h-[400px] left-[920px] top-[699px] bg-[linear-gradient(180deg,#A71613_0%,#2600FF_100%)] rounded-full blur-[210px] pointer-events-none z-0 mix-blend-screen"
        ></div>
        <div
          data-aos="fade-down"
          class="absolute flex flex-col items-center gap-[16px] w-[649px] h-[79px] left-[275.5px] top-[96px] z-10"
        >
          <h2
            class="w-full h-[39px] font-bold text-[32px] leading-[39px] text-center text-white m-0"
          >
            Frequently Asked Questions
          </h2>
          <p
            class="w-full h-[24px] font-normal text-[20px] leading-[24px] text-center text-[#D9D9D9] m-0"
          >
            Here you can see frequently asked questions about our program.
          </p>
        </div>
        <div
          data-aos="fade-up"
          v-for="(item, index) in faqItems"
          :key="index"
          class="absolute box-border flex flex-row justify-between items-center px-[24px] py-[24px] w-[960px] h-[72px] left-[120px] border-[2px] border-[#434343] rounded-[20px] z-10 cursor-pointer hover:bg-white/5 transition-colors bg-[#050208]/50 backdrop-blur-sm"
          :style="{ top: `${239 + index * 80}px` }"
        >
          <span class="font-normal text-[20px] leading-[24px] text-white">
            {{ item }}
          </span>

          <div class="relative w-[24px] h-[24px] shrink-0">
            <div
              class="absolute left-1/2 top-1/4 bottom-1/4 w-[2px] -translate-x-1/2 bg-white rounded-full"
            ></div>
            <div
              class="absolute top-1/2 left-1/4 right-1/4 h-[2px] -translate-y-1/2 bg-white rounded-full"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const faqItems = [
  "What is RedSoft?",
  "How many accounts can I manage?",
  "Does the software need to stay open?",
  "Is there a risk of a Steam ban?",
  "Where are my login credentials stored?",
  "Does it support Steam Guard?",
  "What are the benefits of the Pro plan?",
  "Can I run multiple games at once?",
  'How does the "Advice" system work?',
];
</script>
