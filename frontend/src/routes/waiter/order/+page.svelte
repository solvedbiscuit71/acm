<svelte:head>
    <title>ACM | Waiter | Order</title>
</svelte:head>

<script lang="ts">
    import Filter from "$lib/waiter/Filter.svelte";
    import Navbar from "$lib/waiter/Navbar.svelte";
    import Status from "$lib/Status.svelte";
    import UpdateButton from "$lib/waiter/UpdateButton.svelte";

    import { onMount } from "svelte";
    import { browser } from "$app/environment";

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
        user_name: string;
        items: CartItem[];
        total: number;
    }

    let orders: Order[]

    async function fetchOrder() {
        if (browser) {
            const options = {
                method: 'GET',
                headers: {
                    Status: currentFilter,
                    Authorization: `Bearer ${localStorage.getItem("waiter-token")}`,
                },
            };

            const result = await fetch('http://localhost:8000/order/filter', options)
            const data = await result.json()

            return data
        }
    }

    const nextStatus = {
        placed: "preparing",
        preparing: "ready",
        ready: "served",
    }

    async function updateOrder(orderId: number) {
        if (currentFilter == 'served' || !browser) {
            return
        }

        const options = {
            method: 'PATCH',
            headers: {
                Status: nextStatus[currentFilter],
                Authorization: `Bearer ${localStorage.getItem("waiter-token")}`,
            },
        };

        const result = await fetch(`http://localhost:8000/order/${orderId}`, options)
        switch (result.status) {
            case 200:
                changeFilter(currentFilter)
                break
            default:
                alert("Unhandled error occured")
        }
    }

    const filters = [
        {name: 'placed', handleClick: () => changeFilter('placed'), imageUrl: '/icon-orange-tick.png', nextStatus: 'preparing'},
        {name: 'preparing', handleClick: () => changeFilter('preparing'), imageUrl: '/icon-green-tick.png', nextStatus: 'preparing'},
        {name: 'ready', handleClick: () => changeFilter('ready'), imageUrl: '/icon-purple-tick.png', nextStatus: 'preparing'},
        {name: 'served', handleClick: () => changeFilter('served'), imageUrl: '', nextStatus: ''},
    ]
    type FilterType = 'placed' | 'preparing' | 'ready' | 'served'
    let currentFilter: FilterType = 'placed'

    $: imageUrl = filters.filter(x => x.name == currentFilter)[0].imageUrl
    $: textContent = "Mark as " + filters.filter(x => x.name == currentFilter)[0].nextStatus

    function changeFilter(newFilter: FilterType) {
        currentFilter = newFilter
        orders = []

        setTimeout(() => {
            fetchOrder().then(data => orders = data)
        }, 0)
    }

    onMount(() => {
        fetchOrder().then(data => orders = data)

        setInterval(() => {
            fetchOrder().then(data => orders = data)
        }, 2000)
    })
</script>

<main>
    <Navbar/>
    <Filter {filters} {currentFilter} />

    <section>
        {#if orders && orders.length != 0}
            <ul class="order-container">
                {#each orders as order (order._id)}
                <li class="order">
                    <div class="order-info">
                        <div>
                            <div>Order no: <span>{order._id}</span></div>
                            <Status status={currentFilter} />
                        </div>
                        <div>
                            By {order.user_name}
                        </div>
                    </div>
                    <ul class="item-container">
                        {#each order.items as item}
                        <li class="item">
                            <div>{item.name}</div>
                            <div>
                                <span>x {item.quantity}</span>
                            </div>
                        </li>
                        {/each}
                    </ul>

                    {#if currentFilter != 'served'}
                        <UpdateButton {imageUrl} {textContent} on:click={() => updateOrder(order._id)} />
                    {/if}
                </li>
                {/each}
            </ul>
        {:else}
            <p class="empty">No orders</p>
        {/if}
    </section>
</main>

<style>
    main {
        min-height: 100vh;
    }

    section {
        padding: 0 1em 1.5em;
    }

    p.empty {
        font-size: 1rem;
        color: #444444;
    }

    .order-container {
        padding: 0;
        list-style: none;
    }

    .order {
        border-radius: 8px;
        box-shadow: 0px 1px 4px #00000040;
        margin-bottom: 1em;
        padding: 1em 0.875em;
    }

    .order-info > div:first-of-type {
        display: flex;
        justify-content: space-between;

        font-size: 1.125rem;
        font-weight: 600;

        color: #323232;
    }

    .order-info > div:last-of-type {
        font-size: 0.875rem;
        font-weight: 500;

        color: #323232;

        margin-bottom: 1em;
    }

    .order-info div:first-of-type span {
        color: #444444;
    }

    .item-container {
        padding: 0;
        list-style: none;

        margin-bottom: 0.625em;
    }

    .item {
        display: flex;
        justify-content: space-between;
    }

    .item div:first-of-type {
        margin: 0;

        font-size: 0.9375rem;
        font-weight: 400;

        color: #323232;
    }

    .item span {
        display: block;

        font-size: 0.9375rem;
        font-weight: 400;

        color: #444444;
    }


</style>