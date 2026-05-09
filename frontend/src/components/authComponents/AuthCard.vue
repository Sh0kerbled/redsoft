<template>
  <div class="w-full my-10 bg-black flex flex-col items-center justify-center">
    <div
      class="relative w-[1040px] h-[682px] bg-black shadow-[0_0_12px_rgba(255,255,255,0.5)] rounded-[40px] overflow-hidden"
    >
      <NikolayCircles />
      <NikolayCirclesBlue class="absolute left-[890px] top-[532px]" />

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
              <form
                @submit.prevent="submitLogin"
                class="flex flex-col gap-[12px] w-full"
              >
                <div
                  class="flex items-center px-[24px] h-[72px] rounded-[20px] transition-colors"
                  :class="
                    loginErrors.email
                      ? 'bg-[#3a1a1a] border border-red-500'
                      : 'bg-[#1F1E1E]'
                  "
                >
                  <input
                    v-model="loginData.email"
                    type="email"
                    placeholder="E-mail"
                    @input="loginErrors.email = ''"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <p
                  v-if="loginErrors.email"
                  class="text-red-400 text-[14px] -mt-2 ml-2"
                >
                  {{ loginErrors.email }}
                </p>

                <div
                  class="flex items-center px-[24px] h-[72px] rounded-[20px] transition-colors"
                  :class="
                    loginErrors.password
                      ? 'bg-[#3a1a1a] border border-red-500'
                      : 'bg-[#1F1E1E]'
                  "
                >
                  <input
                    v-model="loginData.password"
                    :type="showLoginPassword ? 'text' : 'password'"
                    placeholder="Password"
                    @input="loginErrors.password = ''"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                  <button
                    type="button"
                    @click="showLoginPassword = !showLoginPassword"
                    class="text-white/50 hover:text-white transition-colors ml-2"
                  >
                    <svg
                      v-if="showLoginPassword"
                      xmlns="http://www.w3.org/2000/svg"
                      class="w-5 h-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 4.411m0 0L21 21"
                      />
                    </svg>
                    <svg
                      v-else
                      xmlns="http://www.w3.org/2000/svg"
                      class="w-5 h-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                      />
                    </svg>
                  </button>
                </div>
                <p
                  v-if="loginErrors.password"
                  class="text-red-400 text-[14px] -mt-2 ml-2"
                >
                  {{ loginErrors.password }}
                </p>

                <a
                  href="#"
                  class="font-normal text-[20px] leading-[24px] text-white hover:underline flex justify-center"
                >
                  Forgot your password?
                </a>

                <transition name="fade">
                  <p
                    v-if="loginError"
                    class="text-red-400 text-[15px] text-center"
                  >
                    {{ loginError }}
                  </p>
                  <p
                    v-else-if="loginSuccess"
                    class="text-green-400 text-[15px] text-center"
                  >
                    {{ loginSuccess }}
                  </p>
                </transition>

                <button
                  type="submit"
                  :disabled="isLoginLoading"
                  class="flex items-center justify-center gap-2 w-[199px] h-[56px] bg-[#8B0000] shadow-[0_0_7px_1px_#3E1112] rounded-[12px] hover:bg-[#a00000] transition-colors mx-auto disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <svg
                    v-if="isLoginLoading"
                    class="animate-spin w-5 h-5 text-white"
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                  >
                    <circle
                      class="opacity-25"
                      cx="12"
                      cy="12"
                      r="10"
                      stroke="currentColor"
                      stroke-width="4"
                    />
                    <path
                      class="opacity-75"
                      fill="currentColor"
                      d="M4 12a8 8 0 018-8v8H4z"
                    />
                  </svg>
                  <span class="font-semibold text-[20px] text-white">
                    {{ isLoginLoading ? "Signing in..." : "Sign in" }}
                  </span>
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>

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
            <form
              @submit.prevent="submitForm"
              class="flex flex-col gap-[32px] w-full"
            >
              <div class="flex flex-col gap-[12px] w-full">
                <div
                  class="flex items-center px-[24px] h-[72px] rounded-[20px] transition-colors"
                  :class="
                    registerErrors.username
                      ? 'bg-[#3a1a1a] border border-red-500'
                      : 'bg-[#1F1E1E]'
                  "
                >
                  <input
                    v-model="formData.username"
                    type="text"
                    placeholder="Name"
                    @input="registerErrors.username = ''"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <p
                  v-if="registerErrors.username"
                  class="text-red-400 text-[14px] -mt-2 ml-2"
                >
                  {{ registerErrors.username }}
                </p>

                <div
                  class="flex items-center px-[24px] h-[72px] rounded-[20px] transition-colors"
                  :class="
                    registerErrors.email
                      ? 'bg-[#3a1a1a] border border-red-500'
                      : 'bg-[#1F1E1E]'
                  "
                >
                  <input
                    v-model="formData.email"
                    type="email"
                    placeholder="E-mail"
                    @input="registerErrors.email = ''"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                </div>
                <p
                  v-if="registerErrors.email"
                  class="text-red-400 text-[14px] -mt-2 ml-2"
                >
                  {{ registerErrors.email }}
                </p>

                <div
                  class="flex items-center px-[24px] h-[72px] rounded-[20px] transition-colors"
                  :class="
                    registerErrors.password
                      ? 'bg-[#3a1a1a] border border-red-500'
                      : 'bg-[#1F1E1E]'
                  "
                >
                  <input
                    v-model="formData.password"
                    :type="showRegisterPassword ? 'text' : 'password'"
                    placeholder="Password"
                    @input="registerErrors.password = ''"
                    class="flex-grow bg-transparent font-normal text-[20px] text-white outline-none placeholder-white/50"
                  />
                  <button
                    type="button"
                    @click="showRegisterPassword = !showRegisterPassword"
                    class="text-white/50 hover:text-white transition-colors ml-2"
                  >
                    <svg
                      v-if="showRegisterPassword"
                      xmlns="http://www.w3.org/2000/svg"
                      class="w-5 h-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 4.411m0 0L21 21"
                      />
                    </svg>
                    <svg
                      v-else
                      xmlns="http://www.w3.org/2000/svg"
                      class="w-5 h-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                      />
                    </svg>
                  </button>
                </div>
                <p
                  v-if="registerErrors.password"
                  class="text-red-400 text-[14px] -mt-2 ml-2"
                >
                  {{ registerErrors.password }}
                </p>

                <div v-if="formData.password" class="flex gap-1 px-1">
                  <div
                    v-for="i in 4"
                    :key="i"
                    class="h-1 flex-1 rounded-full transition-all duration-300"
                    :class="
                      passwordStrength >= i
                        ? passwordStrengthColor
                        : 'bg-[#434343]'
                    "
                  ></div>
                </div>
                <p
                  v-if="formData.password"
                  class="text-[13px] ml-1 -mt-2"
                  :class="passwordStrengthTextColor"
                >
                  {{ passwordStrengthLabel }}
                </p>
              </div>

              <transition name="fade">
                <p
                  v-if="registerError"
                  class="text-red-400 text-[15px] text-center -my-4"
                >
                  {{ registerError }}
                </p>
                <p
                  v-else-if="registerSuccess"
                  class="text-green-400 text-[15px] text-center -my-4"
                >
                  {{ registerSuccess }}
                </p>
              </transition>

              <button
                type="submit"
                :disabled="isRegisterLoading"
                class="flex items-center justify-center gap-2 w-[199px] h-[56px] bg-[#1000BF] shadow-[0_0_7px_1px_#3E1112] rounded-[12px] hover:bg-[#1003A0] transition-colors mx-auto disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <svg
                  v-if="isRegisterLoading"
                  class="animate-spin w-5 h-5 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    class="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    stroke-width="4"
                  />
                  <path
                    class="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v8H4z"
                  />
                </svg>
                <span class="font-semibold text-[20px] text-white">
                  {{ isRegisterLoading ? "Creating..." : "Sign Up" }}
                </span>
              </button>
            </form>
          </div>
        </div>
      </div>

      <div
        class="absolute top-0 w-[481px] h-full z-20 flex items-center justify-center overflow-hidden transition-all duration-700 ease-in-out"
        :class="
          isSignUpActive
            ? 'translate-x-0 rounded-[40px_164px_164px_40px]'
            : 'translate-x-[559px] rounded-[164px_40px_40px_164px]'
        "
      >
        <div
          class="absolute inset-0 w-full h-full bg-[linear-gradient(90deg,#A33839_0%,#5B0002_100%)] transition-opacity duration-700 ease-in-out"
          :class="isSignUpActive ? 'opacity-0' : 'opacity-100'"
        ></div>
        <div
          class="absolute inset-0 w-full h-full bg-[linear-gradient(90deg,#0B005B_0%,#383BA3_100%)] transition-opacity duration-700 ease-in-out"
          :class="isSignUpActive ? 'opacity-100' : 'opacity-0'"
        ></div>

        <div class="relative z-10 w-full h-full">
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

          <!-- Welcome Back -->
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
import { ref, computed } from "vue";
import { useRouter } from "vue-router";
import NikolayCircles from "../../assets/NikolayCircles.vue";
import NikolayCirclesBlue from "../../assets/NikolayCirclesBlue.vue";

const router = useRouter();

const isSignUpActive = ref(false);
const togglePanel = () => {
  isSignUpActive.value = !isSignUpActive.value;
  loginError.value = "";
  loginSuccess.value = "";
  registerError.value = "";
  registerSuccess.value = "";
  loginErrors.value = { email: "", password: "" };
  registerErrors.value = { username: "", email: "", password: "" };
};

const showLoginPassword = ref(false);
const showRegisterPassword = ref(false);

const loginData = ref({ email: "", password: "" });
const loginErrors = ref({ email: "", password: "" });
const loginError = ref("");
const loginSuccess = ref("");
const isLoginLoading = ref(false);

const validateEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

const submitLogin = async () => {
  loginError.value = "";
  loginSuccess.value = "";
  loginErrors.value = { email: "", password: "" };

  let hasError = false;
  if (!validateEmail(loginData.value.email)) {
    loginErrors.value.email = "Enter a valid email address";
    hasError = true;
  }
  if (!loginData.value.password) {
    loginErrors.value.password = "Password is required";
    hasError = true;
  }
  if (hasError) return;

  isLoginLoading.value = true;
  try {
    const response = await fetch("http://127.0.0.1:8000/accounts/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(loginData.value),
    });
    const data = await response.json();

    if (response.ok) {
      const savedUsername = data.user?.username || loginData.value.email;
      localStorage.setItem("username", savedUsername);

      localStorage.setItem("access", data.access);
      localStorage.setItem("refresh", data.refresh);

      window.dispatchEvent(new Event("storage"));

      loginSuccess.value = "Welcome back! Redirecting...";
      loginData.value = { email: "", password: "" };
      setTimeout(() => router.push("/"), 800);
    } else {
      loginError.value =
        data.error || data.detail || "Invalid email or password";
    }
  } catch {
    loginError.value = "Network error. Please check your connection.";
  } finally {
    isLoginLoading.value = false;
  }
};

// ─── SIGN UP ───────────────────────────────────────────
const formData = ref({ username: "", email: "", password: "" });
const registerErrors = ref({ username: "", email: "", password: "" });
const registerError = ref("");
const registerSuccess = ref("");
const isRegisterLoading = ref(false);

// Индикатор силы пароля
const passwordStrength = computed(() => {
  const p = formData.value.password;
  if (!p) return 0;
  let score = 0;
  if (p.length >= 8) score++;
  if (/[A-Z]/.test(p)) score++;
  if (/[0-9]/.test(p)) score++;
  if (/[^A-Za-z0-9]/.test(p)) score++;
  return score;
});

const passwordStrengthColor = computed(() => {
  if (passwordStrength.value <= 1) return "bg-red-500";
  if (passwordStrength.value === 2) return "bg-orange-400";
  if (passwordStrength.value === 3) return "bg-yellow-400";
  return "bg-green-500";
});

const passwordStrengthTextColor = computed(() => {
  if (passwordStrength.value <= 1) return "text-red-400";
  if (passwordStrength.value === 2) return "text-orange-400";
  if (passwordStrength.value === 3) return "text-yellow-400";
  return "text-green-400";
});

const passwordStrengthLabel = computed(() => {
  if (passwordStrength.value <= 1) return "Weak";
  if (passwordStrength.value === 2) return "Fair";
  if (passwordStrength.value === 3) return "Good";
  return "Strong";
});

const submitForm = async () => {
  registerError.value = "";
  registerSuccess.value = "";
  registerErrors.value = { username: "", email: "", password: "" };

  let hasError = false;
  if (!formData.value.username.trim()) {
    registerErrors.value.username = "Name is required";
    hasError = true;
  }
  if (!validateEmail(formData.value.email)) {
    registerErrors.value.email = "Enter a valid email address";
    hasError = true;
  }
  if (formData.value.password.length < 8) {
    registerErrors.value.password = "Password must be at least 8 characters";
    hasError = true;
  }
  if (hasError) return;

  isRegisterLoading.value = true;
  try {
    const response = await fetch("http://127.0.0.1:8000/accounts/register/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData.value),
    });
    const data = await response.json();

    if (response.ok) {
      registerSuccess.value = "Account created! Please sign in.";
      formData.value = { username: "", email: "", password: "" };
      setTimeout(() => {
        isSignUpActive.value = false;
        registerSuccess.value = "";
      }, 1500);
    } else {
      if (data.errors) {
        const firstKey = Object.keys(data.errors)[0];
        const firstMsg = data.errors[firstKey];
        registerError.value = Array.isArray(firstMsg) ? firstMsg[0] : firstMsg;
      } else {
        registerError.value = data.detail || "Registration failed. Try again.";
      }
    }
  } catch {
    registerError.value = "Network error. Please check your connection.";
  } finally {
    isRegisterLoading.value = false;
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
