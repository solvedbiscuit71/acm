<script lang="ts">
    import Category from "$lib/Category.svelte";
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";
</script>

<svelte:head>
    <title>ACM | Amrita Canteen Management | Menu</title>
</svelte:head>

<main>
    <section class="heading">
        <h1>
            <span>Welcome</span>
            <span>back!</span>
        </h1>
    </section>

    <section class="category-container">
        <!-- dummy loop -->
        {#each [0,0,0] as _}
            <Category name="Breakfast" starts_from="8:30 am" />
        {/each}
    </section>

    <MiniCart />
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
