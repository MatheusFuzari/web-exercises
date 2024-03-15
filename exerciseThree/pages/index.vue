<script setup lang="ts">
import type { IProducts } from '~/interfaces/produtos';

const products: IProducts[] = [
  {
    id: 1,
    productImg: 'https://microimport.com.br/wp-content/uploads/iphone-12-de-128-gb.webp',
    productName: 'iPhone 2099',
    productPrice: 8549.99,
    productQnt: 48,
    actualQnt: 0
  },
  {
    id: 2,
    productImg: 'https://mf.b37mrtl.ru/rbthmedia/images/2019.09/original/5d81078c15e9f902e111a482.jpg',
    productName: 'iPhone 2100',
    productPrice: 8549.99,
    productQnt: 48,
    actualQnt: 0
  }
];

const cart = useCart();

const testCart = (item: IProducts) => {
  if (cart.value.findIndex((x) => x.id == item.id) != -1) {
    const addQnt = (array: any) => { return array += 1 };
    toRaw(cart.value[cart.value.findIndex((x) => x.id == item.id)]).actualQnt = addQnt(cart.value[cart.value.findIndex((x) => x.id == item.id)].actualQnt);
  } else {
    toRaw(item).actualQnt = 1
    cart.value.push(item);
    console.log(cart);
  }
}

</script>

<template>
  <main>
    <CustomNav />
    <div class='mt-28'>
      <section
        class='grid grid-cols-1 gap-4 w-screen align-middle place-items-center mt-12 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
        <ItemsCard v-for="product in products" :productImg="product.productImg" :productQnt="product.productQnt"
          :productName="product.productName" :productPrice="product.productPrice" :id="product.id"
          @clicked="(e) => testCart(e)" />
      </section>
    </div>
  </main>
</template>