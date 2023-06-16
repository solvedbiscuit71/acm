<script lang="ts">
    export let filters: {
        name: string;
        handleClick: () => void;
    }[]
    export let currentFilter: string
</script>

<section>
    <ul>
        {#each filters as filter}
            <li class:active="{filter.name == currentFilter}" on:mouseup={filter.handleClick}>{filter.name}</li>
        {/each}
    </ul>
</section>

<style>
    ul {
        list-style: none;
        padding: 1.5em 1em;
        margin: 0;

        display: flex;
        gap: 1.125em;

        align-items: center;
        overflow-x: scroll;
    }

    ul::-webkit-scrollbar {
        display: none;
    }

    li {
        white-space: pre;
        font-size: 0.875rem;
        font-weight: 500;
        color: #57575780;
        text-align: center;
        text-transform: uppercase;

        border: 1.5px solid #57575780;
        border-radius: 6px;

        padding: 0.285em 1em;
    }

    li.active {
        color: #575757;
        border-color: #575757;
    }
</style>