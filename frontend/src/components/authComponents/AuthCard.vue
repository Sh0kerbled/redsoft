<template>
  <div
    class="min-h-screen w-full bg-black flex items-center justify-center font-['Montserrat']"
  >
    <div
      class="relative w-[1040px] h-[682px] bg-black shadow-[0_0_12px_rgba(255,255,255,0.5)] rounded-[40px] overflow-hidden"
    >
      <!-- ─── Sign In Form (Static) ─── -->
      <div
        class="absolute top-0 left-0 w-[559px] h-full flex flex-col items-center justify-center z-10 transition-all duration-700 ease-in-out"
        :class="
          isSignUpActive
            ? 'translate-x-[481px] opacity-0 pointer-events-none'
            : 'translate-x-0 opacity-100'
        "
      >
        <div class="flex flex-col items-center gap-[52px] w-[479px]">
          <h1
            class="font-bold text-[40px] leading-[49px] text-center text-white m-0"
          >
            Sign In
          </h1>
          <div class="flex flex-col items-center gap-[20px] w-full">
            <p class="font-normal text-[20px] text-center text-white m-0">
              Use your E-mail and Password
            </p>
            <div class="flex flex-col gap-[32px] w-full">
              <div class="flex flex-col gap-[12px] w-full">
                <div
                  class="flex items-center p-[24px] h-[72px] bg-[#1F1E1E] rounded-[20px]"
                >
                  <input
                    type="email"
                    placeholder="E-mail"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <div
                  class="flex items-center p-[24px] h-[72px] bg-[#1F1E1E] rounded-[20px]"
                >
                  <input
                    type="password"
                    placeholder="Password"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <a
                  href="#"
                  class="font-normal text-[20px] leading-[24px] text-white hover:underline"
                >
                  Forgot your password?
                </a>
              </div>
              <button
                class="flex items-center justify-center w-[199px] h-[56px] bg-[#8B0000] shadow-[0_0_7px_1px_#3E1112] rounded-[12px] hover:bg-[#a00000] transition-colors mx-auto cursor-pointer"
              >
                <span class="font-semibold text-[20px] text-white"
                  >Sign in</span
                >
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- ─── Sign Up Form (Static) ─── -->
      <div
        class="absolute top-0 left-0 w-[559px] h-full flex flex-col items-center justify-center z-10 transition-all duration-700 ease-in-out"
        :class="
          isSignUpActive
            ? 'translate-x-[481px] opacity-100 pointer-events-auto'
            : 'translate-x-0 opacity-0 pointer-events-none'
        "
      >
        <div class="flex flex-col items-center gap-[40px] w-[479px]">
          <h1
            class="font-bold text-[40px] leading-[49px] text-center text-white m-0"
          >
            Create Account
          </h1>
          <div class="flex flex-col items-center gap-[20px] w-full">
            <p class="font-normal text-[20px] text-center text-white m-0">
              Use your E-mail for registration
            </p>
            <div class="flex flex-col gap-[32px] w-full">
              <div class="flex flex-col gap-[12px] w-full">
                <div
                  class="flex items-center p-[24px] h-[72px] bg-[#1F1E1E] rounded-[20px]"
                >
                  <input
                    type="text"
                    placeholder="Name"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <div
                  class="flex items-center p-[24px] h-[72px] bg-[#1F1E1E] rounded-[20px]"
                >
                  <input
                    type="email"
                    placeholder="E-mail"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <div
                  class="flex items-center p-[24px] h-[72px] bg-[#1F1E1E] rounded-[20px]"
                >
                  <input
                    type="password"
                    placeholder="Password"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
              </div>
              <button
                class="flex items-center justify-center w-[199px] h-[56px] bg-[#1000BF] shadow-[0_0_7px_1px_#3E1112] rounded-[12px] hover:bg-[#1003A0] transition-colors mx-auto cursor-pointer"
              >
                <span class="font-semibold text-[20px] text-white"
                  >Sign Up</span
                >
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- ─── Sliding Gradient Overlay ─── -->
      <div
        class="absolute top-0 w-[481px] h-full z-20 flex items-center justify-center overflow-hidden transition-all duration-700 ease-in-out"
        :class="
          isSignUpActive
            ? 'translate-x-0 rounded-[40px_164px_164px_40px]'
            : 'translate-x-[559px] rounded-[164px_40px_40px_164px]'
        "
      >
        <!-- Слой 1: Красный градиент (исчезает при переключении) -->
        <div
          class="absolute inset-0 w-full h-full bg-[linear-gradient(90deg,#A33839_0%,#5B0002_100%)] transition-opacity duration-700 ease-in-out"
          :class="isSignUpActive ? 'opacity-0' : 'opacity-100'"
        ></div>

        <!-- Слой 2: Синий градиент (появляется при переключении) -->
        <div
          class="absolute inset-0 w-full h-full bg-[linear-gradient(90deg,#0B005B_0%,#383BA3_100%)] transition-opacity duration-700 ease-in-out"
          :class="isSignUpActive ? 'opacity-100' : 'opacity-0'"
        ></div>

        <!-- Контент внутри оверлея (должен быть выше фонов, поэтому relative z-10) -->
        <div class="relative z-10 w-full h-full">
          <!-- Hello, Friend! -->
          <div
            class="absolute w-full top-[calc(50%-123.5px)] flex flex-col items-center gap-[40px] transition-all duration-700 ease-in-out"
            :class="
              isSignUpActive
                ? 'opacity-0 -translate-x-full pointer-events-none'
                : 'opacity-100 translate-x-0'
            "
          >
            <h2
              class="font-bold text-[32px] leading-[39px] text-center text-white m-0"
            >
              Hello, Friend!
            </h2>
            <p
              class="w-[339px] font-normal text-[20px] leading-[24px] text-center text-[#E9E9E9] m-0"
            >
              Create an account to unlock all features and start managing your
              Steam assets today
            </p>
            <button
              @click="togglePanel"
              class="flex items-center justify-center w-[183px] h-[56px] bg-white rounded-[12px] hover:bg-gray-200 transition-colors cursor-pointer"
            >
              <span class="font-semibold text-[20px] text-black">Sign up</span>
            </button>
          </div>

          <!-- Welcome Back! -->
          <div
            class="absolute w-full top-[calc(50%-123.5px)] flex flex-col items-center gap-[40px] transition-all duration-700 ease-in-out"
            :class="
              isSignUpActive
                ? 'opacity-100 translate-x-0'
                : 'opacity-0 translate-x-full pointer-events-none'
            "
          >
            <h2
              class="font-bold text-[32px] leading-[39px] text-center text-white m-0"
            >
              Welcome Back!
            </h2>
            <p
              class="w-[339px] font-normal text-[20px] leading-[24px] text-center text-[#E9E9E9] m-0"
            >
              Enter your personal details to use all of site features
            </p>
            <button
              @click="togglePanel"
              class="flex items-center justify-center w-[183px] h-[56px] bg-white hover:bg-gray-200 rounded-[12px] transition-colors cursor-pointer"
            >
              <span class="font-semibold text-[20px] text-black">Sign In</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const isSignUpActive = ref(false);

const togglePanel = () => {
  isSignUpActive.value = !isSignUpActive.value;
};
</script>
