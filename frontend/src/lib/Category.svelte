<script lang="ts">
    import Item from "$lib/Item.svelte";

    // dummy data
    const items = [{
            _id: "6482d2bb43e45c9542807219",
            name: "Plain Dosa",
            price: 50,
            image_url: "/image/plain dosa.jpg",
        },
        {
            _id: "6482d2bb43e45c954280721a",
            name: "Podi Dosa",
            price: 60,
            image_url: "/image/podi dosa.jpg",
        },
        {
            _id: "6482d2bb43e45c954280721b",
            name: "Ghee Dosa",
            price: 60,
            image_url: "/image/ghee dosa.jpg",
        },
        {
            _id: "6482d2bb43e45c954280721c",
            name: "Egg Dosa",
            price: 60,
            image_url: "/image/egg dosa.jpg",
        },
        {
            _id: "6482d2bb43e45c954280721d",
            name: "Masala Dosa",
            price: 60,
            image_url: "/image/masala dosa.jpg",
        },
        {
            _id: "6482d2bb43e45c9542807220",
            name: "Chapati",
            price: 40,
            image_url: "/image/chapati.jpg",
        },
    ];

    export let name: string, starts_from: string;
</script>

<section class="category">
    <div class="category-header">
        <h2>{name}</h2>
        <div>
            <span>From {starts_from}</span>
            <button>show</button>
        </div>
    </div>

    <div class="item-container">
        {#each items as item (item._id)}
            <Item name="{item.name}" image_url="http://localhost:8000{item.image_url}" price="{item.price}"/>
        {/each}
    </div>
</section>

<style>
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
</style>