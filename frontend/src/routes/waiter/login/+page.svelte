<svelte:head>
    <title>ACM | Amrita Canteen Management | Login</title>
</svelte:head>

<script lang="ts">
    import Input from "$lib/Input.svelte";
    import Button from "$lib/Button.svelte";

    let password: string = ''
    let token: string | null = null

    async function handleSubmit() {
        const options = {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: `{"password":"${password}"}`
        };

        const result = await fetch('http://localhost:8000/waiter/token', options)
        const data = await result.json()
        switch (result.status) {
            case 200:
                token = data["access_token"]
                break
            case 401:
                alert("invalid password")
                break
            default:
                alert("unhandled error occured");
        }
    }

    $: if (token) {
        localStorage.setItem("waiter-token", token)
        window.location.replace("/waiter")
    }
</script>

<main>
    <section>
    <h1>ACM</h1>
    <p>waiter's portal</p>

    <form on:submit|preventDefault={handleSubmit}>
    <Input name="password" type="password" bind:value={password}/>
    <Button style="align-self: center;">
        Login
    </Button>
    </form>
    </section>
</main>

<style>
    main {
        min-height: 100vh;
    }

    section {
        position: relative;
        top: 20vh;
    }

    h1, p {
        text-align: center;
    }

    h1 {
        font-size: 4rem;
        font-weight: 700;

        color: #444444;

        margin: 0;
        text-align: center;
    }

    p {
        font-size: 2rem;
        font-weight: 600;

        color: #535353;

        margin: 0 0 0.875em;
        transform: translateY(-0.75em);
    }

    form {
        display: flex;
        flex-direction: column;
        gap: 2em;

        width: 75%;
        margin: 0 auto;
    }
</style>