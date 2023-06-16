<svelte:head>
    <title>ACM | Waiter | Item</title>
</svelte:head>

<script lang="ts">
    import Filter from "$lib/waiter/Filter.svelte";
    import Navbar from "$lib/waiter/Navbar.svelte";
    import { onMount } from "svelte";
    import { browser } from "$app/environment";
    import Item from "$lib/waiter/Item.svelte";

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        out_of_stock: boolean;
    }

    let filters: {
        name: string;
        starts_from: string;
        handleClick: () => void;
    }[] = []
    let currentFilter: string = 'out of stock'
    $: currentStartsFrom = filters.find(x => x.name == currentFilter)?.starts_from

    let items: Item[] = []

    async function fetchItems() {
        if (!browser) {
            return
        }

        const options = {
            method: 'GET',
            headers: {
                Category: currentFilter,
                Authorization: `Bearer ${localStorage.getItem('waiter-token')}`,
            },
        };

        const result = await fetch('http://localhost:8000/item/filter', options)
        return await result.json()
    }

    function changeFilter(filter: string) {
        currentFilter = filter
        setTimeout(() => {
            fetchItems().then(data => items = data)
        }, 0)
    }

    onMount(async () => {
        const options = {
            method: 'GET',
        };

        const result = await fetch('http://localhost:8000/categories', options)
        const data = await result.json()

        const updateData = data.map((x: {name: string;}) => {
            return {...x, handleClick: () => changeFilter(x.name)}
        })

        filters = [{name: 'out of stock', handleClick: () => changeFilter('out of stock')}, ...updateData]
        setTimeout(() => {
            fetchItems().then(data => items = data)
        }, 0)
    })
</script>

<main>
    <Navbar active="item"/>
    <Filter {filters} {currentFilter}/>

    <section>
        {#if currentFilter != 'out of stock'}
            <h2>{currentFilter}</h2>
            <p>From {currentStartsFrom}</p>
        {/if}

        <ul>
            {#each items as item (item._id)}
                <Item name={item.name} image_url={item.image_url} out_of_stock={item.out_of_stock} />
            {:else}
                <p class="empty">No items</p>
            {/each}
        <ul>
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

    ul {
        list-style: none;
        padding: 0;
        margin: 0;

        display: flex;
        flex-direction: column;
        gap: 1.5em;
    }

    h2 {
        font-size: 2rem;
        font-weight: 700;
        text-transform: capitalize;

        color: #444444;
        margin: 0;
    }    
    
    h2+p {
        font-size: 1rem;
        font-weight: 400;

        color: #565656;
        margin: 0 0 1em;
    }
</style>