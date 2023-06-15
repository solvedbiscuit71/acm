<nav>
    <ul>
        <li class="active">Orders</li>
        <li class="divider"></li>
        <li>Items</li>
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

        color: #ffffff59;
    }

    li.active {
        color: white;
    }

    li:not(.divider) {
        flex-grow: 1;
        text-align: center;
    }

    li.divider {
        border: 1.5px solid #ffffff80;
        border-radius: 8px;
        min-height: 50px;
        width: 0;
    }
</style>