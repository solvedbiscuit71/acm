<script lang="ts">
    type Links = "order" | "home" | "cart"

    export let active: Links = "home"

    const redirectUrl = {
        order: "/order",
        home: "/menu",
        cart: "/cart"
    }

    function handleClick(target: Links) {
        if (target == active) {
            return
        }
        console.log(target)
        window.location.replace(redirectUrl[target])
    }
</script>

<footer>
    <div on:mouseup={() => handleClick("order")} class:active={active=="order"} class="order"></div>
    <div on:mouseup={() => handleClick("home")} class:active={active=="home"} class="home"></div>
    <div on:mouseup={() => handleClick("cart")} class:active={active=="cart"} class="cart"></div>
</footer>

<style>
    footer {
        width: 100vw;
        min-height: 64px;
        background-color: #FF9043;

        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 42px;

        position: fixed;
        bottom: 0;
    }

    div {
        width: 40px;
        height: 40px;
        background-color: #FF9043;

        background-repeat: no-repeat;
    } 

    div.active {
        position: relative;
    }

    div.active::after {
        content: "";
        width: 15px;
        height: 5px;

        background-color: white;
        border-radius: 4px;
        position: absolute;
        bottom: -5px;
        left: 50%;
        transform: translateX(-50%);
    }

    .order {
        background-image: url("/icon-order.png");
    }
    .home {
        background-image: url("/icon-home.png");
    }
    .cart {
        background-image: url("/icon-cart.png");
    }

</style>