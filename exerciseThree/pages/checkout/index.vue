<script setup lang="ts">
import { useToast } from 'primevue/usetoast';
const toast = useToast();
const price = usePrice();
const cart = useCart();
const { calcPrice } = useChangeQnt();

calcPrice();


const purchase = async () => {
  const { data: cartHistory } = await useFetch('http://localhost:8000/carthistory/', {
    method: 'POST',
    body: {
      totalPrice: price.value
    }
  })
  for (let i = 0; i < cart.value.length; i++) {
    const { data: productBought } = await useFetch("http://localhost:8000/productbought/", {
      method: 'POST',
      body: {
        productFk: cart.value[i].id,
        cartFk: cartHistory.value?.id,
        quantity: cart.value[i].actualQnt
      }
    })
  }
  toast.add({
    severity: 'success',
    summary: "Compra realizada!"
  })
  cart.value = []
}

</script>

<template>
  <main>
    <CustomNav />
    <Toast />
    <div class='mt-28'>
      <section v-if='cart.length > 0'>

        <div class='flex flex-row justify-center'>
          <div class='flex flex-col'>
            <CheckoutCard v-for='(item, index) in cart' :key='index' :shopCart="item" />
          </div>
          <div class="h-fit p-2 w-1/5 bg-slate-100 border rounded mx-5">
            <p class='font-semibold text-lg'>Price: R$ {{ price }}</p>
            <button
              class='bg-green-400 text-black text-lg p-1 w-full rounded-md h-fit my-5 hover:bg-green-900 hover:text-white ease-in-out duration-150'
              @click="purchase">Comprar</button>


          </div>
        </div>
      </section>
      <section v-else>
        <p>OBRIGADO POR COMPRAR!, Volte a tela de produtos!</p>
      </section>
    </div>
  </main>
</template>