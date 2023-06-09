<script lang="ts">
    export let name: string, price: number, image_url: string;
</script>

<div class="item">
    <img src="{image_url}" alt="{name}">
    <div>
        <h3>{name}</h3>
        <p>₨ {price}</p>
    </div>
</div>

<style>
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