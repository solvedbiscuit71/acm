<svelte:head>
    <title>ACM | Amrita Canteen Management | Menu</title>
</svelte:head>

<script lang="ts">
    import Category from "$lib/Category.svelte";
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";
    import { onMount } from "svelte";
    import { browser } from "$app/environment";

    const backend_url = "http://localhost:8000"

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

    interface Category {
        _id: string;
        starts_from: string;
        items: Item[]
    }

    let cart: CartItem[] = []
    let categories: Category[] | null = null

    let selectedItem: Item | null = null
    let selectedQuantity: number = 0
    let showMiniCart: boolean = false

    let afterMount: boolean = false

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

    function handleUpdate() {
        if (selectedItem) {
            const cartItem = {...selectedItem, quantity: selectedQuantity}
            const newCart = cart.filter(item => item._id != cartItem._id)

            if (selectedQuantity > 0) {
                cart = [cartItem, ...newCart]
            } else {
                cart = newCart
            }
        }
    }

    function handleClose() {
        handleUpdate()

        selectedItem = null
        showMiniCart = false
    }

    onMount(async () => {
        const result = await fetch(backend_url + "/menu")
        switch (result.status) {
            case 200:
                const data = await result.json()
                categories = data;
                
                const localCart = localStorage.getItem('cart')
                if (localCart) {
                    cart = JSON.parse(localCart)
                } 
                break
            default:
                alert("unhandled error occured")
        }

        afterMount = true
        return
    })

    $: if (browser && afterMount) {
        localStorage.setItem('cart', JSON.stringify(cart))
    }
</script>

<main>
    <section class="heading">
        <h1>
            <span>Welcome</span>
            <span>back!</span>
        </h1>
    </section>

    <section class="category-container">
        {#if categories}
            {#each categories as category (category._id)}
                <Category {handleSelect}  name="{category._id}" starts_from="{category.starts_from}" items={category.items} />
            {/each}
        {/if}
    </section>


    {#if showMiniCart && selectedItem}
        <MiniCart {handleUpdate} {handleClose} item={selectedItem} bind:quantity={selectedQuantity} />
    {/if}
    <Footer active="home" />
</main>

<style>
    .heading {
        padding: 2em 1.5em 0;
    }

    .category-container {
        padding: 0 0 1em 1.5em;
        margin-bottom: 64px;

        display: flex;
        flex-direction: column;

        gap: 2.5em;
    }

    h1 {
        margin: 0;
        font-size: 3rem;
        font-style: 700;

        color: #323232;
    }

    h1 span {
        display: block;
    }

    h1 span:last-of-type {
        position: relative;
        bottom: 0.4em;
    }
</style>
