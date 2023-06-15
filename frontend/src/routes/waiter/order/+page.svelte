<svelte:head>
    <title>ACM | Amrita Canteen Management | Order</title>
</svelte:head>

<script lang="ts">
    import Filter from "$lib/waiter/Filter.svelte";
    import Navbar from "$lib/waiter/Navbar.svelte";
</script>

<main>
    <Navbar/>

    <Filter/>
</main>

<style>
    main {
        min-height: 100vh;
    }
</style>