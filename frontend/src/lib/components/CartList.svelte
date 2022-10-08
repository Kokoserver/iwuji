<script lang="ts">
	import type { CartIn, CartUpdateOut } from '$root/lib/interface/cart.interface';
	import type { Writable } from 'svelte/store';
	import { handleRemoveFromCart, handleUpdateCart } from '$root/routes/shop/crud';
	import DefaultMessage from './DefaultMessage.svelte';
	import CartItemCard from './CartItemCard.svelte';
	export let data: { carts: CartIn[] };
	export let cartStore: Writable<CartIn[]>;

	const handleUpdate = async (
		cartItemObj: CartIn,
		type: 'hard_back' | 'paper_back' | 'pdf',
		direction: 'up' | 'down'
	) => {
		if (type === 'pdf') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj) {
					item.pdf = !cartItemObj.pdf;
					return item;
				}
				return item;
			});
		}
		if (type === 'hard_back' && direction == 'up') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.hard_back_qty < 41) {
					item.hard_back_qty++;
					return item;
				}
				return item;
			});
		}
		if (type === 'hard_back' && direction == 'down') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.hard_back_qty != 0) {
					item.hard_back_qty--;
					return item;
				}
				return item;
			});
		}
		if (type === 'paper_back' && direction == 'up') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.paper_back_qty <= 40) {
					item.paper_back_qty++;
					return item;
				}
				return item;
			});
		}
		if (type === 'paper_back' && direction == 'down') {
			$cartStore = $cartStore.map((item) => {
				if (item === cartItemObj && item.paper_back_qty !== 0) {
					item.paper_back_qty--;
					return item;
				}
				return item;
			});
		}
		if (data.carts !== $cartStore) {
			const to_update: CartUpdateOut = {
				cartId: cartItemObj.id,
				pdf: cartItemObj.pdf,
				paper_back_qty: cartItemObj.paper_back_qty,
				hard_back_qty: cartItemObj.hard_back_qty
			};

			setTimeout(async () => {
				await handleUpdateCart(to_update);
			}, 5000);
		}
	};
</script>

{#if $cartStore[0]?.id}
	{#each $cartStore as item}
		<CartItemCard {item} {handleRemoveFromCart} {handleUpdate} />
	{/each}
{:else}
	<h1 class="h-screen">
		<DefaultMessage message="Cart is empty" />
	</h1>
{/if}
