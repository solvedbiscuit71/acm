<svelte:head>
    <title>ACM | Amrita Canteen Management</title>
</svelte:head>

<script>
    import Loader from "$lib/Loader.svelte";
    import { onMount } from "svelte";

    onMount(() => {
        const token = localStorage.getItem("token");
        if (token) {
            // verify token??
            return
        } else {
            // redirect /login
            setInterval(() => {
                window.location.replace("/login")
            }, 1000)
        }
    })
</script>

<main>
    <section>
    <h1>ACM</h1>

    <p>
        <span>Amrita Canteen</span>
        <span>Management</span>
    </p>

    <div>
        <Loader/>
    </div>
    </section>
</main>

<style>
    main {
        background-color: #FD8736;

        width: 100vw;
        height: 100vh;
    }

    section {
        position: relative;
        top: 40%;
        transform: translateY(-50%);
    }

    h1, p {
        text-align: center;

        color: #FFF9F5;
    }

    h1 {
        margin: 0 0 0.375em;

        font-size: 4rem;
    }

    p {
        margin: 0 0 1.18em;
        font-size: 2rem;
        font-weight: 600;
    }

    span {
        display: block;

        margin: 0;
    }

    span:last-of-type {
        transform: translateY(-0.25em);
    }

    div {
        display: flex;
        justify-content: center;
    }
</style>