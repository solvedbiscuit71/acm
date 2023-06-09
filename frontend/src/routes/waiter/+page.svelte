<svelte:head>
    <title>ACM | Amrita Canteen Management | Waiter</title>
</svelte:head>

<script lang="ts">
    import Loader from "$lib/Loader.svelte";
    import { onMount } from "svelte";

    async function verifyToken(token: string) {
        const options = {
            method: 'GET',
            headers: {
                Authorization: `Bearer ${token}`,
            }
        };

        const result = await fetch('http://localhost:8000/waiter/token', options)
        return result.status
    }

    function redirect() {
        setInterval(() => {
            window.location.replace("/waiter/login")
        }, 1000)
    }

    onMount(async () => {
        const token = localStorage.getItem("waiter-token");
        if (token) {
            const status = await verifyToken(token)
            switch (status) {
                case 200:
                    break
                default:
                    redirect()
            }
            return
        } else {
            redirect()
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
        background-image: url('/bg-top.png'), url('/bg-bottom.png');
        background-repeat: no-repeat;
        background-position: 0 0, 100% 100%;

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