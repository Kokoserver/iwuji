<script lang="ts">
	import { Next, Previous } from 'flowbite-svelte';
	import { TabWrapper, TabContentItem } from 'flowbite-svelte';
	import { Loading, showStep } from '$root/lib/store/modalStore';
	import type { PageServerData } from './$types';
	import { Cart } from '$root/lib/store/toggleSeriesStore';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import CartList from '$root/lib/components/CartList.svelte';
	import { onMount } from 'svelte';
	import AddressForm from '$root/lib/components/AddressForm.svelte';
	import { page } from '$app/stores';
	import AddressCard from '$root/lib/components/AddressCard.svelte';
	import DefaultMessage from '$root/lib/components/DefaultMessage.svelte';
	import { get_total_price } from '../cart/crud';
	import { create_order } from '../user/order/crud';
	export let data: PageServerData;

	onMount(() => {
		$showStep = 1;
	});
	$: addressList = data.address;
	$: user = data.user;
	$: selected_add = 0;

	const previous = () => {
		if ($showStep > 1) {
			$showStep--;
		}
	};
	const next = () => {
		if ($showStep < 3) {
			$showStep++;
		}
	};
	const handleCreateOrder = async (selected_add: number) => {
		$Loading = true;
		await create_order(selected_add);
		// $Loading = false;
	};
</script>

<Container
	divClass="flex flex-wrap py-20 w-full content-center justify-center h-[30rem] overflow-y-scroll px-10 my-10 shadow-md p-20"
>
	{#if $Cart[0]?.id}
		<TabWrapper class="mb-4" activeTabValue={$showStep}>
			<TabContentItem id={1} activeTabValue={$showStep}>
				{#if addressList[0]?.id}
					<div class=" flex flex-col items-center w-full rounded-lg  p-10 gap-10 mt-5">
						{#each addressList as address}
							<label for="address_card{address.id}" on:click={() => (selected_add = address.id)}>
								<div class="flex items-center w-full rounded-lg  p-10 gap-5 shadow-md">
									<input type="radio" id="address_card{address.id}" name="address_card" />
									<AddressCard {address} {user} url_redirect={String($page.url)} />
								</div>
							</label>
						{/each}
					</div>
				{:else}
					<AddressForm method="POST" redirectTo={String($page.url)} />
				{/if}
			</TabContentItem>
			<TabContentItem id={2} activeTabValue={$showStep}>
				<div>
					<CartList cartStore={Cart} {data} />
				</div>
			</TabContentItem>
			<TabContentItem id={3} activeTabValue={$showStep}>
				{#if selected_add !== 0}
					<div class="flex flex-row justify-center gap-3 items-center">
						<button
							class="btn bg-primary py-3 px-6 rounded-full  font-normal capitalize"
							on:click={() => handleCreateOrder(selected_add)}
							>complete order
						</button>
						<h1 class="font-bold text-2xl">Total: ${get_total_price($Cart)}</h1>
					</div>
				{:else}
					<DefaultMessage message="please select or create shipping address" />
				{/if}
			</TabContentItem>
		</TabWrapper>
	{:else}
		<DefaultMessage message="no items to checkout" />
	{/if}
</Container>
<div class="flex items-center justify-center gap-5">
	<Previous on:previous={previous} icon />
	<Next on:next={next} icon />
</div>
