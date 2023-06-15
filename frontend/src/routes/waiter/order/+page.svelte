<svelte:head>
    <title>ACM | Amrita Canteen Management | Order</title>
</svelte:head>

<script lang="ts">
    import Filter from "$lib/waiter/Filter.svelte";
    import Navbar from "$lib/waiter/Navbar.svelte";

    type FilterType = 'new order' | 'preparing' | 'ready' | 'served'

    let filter: FilterType = 'new order'
</script>

<main>
    <Navbar/>

    <Filter bind:filter />
</main>

<style>
    main {
        min-height: 100vh;
    }
</style>