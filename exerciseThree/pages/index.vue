<script setup lang="ts">
const products = [
  {
    productId: 1,
    productImg: 'https://microimport.com.br/wp-content/uploads/iphone-12-de-128-gb.webp',
    productName: 'iPhone 2099',
    productPrice: 8549.99,
    productQnt: 48,
  },
  {
    productId: 2,
    productImg: 'https://mf.b37mrtl.ru/rbthmedia/images/2019.09/original/5d81078c15e9f902e111a482.jpg',
    productName: 'iPhone 2100',
    productPrice: 8549.99,
    productQnt: 48,
  }
];

function checkForDuplicates(array: Array<Object>) {
  const counts: any = {};
  array.forEach(function (x: any) {
    console.log(x)
    counts[x.id] = (counts[x.id] || 0) + 1;
  });
  return counts;
}

const sendCartData = computed(() => (item: Object) => {
  const storagedItems = localStorage.getItem('ShopCart');
  let newCart = ref([]);
  newCart = storagedItems ? JSON.parse(storagedItems) : [];
  if (newCart.findIndex((x) => x.id == item.id) != -1) {
    newCart[newCart.findIndex((x) => x.id == item.id)].actualQnt += 1;
  } else {
    toRaw(item).actualQnt = 0
    newCart.push(item);
    console.log(newCart);
  }
  localStorage.setItem('ShopCart', JSON.stringify(newCart));
});
</script>

<template>
  <main>
    <CustomNav />
    <div class='mt-28'>
      <section
        class='grid grid-cols-1 gap-4 w-screen align-middle place-items-center mt-12 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5'>
        <ItemsCard v-for="product in products" :productImg="product.productImg" :productQnt="product.productQnt"
          :productName="product.productName" :productPrice="product.productPrice" :id="product.productId"
          @clicked="(e) => sendCartData(e)" />
      </section>
    </div>
  </main>
</template>