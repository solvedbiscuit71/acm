<svelte:head>
    <title>ACM | Amrita Canteen Management | Login</title>
</svelte:head>

<script>
    import Input from "$lib/Input.svelte";
    import Button from "$lib/Button.svelte";
</script>

<main>
    <h1>ACM</h1>

    <form>
        <Input name="Mobile" type="text" />
        <Input name="Password" type="password" />

        <Button style="align-self: center;">
            Login
        </Button>
    </form>
</main>

<style>
    main {
        height: 100vh;

        background-color: white;
    }

    h1 {
        color: #444444;

        font-size: 4rem;
        margin: 1.3125em 0 0.5em;

        text-align: center;
    }

    form {
        display: flex;
        gap: 1.5em;
        flex-direction: column;

        width: 75%;
        margin: 0 auto;
    }
</style>
