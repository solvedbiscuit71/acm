<script lang="ts">
    export let imageUrl: string, textContent: string;
</script>

<button on:click>
    <img src="{imageUrl}" alt="Tick icon">
    Mark as {textContent}
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

