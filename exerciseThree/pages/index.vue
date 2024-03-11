<script setup lang="ts">
const products = [
  {
    productId: 1,
    productImg: 'https://microimport.com.br/wp-content/uploads/iphone-12-de-128-gb.webp',
    productName: 'iPhone 2099',
    productPrice: 8549.99,
    productQnt: 48,
  }
]

const cart: Ref<number[]> = ref([])

const sendCartData = () => {
  sessionStorage.setItem('CARRINHO', JSON.stringify(cart));
}
</script>

<template>
  <main>
    <nav class="flex items-center justify-between flex-wrap bg-slate-100 p-6 border-b">
      <div class="w-full flex flex-grow items-center">
        <div class="flex-grow text-md">
          <a class="inline-block text-black mr-4 hover:text-green-600 cursor-pointer hover:outline-2">Produtos</a>
        </div>
        <div class="flex flex-grow items-center flex-shrink-0">
          <img class="w-12 text-center"
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/LOUD_logo.svg/1200px-LOUD_logo.svg.png">
        </div>
        <div>
          <NuxtLink @click='sendCartData' to='checkout' class='inline-block text-md px-6 py-4 leading-none border-2 rounded text-black border-white
            hover:border-transparent hover:bg-white hover:text-green-400 mt-0 cursor-pointer'>
            Check-out</NuxtLink>
        </div>
      </div>
    </nav>
    <section class='grid grid-cols-5 gap-4 w-screen align-middle place-items-center mt-12'>
      <ItemsCard v-for="index in 10" :productImg="products[0].productImg" :productQnt="products[0].productQnt"
        :productName="products[0].productName" :productPrice="products[0].productPrice" :id="products[0].productId"
        @clicked="(e) => cart.push(e)" />
    </section>
  </main>
</template>