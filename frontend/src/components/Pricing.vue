<template>
  <section id="pricing">
    <div
      class="w-full flex justify-center relative font-['Montserrat'] bg-transparent"
    >
      <div class="relative w-[1200px] h-[886px] shrink-0">
        <div class="absolute inset-0 pointer-events-none z-0">
          <div
            class="absolute w-[320px] h-[320px] left-[calc(50%-160px-360px)] top-[271px] bg-[linear-gradient(180deg,#770000_30.28%,#0E0042_100%)] rounded-full blur-[120px] mix-blend-screen"
          ></div>

          <div
            class="absolute w-[320px] h-[320px] left-[calc(50%-160px)] top-[470px] bg-[linear-gradient(180deg,#770000_30.28%,#0E0042_100%)] rounded-full blur-[120px] mix-blend-screen"
          ></div>

          <div
            class="absolute w-[320px] h-[320px] left-[calc(50%-160px+360px)] top-[271px] bg-[linear-gradient(180deg,#770000_30.28%,#0E0042_100%)] rounded-full blur-[120px] mix-blend-screen"
          ></div>
        </div>

        <div
          data-aos="fade-down"
          class="absolute flex flex-col items-center gap-[24px] w-[1040px] h-[111px] left-[80px] top-[96px] z-10"
        >
          <h2
            class="w-full h-[39px] font-bold text-[32px] leading-[39px] text-center text-white m-0"
          >
            Pricing
          </h2>
          <p
            class="w-[546px] h-[48px] font-normal text-[20px] leading-[24px] text-center text-[#D9D9D9] m-0"
          >
            Choose the perfect plan to automate your Steam routine and start
            boosting your accounts today.
          </p>
        </div>

        <div
          data-aos="fade-right"
          class="absolute flex flex-col items-start p-[28px_28px_32px] gap-[40px] w-[320px] h-[519px] left-[80px] top-[271px] bg-[linear-gradient(180deg,rgba(139,0,0,0.32)_10%,rgba(255,255,255,0.0032)_100%)] rounded-[20px] isolate z-10 overflow-hidden"
        >
          <div
            class="absolute inset-0 opacity-50 z-0 mix-blend-overlay pointer-events-none flex items-center justify-center text-white"
          >
            <Pattern2 class="w-full h-full object-cover" />
          </div>

          <div
            class="relative flex flex-col items-start gap-[12px] w-[90px] h-[75px] z-10"
          >
            <h3
              class="w-[90px] h-[39px] font-bold text-[32px] leading-[39px] text-center text-white m-0"
            >
              Basic
            </h3>
            <span
              class="w-[45px] h-[24px] font-normal text-[20px] leading-[24px] text-center text-[#D9D9D9]"
            >
              Free
            </span>
          </div>

          <div class="relative flex flex-col items-start gap-[8px] w-full z-10">
            <div
              v-for="(feature, idx) in basicFeatures"
              :key="idx"
              class="flex flex-row items-center gap-[8px] h-[24px]"
            >
              <div
                class="relative w-[24px] h-[24px] flex items-center justify-center shrink-0"
              >
                <div
                  class="w-[12.72px] h-[8.48px] border-l-[2px] border-b-[2px] border-white -rotate-45 -translate-y-[2px]"
                ></div>
              </div>
              <span
                class="font-['Inter'] font-light text-[20px] leading-[24px] flex items-center text-center text-white m-0"
              >
                {{ feature }}
              </span>
            </div>
          </div>

          <button
            class="absolute flex flex-row justify-center items-center px-[52px] py-[12px] w-[186px] h-[48px] left-[calc(50%-93px)] bottom-[32px] bg-[#8B0000] shadow-[0px_0px_7px_1px_#3E1112] rounded-[12px] z-10 hover:bg-[#a00000] transition-colors"
          >
            <span
              class="font-normal text-[20px] leading-[24px] text-center text-white"
              >Activate</span
            >
          </button>
        </div>

        <div
          data-aos="fade-up"
          class="absolute flex flex-col items-center p-[28px_28px_32px] gap-[80px] w-[320px] h-[519px] left-[440px] top-[271px] bg-[linear-gradient(180deg,rgba(255,255,255,0.0032)_0%,rgba(139,0,0,0.32)_90.03%)] rounded-[20px] isolate z-10 overflow-hidden"
        >
          <div
            class="absolute inset-0 opacity-50 z-0 mix-blend-overlay pointer-events-none flex items-center justify-center text-white"
          >
            <Pattern2 class="w-full h-full object-cover" />
          </div>

          <div
            class="relative flex flex-col items-start gap-[40px] w-[264px] z-10"
          >
            <div
              class="flex flex-col items-start gap-[12px] w-[104px] h-[75px]"
            >
              <h3
                class="w-[104px] h-[39px] font-bold text-[32px] leading-[39px] text-white m-0"
              >
                Pro
              </h3>
              <span
                class="w-[104px] h-[24px] font-normal text-[20px] leading-[24px] text-center text-[#D9D9D9]"
              >
                $9.99 / mo
              </span>
            </div>

            <div class="flex flex-col items-start gap-[8px] w-full">
              <div
                v-for="(feature, idx) in proFeatures"
                :key="idx"
                class="flex flex-row items-center gap-[8px] h-[24px]"
              >
                <div
                  class="relative w-[24px] h-[24px] flex items-center justify-center shrink-0"
                >
                  <div
                    class="w-[12.72px] h-[8.48px] border-l-[2px] border-b-[2px] border-white -rotate-45 -translate-y-[2px]"
                  ></div>
                </div>
                <span
                  class="font-['Inter'] font-light text-[20px] leading-[24px] flex items-center text-center text-white m-0"
                >
                  {{ feature }}
                </span>
              </div>
            </div>
          </div>

          <button
            class="absolute flex flex-row justify-center items-center px-[52px] py-[12px] w-[186px] h-[48px] left-[calc(50%-93px)] bottom-[32px] bg-[#8B0000] shadow-[0px_0px_7px_1px_#3E1112] rounded-[12px] z-10 hover:bg-[#a00000] transition-colors"
          >
            <span
              class="font-normal text-[20px] leading-[24px] text-center text-white"
              >Activate</span
            >
          </button>
        </div>

        <div
          data-aos="fade-left"
          class="absolute flex flex-col justify-end items-center p-[28px_28px_32px] gap-[80px] w-[320px] h-[519px] left-[800px] top-[271px] bg-[linear-gradient(180deg,rgba(139,0,0,0.32)_10%,rgba(255,255,255,0.0032)_100%)] rounded-[20px] isolate z-10 overflow-hidden"
        >
          <div
            class="absolute inset-0 opacity-50 z-0 mix-blend-overlay pointer-events-none flex items-center justify-center text-white"
          >
            <Pattern2 class="w-full h-full object-cover" />
          </div>

          <div
            class="absolute top-[28px] left-[28px] flex flex-col items-start gap-[40px] w-[264px] z-10"
          >
            <div
              class="flex flex-col items-start gap-[12px] w-[147px] h-[75px]"
            >
              <h3
                class="w-[147px] h-[39px] font-bold text-[32px] leading-[39px] text-center text-white m-0"
              >
                Ultimate
              </h3>
              <span
                class="w-[147px] h-[24px] font-normal text-[20px] leading-[24px] text-[#D9D9D9]"
              >
                $19.99 / mo
              </span>
            </div>

            <div class="flex flex-col items-start gap-[8px] w-full">
              <div
                v-for="(feature, idx) in ultimateFeatures"
                :key="idx"
                class="flex flex-row items-center gap-[8px] h-[24px]"
              >
                <div
                  class="relative w-[24px] h-[24px] flex items-center justify-center shrink-0"
                >
                  <div
                    class="w-[12.72px] h-[8.48px] border-l-[2px] border-b-[2px] border-white -rotate-45 -translate-y-[2px]"
                  ></div>
                </div>
                <span
                  class="font-['Inter'] font-light text-[20px] leading-[24px] flex items-center text-center text-white m-0"
                >
                  {{ feature }}
                </span>
              </div>
            </div>
          </div>

          <button
            class="relative flex flex-row justify-center items-center px-[52px] py-[12px] w-[186px] h-[48px] bg-[#8B0000] shadow-[0px_0px_7px_1px_#3E1112] rounded-[12px] z-10 hover:bg-[#a00000] transition-colors"
          >
            <span
              class="font-normal text-[20px] leading-[24px] text-center text-white"
              >Activate</span
            >
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Pattern2 from "../assets/Pattern2.vue";

const basicFeatures = ["2 Steam account", "Single session", "Basic monitoring"];

const proFeatures = [
  "5 Steam Accounts",
  "3 Simultaneous Sessions",
  "Priority Boosting",
  "Full Analytics",
  "Interactive Advice",
  "Early Updates",
];

const ultimateFeatures = [
  "10 Steam Accounts",
  "Unlimited Sessions",
  "High-Load Optimization",
  "Live System Diagnostics",
  "Anti-Cheat Stealth Mode",
  "Bulk Management",
  "Priority Support",
];
</script>
