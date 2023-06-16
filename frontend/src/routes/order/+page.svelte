<svelte:head>
    <title>ACM | Amrita Canteen Management | Order</title>
</svelte:head>

<script lang="ts">
    import { onMount } from "svelte";
    import Footer from "$lib/Footer.svelte";
    import Status from "$lib/Status.svelte";

    type OrderStatus = "placed" | "preparing" | "ready" | "served";

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        out_of_stock: boolean;
    }

    interface CartItem extends Item {
        quantity: number;
    }

    interface Order {
        _id: number;
        items: CartItem[];
        total: number;
        status: OrderStatus;
    }

    interface Status {
        _id: number;
        status: OrderStatus;
    }

    let orders: Order[] | null = null

    async function refreshOrder() {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            }
        };

        if (orders) {
            const result = await fetch('http://localhost:8000/order/status', options) 
            const data: Status[] = await result.json()

            orders = orders.map(order => {
                const orderStatus = data.find((x: Status) => x._id == order._id)
                if (orderStatus) {
                    return {...order, ...orderStatus}
                } 
                return order
            })
        }
    }

    onMount(async () => {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${localStorage.getItem("token")}`,
            }
        };

        const result = await fetch('http://localhost:8000/order', options) 
        switch (result.status) {
            case 200:
                const data = await result.json()
                orders = data
                setInterval(refreshOrder, 2000)
                break
            case 401:
                alert("Login to view order")
                window.location.replace("/login")
                break
            default:
                alert("Unhandled error occurred")
        }
    })
</script>

<main>
    <section>
        <h1>Orders</h1>

        {#if orders && orders.length != 0}
            <ul class="order-container">
                {#each orders as order (order._id)}
                <li class="order">
                    <div class="order-info">
                        <div>Order no: <span>{order._id}</span></div>
                        <Status status={order.status} />
                    </div>
                    <ul class="item-container">
                        {#each order.items as item}
                        <li class="item">
                            <div>{item.name}</div>
                            <div>
                                <span>₨ {item.price} x {item.quantity}</span>
                            </div>
                        </li>
                        {/each}
                    </ul>

                    <p class="total">
                        Total <span>₨ {order.total}</span>
                    </p>
                </li>
                {/each}
            </ul>
        {:else}
            <p class="empty">Place an order to view</p>
        {/if}
    </section>

    <Footer active="order" />
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

    .order-container {
        padding: 0;
        list-style: none;
    }

    .order {
        border-bottom: 1.5px solid #D9D9D9;
        margin-bottom: 1em;
        padding: 0.5em 0 1em;
    }

    .order-info {
        display: flex;
        justify-content: space-between;

        margin-bottom: 0.5em;
    }

    .order-info div:first-of-type {
        font-size: 1rem;
        font-weight: 600;

        color: #323232;
    }

    .order-info div:first-of-type span {
        color: #444444;
    }

    .item-container {
        padding: 0;
        padding-left: 1em;
        list-style: none;
    }

    .item {
        display: flex;
        justify-content: space-between;
    }

    .item div:first-of-type {
        margin: 0;

        font-size: 0.8rem;
        font-weight: 500;

        color: #323232;
    }

    .item span {
        display: block;

        font-size: 0.8rem;
        font-weight: 400;

        color: #444444;
    }

    .total {
        margin: 0;
        font-size: 0.8rem;
        font-weight: 500;
        color: #323232;

        text-align: right;
    }

    .total span {
        display: inline-block;
        margin-left: 1em;

        font-size: 0.8rem;
        font-weight: 400;
        color: #444444;
    }
    
</style>