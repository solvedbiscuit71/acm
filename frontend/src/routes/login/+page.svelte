<svelte:head>
    <title>ACM | Amrita Canteen Management | Login</title>
</svelte:head>

<script lang="ts">
    import Input from "$lib/Input.svelte";
    import Button from "$lib/Button.svelte";

    interface User {
        id: string;
        mobile: string;
        password: string;
        name: string;
    }

    let user : User = {
        id: '',
        mobile: '',
        password: '',
        name: ''
    }
</script>

<main>
    <h1>ACM</h1>

    <form>
        <Input name="Mobile" type="text" bind:value={user.mobile} />
        <Input name="Password" type="password" bind:value={user.password} />

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
