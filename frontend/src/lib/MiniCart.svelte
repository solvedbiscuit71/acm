<script lang="ts">
    import Counter from "$lib/Counter.svelte";

    // dummy data!
    let item = { _id: "647d594cbb2ff15f3e46ebd7", name: "Chicken 65", price: 60, image_url: "/image/chicken 65.webp", count: 0 };

    export let hidden: boolean = true
</script>

<section style:display={hidden ? "none": "block"}>
    <div class="item">
        <div class="img">
            <img
                src={"http://localhost:8000" + item.image_url}
                alt={item.name}
            />
        </div>

        <div class="info">
            <div>
                <h1>{item.name}</h1>
                <div>
                    <p>₨ {item.price}</p>
                </div>
            </div>
            <Counter bind:value={item.count} />
        </div>
    </div>
</section>

<style>
    section {
        width: 100vw;
        min-height: calc(100vh - 64px);

        position: fixed;
        top: 0px;

        background-color: #57575759;
    }

    div.item {
        position: absolute;
        bottom: 0;

        width: 100%;
        min-height: 200px;

        background-color: white;
        border-top-right-radius: 6px;
        border-top-left-radius: 6px;
        box-shadow: 0px 0px 8px 0px #54545459;

        display: flex;
        gap: 1em;

        padding: 1.125em;
    }

    div.info {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }

    img {
        max-height: 150px;
        width: 150px;
        border-radius: 8px;
    }

    div.img {
        display: flex;
        flex-direction: column;

        justify-content: center;
    }

    h1 {
        font-size: 1.5rem;
        font-weight: 700;
        margin: 0;

        color: #444444;
    }

    p {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 0.2em 0 0;

        color: #535353;
    }
</style>
