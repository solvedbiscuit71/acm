<script lang="ts">
    export let name : string
    export let type: "text" | "password" = "text"

    export let value : string;
    let ref : HTMLInputElement
</script>

<label for="input-{name.toLowerCase()}">
    <span>{name.toUpperCase()}</span>
    <input id="name" name="{name.toLowerCase()}" {type} on:input={() => value = ref.value}  bind:this={ref}>
</label>

<style>
    label {
        display: flex;
        flex-direction: column;
    }

    span {
        font-size: 1.5rem;
        font-weight: 500;
        color: #565656;
    }

    input {
        color: #565656;
        border: none;
        border-bottom: 2px solid #FF9043;

        background-color: #FFF4EC;

        font-size: 1.5rem;
        padding: 0.2em;
    }

    input:focus {
        outline: none;
    }
</style>

