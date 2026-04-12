<template>
  <section id="features">
    <div
      class="w-full bg-black flex justify-center overflow-x-hidden font-Montserrat"
    >
      <div data-aos="fade-down" class="relative w-[1200px] h-[891px] shrink-0">
        <div
          class="absolute w-[736px] h-[563px] left-[calc(50%-368px)] top-[96px] bg-[#560000] rounded-[50%] blur-[60px] pointer-events-none z-0"
        ></div>

        <Accounts
          class="absolute w-[600px] h-[338px] left-[80px] top-[241px] bg-[url('/Accounts.png')] bg-cover bg-no-repeat bg-center z-10"
        ></Accounts>
        <Game
          class="absolute w-[600px] h-[338px] left-[520px] top-[241px] bg-[url('/Game.png')] bg-cover bg-no-repeat bg-center z-10"
        ></Game>
        <h2
          class="absolute w-[1040px] h-[39px] left-[80px] top-[96px] font-bold text-[32px] leading-[39px] text-center text-white m-0 z-40"
        >
          Features
        </h2>

        <div class="absolute w-[1040px] h-[596px] left-[80px] top-[199px] z-20">
          <div
            class="absolute flex items-center justify-center w-[716px] h-[421px] left-[152px] top-0 bg-black rounded-[20px] z-30"
            style="
              box-shadow:
                -32px -20px 120px rgba(121, 91, 255, 0.32),
                32px 20px 120px rgba(121, 91, 255, 0.32);
            "
          >
            <MainPage
              class="w-[728px] h-[413px] bg-cover bg-no-repeat bg-center shrink-0 rounded-[12px]"
              style="
                filter: drop-shadow(32px 4px 120px rgba(0, 0, 0, 0.75))
                  drop-shadow(-32px 4px 120px rgba(0, 0, 0, 0.75));
              "
            />
          </div>
          <div
            class="absolute w-[1040px] h-[413px] left-0 top-[183px] pointer-events-none z-40"
            style="
              background: linear-gradient(
                0deg,
                #000000 0%,
                rgba(10, 10, 10, 0.899) 50.24%,
                rgba(0, 0, 0, 0) 100%
              );
            "
          ></div>
          <div
            class="absolute bg-black flex flex-col items-start px-[32px] gap-[16px] w-[1040px] h-[175px] left-0 top-[421px] z-50"
          >
            <h3
              class="w-[976px] h-[39px] font-semibold text-[32px] leading-[39px] text-white m-0"
            >
              Main page
            </h3>
            <p
              class="w-[976px] h-[120px] font-normal text-[20px] leading-[24px] text-[#F5F5F5] m-0"
            >
              The main page is an interactive dashboard for complete control
              over gaming processes and accounts. It centralizes the monitoring
              of launched games, personal user statistics, and the latest system
              news in a single workspace. Featuring a built-in advice block and
              a status bar with region and software version data, the dashboard
              provides instant access to all automation and security tools in
              real time.
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import Game from "../assets/Game.vue";
import Accounts from "../assets/Accounts.vue";
import MainPage from "../assets/MainPage.vue";
</script>
