<template>
  <div
    class="w-full bg-[#050208] flex justify-center overflow-y-clip font-['Montserrat']"
  >
    <div class="relative w-[1200px] h-[715px] shrink-0">
      <div
        class="absolute w-[1200px] h-[611px] left-0 top-[52px] bg-[linear-gradient(270deg,#190000_0.81%,#000000_100%)] rounded-[20px] overflow-hidden"
      >
        <div
          class="absolute w-full h-full left-0 top-0 z-0 pointer-events-none text-white"
        >
          <Pattern class="w-full h-full" />
        </div>
        <div class="relative w-full h-full overflow-hidden">
          <div
            data-aos="fade-down-right"
            class="relative z-10 flex flex-col justify-center items-start gap-[52px] w-[631px] h-[523px] left-[80px] top-[44px] animate__animated animate__fadeInTopLeft"
          >
            <h2 class="font-bold text-[28px] leading-[34px] text-white m-0">
              About Us
            </h2>

            <div class="flex flex-col items-start gap-[32px] w-full">
              <div class="flex flex-col items-start gap-[16px] w-full">
                <h3
                  class="font-semibold text-[24px] leading-[32px] text-white m-0"
                >
                  Automate your progress and maximize your benefits!
                </h3>
                <p
                  class="font-normal text-[20px] leading-[28px] text-[#F5F5F5] m-0"
                >
                  Our product offers powerful functionality for centralized
                  automation of your accounts. Enjoy convenient in-game time
                  (hours) boosting, automatic achievement unlocking, and
                  simulation of real user activity. Thanks to RedSoft, you gain
                  a significant advantage in efficiently utilizing your profile!
                </p>
              </div>

              <div class="flex flex-col items-start gap-[16px] w-full">
                <h3
                  class="font-semibold text-[24px] leading-[29px] text-white m-0"
                >
                  Why Choose Us?
                </h3>
                <p
                  class="font-normal text-[20px] leading-[28px] text-[#F5F5F5] m-0"
                >
                  The REDSOFT project is developed by a team with years of
                  experience in automating gaming services. We have been
                  operating since 2016, providing reliable and secure solutions.
                  We ensure you won't have to doubt the quality and
                  confidentiality of the software you use!
                </p>
              </div>
            </div>
          </div>
        </div>
        <BigLogo
          data-aos="fade-down-left"
          data-aos-duration="900"
          data-aos-easing="ease-out-cubic"
          class="absolute w-[285px] h-[285px] left-[835px] top-[163px] z-10 wow animate__animated animate__fadeInTopRight"
        />
      </div>

      <div
        class="absolute h-[108px] w-[100dvw] left-1/2 -translate-x-1/2 top-0 bg-[linear-gradient(0deg,rgba(0,0,0,0)_3.8%,#000000_73.79%)] pointer-events-none z-20"
      ></div>

      <div
        class="absolute h-[108px] w-[100dvw] left-1/2 -translate-x-1/2 bottom-0 bg-[linear-gradient(180deg,rgba(0,0,0,0)_3.8%,#000000_73.79%)] pointer-events-none z-20"
      ></div>
    </div>
  </div>
</template>

<script setup>
import BigLogo from "../assets/BigLogo.vue";
import Pattern from "../assets/Pattern.vue";
</script>
