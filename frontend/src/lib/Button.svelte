<script lang="ts">
    export let type : "submit" | "reset" = "submit"
    export let style: string = ""
</script>

<button on:click type="{type}" style="{style}">
    <slot></slot>
</button>

<style>
    button {
        font-size: 2rem;
        font-weight: 600;

        background-color: #FF9043;
        color: white;
        border: none;
        border-radius: 0.33em;
        padding: 0.15em 0.8em;
    }
</style>