<script lang="ts">
	import { page } from '$app/stores';
	import CartList from '$root/lib/components/CartList.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import SectionTitle from '$root/lib/components/SectionTitle.svelte';
	import { Cart } from '$root/lib/store/toggleSeriesStore';
</script>

<Container divClass="mt-20 space-y-20">
	<SectionTitle title="Cart" />
	{#if $Cart[0]?.id}
		<div class="flex justify-end">
			<a href="/checkout" class="rounded-full font-semibold bg-primary px-5 py-3 capitalize"
				>Checkout</a
			>
		</div>
	{/if}
	<CartList cartStore={Cart} data={$page.data.carts} />
</Container>
