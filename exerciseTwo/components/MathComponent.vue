<script setup lang="ts">
const props = defineProps({
    labelOne: { type: String, required: true },
    labelTwo: { type: String, required: true },
    operation: { type: String, required: true },
});

const firstvalue = ref(0);
const secondvalue = ref(0);
const makeOperation = (n1: number, n2: number) => {
    switch (props.operation) {
        case 'Multiply':
            return n1 * n2;
        case 'Division':
            return n1 / n2;
        case 'Plus':
            return n1 + n2;
        case 'Minus':
            return n1 - n2;
        case 'SquareRoot':

            return [Math.sqrt(n1), Math.sqrt(n2)];
    };
};

const result = computed(() =>
    makeOperation(firstvalue.value, secondvalue.value)
)
const emit = defineEmits(['changed'])

</script>

<template>
    <div class="flex flex-col justify-center dark:text-white">
        <section class="m-auto text-center justify-items-center  rounded-3xl bg-slate-200 w-80 h-80 dark:bg-green-400">
            <p>{{ props.operation }}</p>
            <br>
            <label for='firstNumber' class='text-black'>{{ props.labelOne }}</label>
            <br>
            <input id='firstNumber' class="border-b-2 border-slate-800 outline-none p-2 bg-slate-100 text-black
            dark:text-black dark:bg-green-200" type="number" v-model="firstvalue"></input>
            <br>
            <label for='secondNumber' class="text-black">{{ props.labelTwo }}</label>
            <br>
            <input id='secondNumber'
                class="border-b-2 p-2 border-slate-800 outline-none bg-slate-100 text-black dark:text-black dark:bg-green-200"
                type="number" v-model="secondvalue"></input>
            <p>{{ result }}</p>
        </section>
    </div>
</template>