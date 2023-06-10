<script lang="ts">
    import { onMount, createEventDispatcher } from "svelte";

    const backend_url = "http://localhost:8000"
    const dispatcher = createEventDispatcher()

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

    let orderPlaced: boolean = false
    export let cart: CartItem[]
    export let total: number

    async function placeOrder() {
        if (cart.length != 0) {
            const options = {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${localStorage.getItem('token')}`
                },
                body: JSON.stringify({
                    "items": cart,
                    "total": total
                })
            };

            const result = await fetch(`${backend_url}/order`, options)
            switch (result.status) {
                case 200:
                    orderPlaced = true
                    dispatcher("orderPlaced")
                    break
                case 401:
                    alert("Login to place order")
                    dispatcher("orderPlaced")
                    window.location.replace("/login")
                    break
                default:
                    alert("Unhandled error occurred")
            }
        }
    }

    onMount(() => {
        setTimeout(placeOrder, 5000)
    })
</script>

<section>
    {#if !orderPlaced}
    <div>
        <h1>Processing</h1>
        <img src="/icon-loader.png" alt="Loading icon" class="spin">
    </div>
    {:else}
    <div>
        <h1>Order Placed</h1>
        <img src="/icon-complete.png" alt="Check icon">
    </div>
    {/if}
</section>

<style>
    section {
        min-height: calc(100vh - 64px);

        background-color: white;
        background-image: url('/bg-top-colored.png'), url('/bg-bottom-colored.png');
        background-repeat: no-repeat;
        background-position: 0 0, 100% 100%;
    }

    section, div {
        display: flex;
        flex-direction: column;

        justify-content: center;
        align-items: center;
    }

    h1 {
        font-size: 3rem;
        font-weight: 700;
        color: #444;

        margin: 0;
    }

    .spin {
        animation-name: rotate;
        animation-duration: 1.25s;
        animation-timing-function: linear;
        animation-iteration-count: infinite;
    }

    @keyframes rotate {
        from {transform: rotate(0deg);}
        to {transform: rotate(360deg);}
    }
</style>