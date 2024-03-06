<script setup lang="ts">
    const selectedMedia = ref("");
</script>

<template>
    <main>
        <p>{{ selectedMedia.value }}</p>
        <CustomSelectBox label="Select Xsqdl" :options="['Instagram','GitHub','Twitter','Linkedn']" v-model="selectedMedia"></CustomSelectBox>
    </main>
</template>
