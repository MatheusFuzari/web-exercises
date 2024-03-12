<script setup lang="ts">
const storagedItems = typeof window !== 'undefined' ? localStorage.getItem("ShopCart") : '';
const cartItems = storagedItems ? JSON.parse(storagedItems) : []

const model: any = ref({})
const equalItems = reactive({
  id: 0,
  quantity: 0,

});

</script>

<template>
  <main>
    <CustomNav />
    <div class='mt-28'>
      <section v-if='storagedItems'>
        <div class='flex flex-row justify-center'>
          <div class='flex flex-col'>
            <CheckoutCard v-for='(item, index) in cartItems' :key='index' :shopCart="item" :shopQuantity="1"
              v-model="model" />
          </div>
          <div class="h-fit p-2 w-1/5 bg-slate-100 border rounded mx-5">
            <p class='font-semibold text-lg'>Price: R$ {{ cartItems.productPrice }}</p>
            <button
              class='bg-green-400 text-black text-lg p-1 w-full rounded-md h-fit my-5 hover:bg-green-900 hover:text-white ease-in-out duration-150'>Comprar</button>
          </div>
        </div>
      </section>
      <section v-else>
        <p>SEM ITEMS</p>
      </section>
    </div>
  </main>
</template>