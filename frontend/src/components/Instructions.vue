<template>
  <div
    class="flex flex-col items-center w-[1200px] h-[785px] px-[80px] py-[96px] gap-[64px] mx-auto"
  >
    <div
      class="flex flex-col items-center w-[1040px] h-[87px] gap-[24px] text-center"
    >
      <h2
        class="w-[1040px] h-[39px] text-white font-bold text-[32px] leading-[39px] font-montserrat"
      >
        Brief Overview
      </h2>
      <p
        class="w-[1040px] h-[24px] text-gray-400 font-normal text-[20px] leading-[24px] font-montserrat"
      >
        Learn to manage assets and automate tasks in real time.
      </p>
    </div>

    <div
      class="relative w-[872px] h-[442px] bg-black rounded-[20px] border border-gray-400 overflow-hidden"
    >
      <video
        ref="videoRef"
        class="absolute inset-0 w-full h-full object-cover"
        :src="videoSrc"
        @loadedmetadata="onLoadedMetadata"
        @timeupdate="onTimeUpdate"
      />

      <div
        v-if="!isPlaying"
        class="absolute inset-0 flex items-center justify-center"
        @click="togglePlay"
      >
        <div
          class="w-[100px] h-[100px] flex items-center justify-center rounded-full border-2 border-white cursor-pointer"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M8 5V19L19 12L8 5Z" fill="white" />
          </svg>
        </div>
      </div>

      <div
        class="absolute bottom-0 left-0 right-0 px-[8px] py-[8px] flex items-center gap-[16px] bg-black/80 rounded-[8px] mx-[91px] my-[10px]"
        :class="showControls ? 'opacity-100' : 'opacity-0'"
        @mouseenter="showControls = true"
        @mouseleave="showControls = false"
      >
        <button
          class="w-[48px] h-[40px] flex items-center justify-center"
          @click="togglePlay"
        >
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              :d="isPlaying ? 'M10 16V8L16 12L10 16Z' : 'M8 5V19L19 12L8 5Z'"
              fill="white"
            />
          </svg>
        </button>

        <div
          class="w-[594px] h-[8px] bg-gray-600 rounded-[20px] cursor-pointer relative"
          @click="onProgressClick"
        >
          <div
            class="absolute top-0 left-0 h-full bg-white rounded-[20px]"
            :style="{ width: `${progress}%` }"
          />
        </div>

        <div class="flex items-center gap-[20px] ml-auto">
          <button
            class="w-[24px] h-[24px] flex items-center justify-center border border-white rounded-sm"
            @click="toggleMute"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                :d="
                  isMuted
                    ? 'M11 5L6 9H2V15H6L11 19V5ZM15.54 8.46L19.07 12L15.54 15.54L14.12 14.12L16.17 12L14.12 9.88L15.54 8.46Z'
                    : 'M11 5L6 9H2V15H6L11 19V5Z'
                "
                stroke="white"
                stroke-width="2"
              />
            </svg>
          </button>

          <button
            class="w-[24px] h-[24px] flex items-center justify-center border border-white rounded-sm"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M19.43 12.98C19.8 13.5 20 14.1 20 14.72V18.5C20 19.33 19.33 20 18.5 20H15.5C14.9 20 14.3 19.7 13.88 19.2L12 17L10.12 19.2C9.7 19.7 9.1 20 8.5 20H5.5C4.67 20 4 19.33 4 18.5V14.72C4 14.1 4.2 13.5 4.57 12.98L2.5 12.5C1.8 12.37 1.8 11.63 2.5 11.5L4.57 11.02C4.2 10.5 4 9.9 4 9.28V5.5C4 4.67 4.67 4 5.5 4H8.5C9.1 4 9.7 4.3 10.12 4.8L12 7L13.88 4.8C14.3 4.3 14.9 4 15.5 4H18.5C19.33 4 20 4.67 20 5.5V9.28C20 9.9 19.8 10.5 19.43 10.98L21.5 11.5C22.2 11.63 22.2 12.37 21.5 12.5L19.43 12.98Z"
                stroke="white"
                stroke-width="2"
              />
            </svg>
          </button>

          <button
            class="w-[24px] h-[24px] flex items-center justify-center border border-white rounded-sm"
          >
            <svg
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M10 14L14 10M14 14L10 10"
                stroke="white"
                stroke-width="2"
                stroke-linecap="round"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";

const videoSrc = "/path/";

const videoRef = ref(null);
const isPlaying = ref(false);
const isMuted = ref(false);
const duration = ref(0);
const currentTime = ref(0);
const showControls = ref(false);

const progress = computed(() => {
  if (!duration.value) return 0;
  return (currentTime.value / duration.value) * 100;
});

const onLoadedMetadata = () => {
  duration.value = videoRef.value?.duration || 0;
};

const onTimeUpdate = () => {
  currentTime.value = videoRef.value?.currentTime || 0;
};

const onProgressClick = (e) => {
  const rect = e.target.getBoundingClientRect();
  const percent = (e.clientX - rect.left) / rect.width;
  if (videoRef.value) {
    videoRef.value.currentTime = percent * duration.value;
  }
};

// Управление воспроизведением
const togglePlay = () => {
  if (!videoRef.value) return;
  if (isPlaying.value) {
    videoRef.value.pause();
  } else {
    videoRef.value.play();
  }
  isPlaying.value = !isPlaying.value;
};

const toggleMute = () => {
  if (!videoRef.value) return;
  videoRef.value.muted = !isMuted.value;
  isMuted.value = !isMuted.value;
};
</script>

<style>
@font-face {
  font-family: "Montserrat";
  src: url("path/to/Montserrat-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
}
@font-face {
  font-family: "Montserrat";
  src: url("path/to/Montserrat-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
}
.font-montserrat {
  font-family: "Montserrat", sans-serif;
}
</style>
