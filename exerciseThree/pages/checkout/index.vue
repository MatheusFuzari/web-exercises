<script setup lang="ts">
const cart = typeof window !== 'undefined' ? sessionStorage.getItem("CARRINHO") : null;

</script>

<template>
  <p>
    {{ cart }}
  </p>
</template>