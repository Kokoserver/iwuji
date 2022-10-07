<script lang="ts">
	import CartList from '$root/lib/components/CartList.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import { Cart} from '$root/lib/store/toggleSeriesStore';
	import type { PageServerData } from '.svelte-kit/types/src/routes/cart/$types';
	export let data: PageServerData;
</script>

<Container divClass="mt-20 space-y-20">
	<h1 class="text-center font-bold text-3xl uppercase">Cart</h1>
	{#if $Cart[0]?.id}
		<div class="flex justify-end">
			<a href="/checkout" class="rounded-full font-semibold bg-primary px-5 py-3 capitalize"
				>Checkout</a
			>
		</div>
	{/if}
	<CartList cartStore={Cart} {data} />
</Container>
