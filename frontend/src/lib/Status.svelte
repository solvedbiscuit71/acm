<script lang="ts">
    type OrderStatus = "placed" | "preparing" | "ready" | "served";

    const colorMap = {
        "placed": "#FFCF44",
        "preparing": "#FD8736",
        "ready": "#68BE61",
        "served": "#BD68FF",
    }

    export let status: OrderStatus
</script>

<div class="status" style:color="{colorMap[status]}" style:border-color="{colorMap[status]}">{status}</div>

<style>
    .status {
        border-width: 1px;
        border-style: solid;
        border-radius: 4px;
        padding: 0.25em 0.5em;

        text-transform: capitalize;
        font-size: 0.875rem;
        font-weight: 600;
    }
</style>