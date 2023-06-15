<script lang="ts">
    export let value = 0
</script>

<div>
    <img src="/icon-minus.png" alt="minus" on:mouseup={() => value = value > 0 ? value - 1 : value}>
    <span>{value}</span>
    <img src="/icon-plus.png" alt="plus" on:mouseup={() => value = value + 1}>
</div>

<style>
    img {
        width: 32px;
    }

    div {
        display: flex;
        align-items: center;
        gap: 1em;
    }

    span {
        font-size: 1.25rem;
        font-weight: 700;
        color: white;

        background-color: #FF9043;
        border-radius: 4px;
        padding: 0.1em 0.5em;
    }
</style>