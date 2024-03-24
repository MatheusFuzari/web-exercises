export default function () {
    const price = usePrice();
    const cart = useCart();

    const calcPrice = () => {
        cart.value.forEach((x) => {
            price.value += (x.actualQnt * x.productPrice);
        });
    };

    const changeQnt = (newQnt: number, id: number) => {
        cart.value.forEach((x) => {
            if (x.id == id) {
                toRaw(x).actualQnt = newQnt;
            };
        });
        price.value = 0;
        calcPrice();
    };

    const deleteProduct = (id: number) => {
        const index = cart.value.findIndex((x) => x.id == id);
        cart.value.splice(index, 1);
        price.value = 0;
        calcPrice();
    };

    return { changeQnt, calcPrice, deleteProduct };
}