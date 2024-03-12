<script setup lang="ts">
const props = defineProps({
  id: { type: Number },
  productImg: { type: String },
  productName: { type: String },
  productPrice: { type: Number },
  productQnt: { type: Number, required: true },
})

const emit = defineEmits(['clicked'])

</script>

<template>
  <div class="bg-gray-100 w-56 h-56 rounded-lg border border-gray-300">
    <div class="flex w-2/3 m-auto justify-center content-center self-center">
      <div v-if="props.productQnt > 0">
        <p class=' bg-green-200 p-1 rounded-md h-8 z-10 mt-1'>Instock</p>
      </div>
      <div v-else>
        <p class=' bg-red-200 p-1 rounded-md h-8 z-10 mt-1'>Outstock</p>
      </div>
      <img alt="imagem" :src="props.productImg" class='m-3 w-5/6' />
    </div>
    <div class="flex flex-col col-span-12">
      <div class="flex flex-row content-between justify-between mx-5">
        <p>{{ props.productName }}</p>
        <button class="bg-black text-white rounded-md p-1 hover:bg-gray-700"
          @click="emit('clicked', props)">Comprar</button>
      </div>
      <p class='justify-center text-center text-gray-500'>R$: {{ props.productPrice }}</p>
    </div>
  </div>
</template>