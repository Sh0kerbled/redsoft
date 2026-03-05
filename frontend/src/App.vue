<template>
  <RouterView />
</template>

<!-- <script>
export default {
  name: "App",
  beforeCreate() {
    this.$store.commit("initializeStore");

    const access = this.$store.state.access;

    if (access) {
      axios.defaults.headers.common[Auth] = "JWT" + access;
    }
  },
};
</script> -->

<script setup>
import { RouterView } from "vue-router";
</script>
