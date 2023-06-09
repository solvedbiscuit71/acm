<svelte:head>
    <title>ACM | Amrita Canteen Management | Menu</title>
</svelte:head>

<script lang="ts">
    import Category from "$lib/Category.svelte";
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";
    import { onMount } from "svelte";

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        category: string
    }

    interface Category {
        _id: string;
        starts_from: string;
        items: Item[]
    }

    const backend_url = "http://localhost:8000"
    let categories: Category[] | null = null

    onMount(async () => {
        const result = await fetch(backend_url + "/menu")
        switch (result.status) {
            case 200:
                const data = await result.json()
                categories = data;
                break
            default:
                alert("unhandled error occured")
        }

        return
    })

    $: console.log(categories)
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
            {#each categories as category}
                <Category name="{category._id}" starts_from="{category.starts_from}" items={category.items} />
            {/each}
        {/if}
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
