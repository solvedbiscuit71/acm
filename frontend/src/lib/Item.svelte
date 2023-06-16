<script lang="ts">
    const backend_url = "http://localhost:8000"
    
    export let name: string, price: number, image_url: string, out_of_stock: boolean;
    export let categoryAvailable: boolean = true
    export let handleClick: () => void

    $: available = categoryAvailable && !out_of_stock
    $: message = out_of_stock ? "Out of stock" : "Not available"
</script>

<div class:available class="item" on:mouseup={() => available && handleClick()}>
    <div class="photo">
        <img src="{backend_url + image_url}" alt="{name}">
        <span class="alert">{message}</span>
    </div>
    <div>
        <h3>{name}</h3>
        <p>₨ {price}</p>
    </div>
</div>

<style>
    .item {
        display: flex;
        flex-direction: column;

        gap: 0.675em;
        padding: 0.675em;

        border-radius: 4px;
        box-shadow: 0px 2px 4px 0px #0000003c;

    }

    .photo {
        position: relative;
    }

    .alert {
        position: absolute;

        color: #FF5252;
        top: 50%;
        left: 50%;

        width: max-content;
        transform: translate(-50%, -50%) rotate(-35deg);

        font-size: 1.25rem;
        font-weight: 600;

        display: none;
    }

    .item:not(.available) .alert {
        display: inline;
    }

    .item img {
        width: 180px;
        height: 180px;

        border-radius: 4px;
        filter: grayscale(1);

        z-index: -1;
    }

    .item.available img {
        filter: none;
    }


    .item h3, .item p {
        margin: 0;
    }

    .item h3 {
        font-size: 1.125rem;
        color: #444444;
    }

    .item p {
        font-size: 1rem;
        font-weight: 500;
        color: #565656;
    }
</style>