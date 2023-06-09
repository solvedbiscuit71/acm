<script lang="ts">
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";
</script>

<svelte:head>
    <title>ACM | Amrita Canteen Management | Menu</title>
</svelte:head>

<main>
    <MiniCart/>
    <Footer active="home" />
</main>
