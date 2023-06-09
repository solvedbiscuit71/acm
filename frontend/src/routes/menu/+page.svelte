<script lang="ts">
    import Footer from "$lib/Footer.svelte";
    import MiniCart from "$lib/MiniCart.svelte";

    // dummy data
    const items = [ {
            _id: "6482d2bb43e45c9542807219",
            name: "Plain Dosa",
            price: 50,
            image_url: "/image/plain dosa.jpg",
            category: "breakfast",
        },
        {
            _id: "6482d2bb43e45c954280721a",
            name: "Podi Dosa",
            price: 60,
            image_url: "/image/podi dosa.jpg",
            category: "breakfast",
        },
        {
            _id: "6482d2bb43e45c954280721b",
            name: "Ghee Dosa",
            price: 60,
            image_url: "/image/ghee dosa.jpg",
            category: "breakfast",
        },
        {
            _id: "6482d2bb43e45c954280721c",
            name: "Egg Dosa",
            price: 60,
            image_url: "/image/egg dosa.jpg",
            category: "breakfast",
        },
        {
            _id: "6482d2bb43e45c954280721d",
            name: "Masala Dosa",
            price: 60,
            image_url: "/image/masala dosa.jpg",
            category: "breakfast",
        },
        {
            _id: "6482d2bb43e45c9542807220",
            name: "Chapati",
            price: 40,
            image_url: "/image/chapati.jpg",
            category: "breakfast",
        },
    ];
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
        {#each [0,1,2] as _}
            
        <section class="category">
            <div class="category-header">
                <h2>Breakfast</h2>
                <div>
                    <span>From 8:30 am</span>
                    <button>show</button>
                </div>
            </div>

            <div class="item-container">
                {#each items as item (item._id)}
                    <div class="item">
                        <img src="http://localhost:8000{item.image_url}" alt="{item.name}">
                        <div>
                            <h3>{item.name}</h3>
                            <p>₨ {item.price}</p>
                        </div>
                    </div>
                {/each}
            </div>
        </section>

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

    .category-container {
        display: flex;
        flex-direction: column;

        gap: 2.5em;
    }

    .category-header {
        margin-bottom: 0.5em;
    }

    .category-header h2 {
        font-size: 1.5rem;
        font-weight: 600;

        color: #444444;
        margin: 0;
    }

    .category-header h2+div {
        display: flex;
        justify-content: space-between;

        padding-right: 1.5em;
    }

    .category-header h2+div span {
        font-size: 1rem;
        font-weight: 400;

        color: #565656;
    }

    .category-header button {
        border: none;
        background-color: white;

        font-size: 1rem;
        font-weight: 500;
        
        color: #444444;
    }

    .item-container {
        padding: 0.5em 1em 0.5em 0.5em;
        width: 100%;
        display: flex;
        gap: 1.5em;

        justify-content: flex-start;
        align-items: center;

        overflow: scroll;
    }

    .item-container::-webkit-scrollbar {
        display: none;
    }

    .item {
        display: flex;
        flex-direction: column;

        gap: 0.5em;
        padding: 0.5em;

        border-radius: 4px;
        box-shadow: 0px 2px 4px 0px #0000003c;
        width: min-content;
    }

    .item img {
        width: 120px;
        height: 120px;

        border-radius: 4px;
    }

    .item h3, .item p {
        margin: 0;
    }

    .item h3 {
        font-size: 100%;
        color: #444444;
    }

    .item p {
        font-size: 0.75rem;
        font-weight: 600;
        color: #565656;
    }
</style>
