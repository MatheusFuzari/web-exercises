<script setup lang="ts">
const props = defineProps({
  shopCart: { type: Object, required: true },
});
const { changeQnt, deleteProduct } = useChangeQnt();
</script>
<template>
  <div class='p-8 bg-gray-100 flex flex-row h-fit'>
    <div class='w-52 mx-5'>
      <img :src='props.shopCart.productImg'>
    </div>
    <div class="flex flex-col justify-between h-100% w-4/6">
      <p class='text-lg font-semibold'>{{ props.shopCart.productName }}</p>
      <div class='flex flex-row gap-5'>
        <select :name="props.shopCart.id" v-on:input="changeQnt($event.target.value, props.shopCart.id)"
          :defaultValue="props.shopCart.actualQnt">
          <option v-for='quantity of props.shopCart.productQnt' :value='quantity'
            v-bind:selected="props.shopCart.actualQnt == quantity">{{
        quantity }}
          </option>
        </select>
        <button class='underline text-green-700' @click="() => deleteProduct(props.shopCart.id)">Excluir</button>
      </div>
    </div>
    <p class='font-semibold text-lg'>Price: R$:{{ props.shopCart.productPrice }}</p>
  </div>
</template>