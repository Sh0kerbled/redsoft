<template>
  <section class="container mx-auto px-6 py-16">
    <h2 class="text-3xl font-bold text-center mb-12">Advantages</h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div
        v-for="adv in advantages"
        :key="adv.title"
        class="bg-gradient-to-br from-[#1a0b12] to-[#0a0508] border border-red-900/40 rounded-2xl p-8 relative overflow-hidden group hover:border-red-700 transition duration-300"
      >
        <div
          class="absolute top-0 right-0 w-32 h-32 bg-red-600/10 rounded-bl-full blur-xl"
        ></div>
        <div
          class="w-12 h-12 rounded-lg bg-red-950 border border-red-800 flex items-center justify-center mb-6 text-red-500"
          v-html="adv.icon"
        ></div>
        <h3 class="text-xl font-bold mb-3">{{ adv.title }}</h3>
        <p class="text-gray-400 text-sm leading-relaxed">{{ adv.desc }}</p>
      </div>
    </div>
  </section>
</template>

<script setup>
const advantages = [
  {
    title: "Protection",
    desc: "We guarantee the security of your data. Many hashing algorithms prevent passwords from being stored in plain text, protecting your library from unauthorized access.",
    icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>',
  },
  {
    title: "Time",
    desc: "Forget about manually searching through text files. Our system optimizes database work, allowing us to find the right account among thousands of records in a split second.",
    icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>',
  },
  {
    title: "Price",
    desc: "We offer a professional solution at an affordable price. The price is fully consistent with the quality of the automation tools and the level of protection you receive.",
    icon: '<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z"></path></svg>',
  },
];
</script>
