<script lang="ts">
    export let name: string, image_url: string;
</script>

<li class="item">
    <img src={"http://localhost:8000" + image_url} alt={name}/>

    <div class="info">
        <h1>{name}</h1>

        <div class="toggle-button">
            <div class="toggle"></div>
            <span>Item available</span>
        </div>
    </div>
</li>

<style>
    li.item {
        width: 100%;
        min-height: 150px;

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
        max-height: 120px;
        width: 120px;
        border-radius: 4px;
    }

    h1 {
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0;

        color: #444444;
    }

    .toggle-button {
        align-self: flex-end;

        display: flex;
        flex-direction: column;
        align-items: flex-end;

        gap: 0.3125em;
    }

    .toggle-button span {
        font-size: 0.65rem;
        font-weight: 500;

        color: #666867;
    }

    .toggle {
        width: 2.875em;
        min-height: 1.375em;

        background-color: #68BE61;
        border-radius: 1em;

        position: relative;
    }

    .toggle::after {
        content: "";
        display: block;

        border: 0.5em solid white;
        border-radius: 50%;

        position: absolute;
        top: 12%;
        right: 8%;
    }
</style>
