<script lang="ts">
    import Input from "$lib/Input.svelte";
    import Button from "$lib/Button.svelte";

    interface User {
        id: string;
        mobile: string;
        password: string;
        name: string;
    }

    interface UserCreate {
        mobile: string;
        password: string;
    }

    let user: User = {
        id: "",
        mobile: "",
        password: "",
        name: "",
    };

    async function handleSubmit() {
        if (!/^[0-9]{10}$/.test(user.mobile)) {
            alert("invalid mobile number")
            return
        }

        if (user.password.length < 8) {
            alert("password must be atleast 8 characters")
            return
        }

        let payload: UserCreate = {
            mobile: user.mobile,
            password: user.password,
        };
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
        };

        let result = await fetch("http://localhost:8000/user", options)
        let data = await result.json()

        switch (result.status) {
            case 200:
                user.id = data["_id"]
                break
            case 409:
                alert(data["detail"])
                break
        }
    }
</script>

<svelte:head>
    <title>ACM | Amrita Canteen Management | Login</title>
</svelte:head>

<main>
    <h1>ACM</h1>

    {#if user.id}
        <div></div>
    {:else}
        <form on:submit|preventDefault={handleSubmit}>
            <Input name="Mobile" type="text" bind:value={user.mobile} />
            <Input name="Password" type="password" bind:value={user.password} />

            <Button style="align-self: center;">Login</Button>
        </form>
    {/if}
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
