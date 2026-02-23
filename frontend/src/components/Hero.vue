<template>
  <div
    class="w-full min-h-screen bg-[#050208] flex justify-center font-['Montserrat']"
  >
    <div class="relative w-[1200px] h-[1072px] shrink-0">
      <div
        class="absolute w-[843px] h-[877px] right-[179px] bottom-0 bg-[linear-gradient(180deg,#4C001C_0%,#0B004C_22.12%,#1B00B2_100%)] blur-[600px] pointer-events-none z-0"
      ></div>

      <div
        class="absolute w-[500px] h-[387px] left-[calc(50%-250px)] top-[329px] bg-[linear-gradient(180deg,#FF001C_0%,#3B2E86_70.67%,#0E0B20_100%)] blur-[125px] pointer-events-none z-0"
      ></div>

      <div class="absolute top-[416px] left-0 w-[1200px] h-[656px] z-10">
        <div
          data-aos="fade-up-big"
          data-aos-duration="900"
          data-aos-easing="ease-out-cubic"
        >
          <div
            class="absolute w-[1112px] h-[598px] left-[calc(50%-556px)] top-[4px] bg-black border border-[#1F1E1E] shadow-[32px_0px_120px_rgba(121,91,255,0.25),0px_-32px_120px_rgba(121,91,255,0.25)] rounded-[36px]"
          ></div>

          <Main
            class="absolute w-[1080px] h-[608px] left-[calc(50%-540px)] top-[20px] bg-cover bg-no-repeat bg-center"
          ></Main>
        </div>
        <div
          class="absolute h-[541px] w-[100vw] left-1/2 -translate-x-1/2 bottom-0 bg-[linear-gradient(180deg,rgba(0,0,0,0)_3.8%,#050208_73.71%,#000000_86.04%)] pointer-events-none z-20"
        ></div>
      </div>

      <div
        data-aos="fade-down-big"
        data-aos-duration="900"
        data-aos-easing="ease-out-cubic"
        class="absolute top-0 left-0 w-[1200px] h-[384px] flex flex-col items-center pointer-events-none z-20"
      >
        <div
          class="relative flex flex-col items-center pt-[52px] gap-[20px] w-[1200px] h-[296px] pointer-events-auto"
        >
          <div class="flex flex-col items-center w-[1200px] h-[128px]">
            <h1
              class="w-[1200px] h-[63px] font-bold text-[52px] leading-[63px] text-center text-white m-0 uppercase"
            >
              YOUR STEAM
            </h1>
            <h2
              class="w-[1200px] h-[63px] font-bold text-[52px] leading-[63px] text-center bg-[radial-gradient(28.21%_121.43%_at_50%_-11.9%,#FFFFFF_0%,#7462C7_46.62%,#8A086A_100%)] bg-clip-text text-transparent m-0 uppercase"
            >
              YOUR RULES
            </h2>
          </div>

          <p
            class="w-[675px] h-[96px] font-medium text-[20px] leading-[24px] text-center text-white m-0"
          >
            REDSOFT is the ultimate tool for those who value their time and want
            to get the most out of their profile. Automate hour boosting, unlock
            any achievements, and manage your account collection in a single
            click.
          </p>

          <div
            class="flex flex-col items-start p-[4px] gap-[10px] w-[196px] h-[64px] rounded-[16px]"
          >
            <button
              class="relative flex flex-row items-center justify-center px-[40px] py-[16px] w-[188px] h-[56px] bg-[#8B0000] shadow-[0px_0px_7px_1px_#3E1112] rounded-[12px] hover:bg-[#a00000] transition-colors cursor-pointer z-50"
            >
              <span
                class="font-bold text-[20px] leading-[24px] text-center text-white"
              >
                Download
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Main from "../assets/Main.vue";
</script>
