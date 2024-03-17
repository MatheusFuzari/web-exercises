<script setup lang="ts">
const price = usePrice();
const cart = useCart();
const { calcPrice } = useChangeQnt();
calcPrice();
</script>

<template>
  <main>
    <CustomNav />
    <div class='mt-28'>
      <section v-if='cart.length > 0'>
        <div class='flex flex-row justify-center'>
          <div class='flex flex-col'>
            <CheckoutCard v-for='(item, index) in cart' :key='index' :shopCart="item" />
          </div>
          <div class="h-fit p-2 w-1/5 bg-slate-100 border rounded mx-5">
            <p class='font-semibold text-lg'>Price: R$ {{ price }}</p>
            <button
              class='bg-green-400 text-black text-lg p-1 w-full rounded-md h-fit my-5 hover:bg-green-900 hover:text-white ease-in-out duration-150'>Comprar</button>
          </div>
        </div>
      </section>
      <section v-else>
        <p>nada por aqui</p>
      </section>
    </div>
  </main>
</template>