<script setup lang="ts">
import MathComponent from '~/components/MathComponent.vue';
const response: any = ref(0);
const darkMode = ref('');
const operation: any = ref('Plus');
</script>

<template>
  <main :class="darkMode">
    <div class='w-screen h-screen bg-white dark:bg-gray-900'>
      <div>
        <div class="flex flex-row m-auto justify-center text-center w-60 gap-10">
          <p class="dark:text-white">Response: {{ response }}</p>
          <InputSwitch v-model="darkMode" trueValue="dark" falseValue="light"></InputSwitch>
        </div>
        <div class="flex flex-row m-auto justify-center text-center w-full gap-10 my-3">
          <CustomButton buttonName='Sum' buttonValue='Plus' @clicked="(event) => { operation = event }"></CustomButton>
          <CustomButton buttonName='Minus' buttonValue='Minus' @clicked="(event) => { operation = event }">
          </CustomButton>
          <CustomButton buttonName='Multiply' buttonValue='Multiply' @clicked="(event) => { operation = event }">
          </CustomButton>
          <CustomButton buttonName='Division' buttonValue='Division' @clicked="(event) => { operation = event }">
          </CustomButton>
          <CustomButton buttonName='Square Root' buttonValue='SquareRoot' @clicked="(event) => { operation = event }">
          </CustomButton>
        </div>
      </div>
      <MathComponent labelOne='Number 1: ' labelTwo='Number 2: ' :operation='operation' />
    </div>
  </main>
</template>