export default function () {
    const price = usePrice();
    const cart = useCart();
    const relativePrice = () => {
        for(let i=0;i<cart.value.length;i++){
            price.value = (cart.value[i].actualQnt * cart.value[i].productPrice);
        }
    }

    return {relativePrice};
}