<svelte:head>
    <title>ACM | Amrita Canteen Management | Cart</title>
</svelte:head>

<script lang="ts">
    import Button from "$lib/Button.svelte";
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";
    import Payment from "$lib/Payment.svelte";
    import Process from "$lib/Process.svelte";

    import { onMount } from "svelte";
    import { browser } from "$app/environment";

    const paymentMethods = [
        {name: "Gpay", iconUrl: "/icon-gpay.png", handler: () => {selectedPaymentMethod = "Gpay"}, showLabel: false},
        {name: "Paytm", iconUrl: "/icon-paytm.png", handler: () => {selectedPaymentMethod = "Paytm"}, showLabel: false},
        {name: "Net Banking", iconUrl: "/icon-bank.png", handler: () => {selectedPaymentMethod = "Net Banking"}, showLabel: true},
        {name: "Cash", iconUrl: "/icon-rupee.png", handler: () => {selectedPaymentMethod = "Cash"}, showLabel: true},
    ]

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        category: string
    }

    interface CartItem extends Item {
        quantity: number
    }

    let proceedToPay: boolean = false
    let selectedPaymentMethod: string | null = null

    let cart: CartItem[] = []

    let selectedItem: Item | null = null
    let selectedQuantity: number = 0
    let showMiniCart: boolean = false
    
    let afterMount = false

    function handleSelect(item: Item) {
        const findCart = cart.find(cartItem => cartItem._id == item._id)
        if (findCart) {
            selectedQuantity = findCart.quantity
        } else {
            selectedQuantity = 0
        }
        selectedItem = item
        showMiniCart = true
    }

    function handleClose() {
        if (selectedItem) {
            const cartItem = {...selectedItem, quantity: selectedQuantity}
            const newCart = cart.filter(item => item._id != cartItem._id)

            if (selectedQuantity > 0) {
                cart = [cartItem, ...newCart]
            } else {
                cart = newCart
            }
        }

        selectedItem = null
        showMiniCart = false
    }

    function reset() {
        cart = []
        localStorage.removeItem("cart")
    }
    
    onMount(() => {
        const localCart = localStorage.getItem('cart')
        if (localCart) {
            cart = JSON.parse(localCart)
        }

        afterMount = true
        return
    })

    $: total = cart.reduce((sum, cartItem) => {return sum + cartItem.price * cartItem.quantity}, 0)
    $: if (browser && afterMount) {
        localStorage.setItem('cart', JSON.stringify(cart))
    }
</script>

<main>
    {#if proceedToPay && !selectedPaymentMethod}
        <Payment {paymentMethods} />
    {:else if selectedPaymentMethod}
        <Process on:orderPlaced={reset} {cart} {total} />
    {:else}
        <section>
            <h1>Cart</h1>

            {#if cart.length != 0}
                <ul>
                    {#each cart as item (item._id)}
                    <li on:mouseup={() => handleSelect(item)}>
                        <h2>{item.name}</h2>
                        <div>
                            <span>₨ {item.price * item.quantity}</span>
                            <span>{item.price} x {item.quantity}</span>
                        </div>
                    </li>
                    {/each}
                </ul>

                <p class="total">
                    Total <span>₨ {total}</span>
                </p>

                <div class="btn">
                    <Button on:click={() => proceedToPay=true} style="font-size: 1.675rem;">Proceed to Pay</Button>
                </div>
            {:else}
                <p class="empty">Cart is empty</p>
            {/if}
        </section>
    {/if}

    
    {#if showMiniCart && selectedItem && !proceedToPay}
        <MiniCart {handleClose} item={selectedItem} bind:quantity={selectedQuantity} />
    {/if}
    <Footer active="cart" />
</main>

<style>
    section {
        padding: 2rem;
        margin-bottom: 64px;
    }

    p.empty {
        font-size: 1rem;
        color: #444444;
    }

    h1 {
        margin: 0 0 0.5em;
        font-size: 3rem;
        font-weight: 700;

        color: #323232;
    }

    ul {
        padding: 0;
        list-style: none;
    }

    li {
        display: flex;
        justify-content: space-between;

        border-bottom: 1.5px solid #D9D9D9;
        margin-bottom: 0.5em;
        padding: 0.5em 0.5em;
    }

    li h2 {
        margin: 0;

        font-size: 1.125rem;
        font-weight: 600;

        color: #323232;
    }

    li span {
        display: block;

        font-size: 1rem;
        font-weight: 500;

        color: #444444;
    }

    li span:last-of-type {
        font-size: 0.8rem;
        text-align: right;
    }

    p.total {
        font-size: 1.5rem;
        font-weight: 600;
        color: #323232;

        text-align: right;
    }

    p.total span {
        display: inline-block;
        margin-left: 1em;

        font-size: 1.25rem;
        font-weight: 500;
        color: #444444;
    }

    div.btn {
        margin-top: 3.125em;

        display: flex;
        justify-content: center;
    }
</style>