<script lang="ts" setup>

</script>
<template>
  <nav class="fixed top-0 left-0 right-0 flex items-center justify-between flex-wrap bg-slate-100 p-6 border-b">
    <div class="w-full flex flex-grow items-center">
      <div class="flex-grow text-md">
        <NuxtLink to='/' class="inline-block text-black mr-4 hover:text-green-600 cursor-pointer hover:outline-2">
          Produtos</NuxtLink>
      </div>
      <div class="flex flex-grow items-center flex-shrink-0">
        <img class="w-12 text-center"
          src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/LOUD_logo.svg/1200px-LOUD_logo.svg.png">
      </div>
      <div>
        <NuxtLink to='checkout' class='inline-block text-md px-6 py-4 leading-none border-2 rounded text-black border-white
            hover:border-transparent hover:bg-white hover:text-green-400 mt-0 cursor-pointer'>
          Check-out</NuxtLink>
      </div>
    </div>
  </nav>
</template>