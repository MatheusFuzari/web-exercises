<script setup lang="ts">
const props = defineProps({
  buttonName: { type: String },
  buttonValue: { type: String },
})

const emit = defineEmits(["clicked"])
</script>
<template>
  <Button @click="emit('clicked', props.buttonValue)"
    class="w-24 h-6 rounded-lg bg-gray-700 text-white hover:bg-gray-900 ease-in-out duration-100 dark:bg-green-400 dark:hover:bg-green-600">{{
    props.buttonName
  }}</Button>
</template>