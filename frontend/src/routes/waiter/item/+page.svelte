<svelte:head>
    <title>ACM | Waiter | Item</title>
</svelte:head>

<script lang="ts">
    import Filter from "$lib/waiter/Filter.svelte";
    import Navbar from "$lib/waiter/Navbar.svelte";
    import { onMount } from "svelte";

    let filters: {
        name: string;
        handleClick: () => void;
    }[] = []
    let currentFilter: string = 'out of stock'

    function changeFilter(filter: string) {
        currentFilter = filter
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
    })
</script>

<main>
    <Navbar active="item"/>
    <Filter {filters} {currentFilter}/>
</main>