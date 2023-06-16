<script lang="ts">
    import Item from "$lib/Item.svelte";

    interface Item {
        _id: number;
        name: string;
        price: number;
        image_url: string;
        out_of_stock: boolean;
    }

    export let _id: string,
               starts_from: string,
               available: boolean,
               items: Item[];
    export let handleSelect: (item: Item) => void;
</script>

<section class="category">
    <div class="category-header">
        <h2>{_id}</h2>
        <div>
            <span>From {starts_from}</span>
            <button>show</button>
        </div>
    </div>

    <div class="item-container">
        {#each items as item (item._id)}
            <Item
                categoryAvailable={available}
                handleClick={() => handleSelect(item)}
                name={item.name}
                price={item.price}
                image_url={item.image_url}
                out_of_stock={item.out_of_stock}
            />
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
        align-items: stretch;

        overflow: scroll;
    }

    .item-container::-webkit-scrollbar {
        display: none;
    }
</style>