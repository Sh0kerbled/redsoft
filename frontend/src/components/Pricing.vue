<template>
  <section class="container mx-auto px-6 py-16 mb-24">
    <div class="text-center mb-16">
      <h2 class="text-3xl font-bold mb-4">Pricing</h2>
      <p class="text-gray-400 text-sm">
        Choose the perfect plan to automate your Steam routine and start
        boosting your account today.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto">
      <div
        v-for="plan in plans"
        :key="plan.name"
        :class="[
          'border rounded-2xl p-8 flex flex-col transition duration-300',
          plan.highlight
            ? 'bg-gradient-to-b from-[#300b17] to-[#120409] border-red-700 transform scale-105 shadow-[0_0_30px_rgba(220,38,38,0.15)] z-10 relative'
            : 'bg-gradient-to-b from-[#160812] to-[#0a0307] border-red-900/30 hover:-translate-y-2',
        ]"
      >
        <h3
          :class="[
            'text-2xl font-bold mb-2',
            plan.highlight ? 'text-white' : '',
          ]"
        >
          {{ plan.name }}
        </h3>
        <div
          :class="[
            'text-sm mb-6 pb-6 border-b',
            plan.highlight
              ? 'text-red-400 border-red-900/50'
              : 'text-gray-400 border-gray-800',
          ]"
        >
          {{ plan.price }}
        </div>

        <ul
          :class="[
            'space-y-4 flex-1 text-sm mb-8',
            plan.highlight ? 'text-gray-200' : 'text-gray-300',
          ]"
        >
          <li
            v-for="feature in plan.features"
            :key="feature"
            class="flex items-center gap-3"
          >
            <svg
              class="w-4 h-4 text-red-500"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M5 13l4 4L19 7"
              ></path>
            </svg>
            {{ feature }}
          </li>
        </ul>

        <button
          :class="[
            'w-full py-3 rounded-lg font-semibold transition',
            plan.highlight
              ? 'bg-red-600 hover:bg-red-500 text-white shadow-[0_0_15px_rgba(220,38,38,0.4)]'
              : 'bg-red-950/50 text-red-500 border border-red-900/50 hover:bg-red-900 hover:text-white',
          ]"
        >
          ACTIVATE
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
const plans = [
  {
    name: "Basic",
    price: "Free",
    highlight: false,
    features: ["2 Steam accounts", "Single session", "Basic monitoring"],
  },
  {
    name: "Pro",
    price: "$2.99 / mo",
    highlight: true,
    features: [
      "5 Steam accounts",
      "Simultaneous Sessions",
      "Priority Boosting",
      "Full Analytics",
      "Interactive Advice",
      "Early Features",
    ],
  },
  {
    name: "Ultimate",
    price: "$9.99 / mo",
    highlight: false,
    features: [
      "50 Steam accounts",
      "Unlimited Sessions",
      "High-load Optimization",
      "Live System Diagnostics",
      "Anti-Cheat Stealth Mode",
      "Risk Management",
      "Priority Support",
    ],
  },
];
</script>
