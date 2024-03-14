<script setup lang="ts">
interface IProducts {
  id: number;
  productImg: string;
  productName: string;
  productPrice: number;
  productQnt: number;
  actualQnt: number;
}

const storagedItems = typeof window !== 'undefined' ? localStorage.getItem("ShopCart") : '';
const cartItems: IProducts[] = storagedItems ? JSON.parse(storagedItems) : []

const price = ref(0);
cartItems.forEach((x) => {
  price.value += (x.productPrice * x.actualQnt);
})

const totalPrice = computed(() => (e: number) => {
  console.log(e)
});
</script>

<template>
  <main>
    <CustomNav />
    <div class='mt-28'>
      <section v-if='storagedItems'>
        <div class='flex flex-row justify-center'>
          <div class='flex flex-col'>
            <CheckoutCard v-for='(item, index) in cartItems' :key='index' :shopCart="item"
              @clicked="(e) => totalPrice(e)" />
          </div>
          <div class="h-fit p-2 w-1/5 bg-slate-100 border rounded mx-5">
            <p class='font-semibold text-lg'>Price: R$ {{ price }}</p>
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