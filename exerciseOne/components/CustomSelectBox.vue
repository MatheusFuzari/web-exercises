<script setup lang="ts">
    const props = defineProps({
        label: {type: String, required: true},
        selectText: {type: String, default: "Select Media"},
        selectId: {type: String, default: "customSelectBox"},
        options: {type: Array, required: true},
    });


    const model = defineModel();
</script>

<template>
    <section>
        <label :for="props.selectId">{{ props.label }}: </label>
        <select v-model="model":id="props.selectId">
            <option disabled="true" selected>
                {{ props.selectText }}
            </option>
            <option v-for="(option, index) in props.options" :key="index" v-bind:value="{value: option}">
                {{ option }}
            </option>
        </select>
    </section>
</template>