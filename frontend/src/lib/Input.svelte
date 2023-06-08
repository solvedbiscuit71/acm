<script lang="ts">
    export let name: string;
    export let type: "text" | "password" = "text";
    export let placeHolder: string = "";
    export let nolabel: boolean = false;

    export let value: string;
    let ref: HTMLInputElement;
</script>

<label for="input-{name.toLowerCase()}">
    <span style:display={nolabel ? "none" : "inline"}>{name.toUpperCase()}</span
    >
    <input
        placeholder="{placeHolder}"
        id={name.toLowerCase()}
        name={name.toLowerCase()}
        {type}
        on:input={() => (value = ref.value)}
        bind:this={ref}
        
    />
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
        border-bottom: 2px solid #ff9043;

        background-color: #fff4ec;

        font-size: 1.5rem;
        font-weight: 500;
        padding: 0.2em;
    }

    input::placeholder {
        color: #ff9142b3;
    }

    input:focus {
        outline: none;
    }
</style>
