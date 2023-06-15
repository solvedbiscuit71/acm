<script lang="ts">
    type FilterType = 'placed' | 'preparing' | 'ready' | 'served'

    export let filter: FilterType
</script>

<section>
    <ul>
        <li class:active="{filter == "placed"}" on:mouseup={() => filter = "placed"}>New orders</li>
        <li class:active="{filter == "preparing"}" on:mouseup={() => filter = "preparing"}>Preparing</li>
        <li class:active="{filter == "ready"}" on:mouseup={() => filter = "ready"}>Ready</li>
        <li class:active="{filter == "served"}" on:mouseup={() => filter = "served"}>Served</li>
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
        flex-grow: 1;
    }

    li.active {
        color: #575757;
        border-color: #575757;
    }


</style>