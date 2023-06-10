<script lang="ts">
    interface PaymentMethod {
        showLabel: boolean;
        name: string;
        iconUrl: string;
        handler: () => void;
    }

    export let paymentMethods: PaymentMethod[]

</script>

<section>
    <h1>Payment</h1>

    <div class="payment-options">
        {#each paymentMethods as payment (payment.name)}
            <div on:mouseup={payment.handler}>
                <img src="{payment.iconUrl}" alt="{payment.name}">
                {#if payment.showLabel}
                    <span>{payment.name}</span>
                {/if}
            </div> 
        {/each}

    </div>
</section>

<style>
    section {
        padding: 2rem;
    }

    h1 {
        margin: 0 0 0.5em;
        font-size: 3rem;
        font-weight: 700;

        color: #323232;
    }

    div.payment-options {
        display: grid;
        grid-template-columns: 1fr 1fr;

        gap: 1.5em 1em;
    }

    div.payment-options > div {
        display: flex;
        width: 130px;
        height: 130px;
        padding: 1.5em;

        border-radius: 0.5em;
        box-shadow: 0px 2px 4px 0px #0000003c;

        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 0.5em;
    }

    div.payment-options > div span {
        color: #444444;
        font-size: 1.25rem;
        font-weight: 600;

        text-align: center;
        display: block;

        line-height: 1em;
    }
</style>