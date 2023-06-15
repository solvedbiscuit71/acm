<script lang="ts">
    type Links = "order" | "item"

    export let active: Links = "order"

    const redirectUrl = {
        order: "/waiter/order",
        item: "/waiter/item",
    }

    function handleClick(target: Links) {
        if (target == active) {
            return
        }
        console.log(target)
        window.location.replace(redirectUrl[target])
    }
</script>

<nav>
    <ul>
        <li on:mouseup={() => handleClick("order")} class:active="{active == "order"}">Orders</li>
        <li class="divider"></li>
        <li on:mouseup={() => handleClick("item")} class:active="{active == "item"}">Items</li>
    </ul>
</nav>

<style>
    nav {
        background-color: #FD8736;
        min-height: 82px;

        padding: 1em 0em;
    }

    ul {
        list-style: none;
        padding: 0;
        margin: 0;

        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    li {
        font-size: 1.25rem;
        font-weight: 600;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 0.04em;

        color: #ffffff59;
    }

    li.active {
        color: white;
    }

    li:not(.divider) {
        flex-grow: 1;
    }

    li.divider {
        border: 1.5px solid #ffffff80;
        border-radius: 8px;
        min-height: 50px;
        width: 0;
    }
</style>