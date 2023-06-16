<script lang="ts">
    import Toggle from "./Toggle.svelte";

    export let name: string, image_url: string, out_of_stock: boolean = false;
</script>

<li class="item">
    <img src={"http://localhost:8000" + image_url} alt={name}/>

    <div class="info">
        <h1>{name}</h1>
        <Toggle {out_of_stock}/>
    </div>
</li>

<style>
    li.item {
        width: 100%;
        min-height: 150px;

        background-color: white;
        border-top-right-radius: 6px;
        border-top-left-radius: 6px;
        box-shadow: 0px 0px 8px 0px #54545459;

        display: flex;
        gap: 1em;

        padding: 1.125em;
    }

    div.info {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    img {
        max-height: 120px;
        width: 120px;
        border-radius: 4px;
    }

    h1 {
        font-size: 1.375rem;
        font-weight: 700;
        margin: 0;

        color: #444444;
    }
</style>
