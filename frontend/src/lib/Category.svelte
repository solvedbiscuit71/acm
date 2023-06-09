<script lang="ts">
    import Item from "$lib/Item.svelte";

    const backend_url = "http://localhost:8000"

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        category: string
    }

    export let name: string, starts_from: string, items: Item[];
    export let handleSelect: (item: Item) => void;

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
            <Item on:mouseup={() => handleSelect(item)} name="{item.name}" image_url="{backend_url}{item.image_url}" price="{item.price}"/>
        {/each}
    </div>
</section>

<style>
    .category-header {
        margin-bottom: 0.5em;
    }

    .category-header h2 {
        font-size: 2rem;
        font-weight: 700;
        text-transform: capitalize;

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