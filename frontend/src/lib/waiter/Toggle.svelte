<script lang="ts">
    export let out_of_stock = false
</script>

<div class="toggle-button">
    <button on:click class="toggle" class:off={out_of_stock}></button>
    <span>Item {out_of_stock ? "unavailable" : "available"}</span>
</div>

<style>
    .toggle-button {
        align-self: flex-end;

        display: flex;
        flex-direction: column;
        align-items: flex-end;

        gap: 0.3125em;
    }

    .toggle-button span {
        font-size: 0.65rem;
        font-weight: 500;

        color: #666867;
    }

    .toggle {
        width: 2.875em;
        min-height: 1.375em;

        background-color: #68BE61;
        border: none;
        border-radius: 1em;

        position: relative;
    }

    .toggle.off {
        background-color: #FF5252;
    }

    .toggle.off::after {
        left: 8%;
        right: unset;
    }

    .toggle::after {
        content: "";
        display: block;

        border: 0.5em solid white;
        border-radius: 50%;

        position: absolute;
        top: 12%;
        right: 8%;
    }
</style>