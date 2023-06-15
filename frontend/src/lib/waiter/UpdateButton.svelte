<script lang="ts">
    type FilterType = 'placed' | 'preparing' | 'ready'

    const filterInfo = {
        placed: {
            imageUrl: "/icon-orange-tick.png",
            textContent: "Mark as Preparing",
        },
        preparing: {
            imageUrl: "/icon-green-tick.png",
            textContent: "Mark as Ready",
        },
        ready: {
            imageUrl: "/icon-purple-tick.png",
            textContent: "Mark as Served",
        },
    }

    export let filter: FilterType
</script>

<button on:click>
    <img src="{filterInfo[filter].imageUrl}" alt="Tick icon">
    {filterInfo[filter].textContent}
</button>

<style>
    button {
        width: 100%;

        font-size: 0.875rem;
        font-weight: 600;

        color: #323232;
        padding: 0.6em;

        background-color: white;
        border: 1px solid #5B5B5B;
        box-shadow: 0px 2px 4px #00000026;
        border-radius: 4px;

        text-align: center;
        text-transform: uppercase;

        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75em;
    }
</style>

