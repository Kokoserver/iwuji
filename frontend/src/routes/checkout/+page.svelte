<script lang="ts">
	import { Next, Previous, Card, Checkbox, Button, Label, Helper, Input } from 'flowbite-svelte';

	import { showStep } from '$root/lib/store/modalStore';
	import type { PageServerData } from './$types';
	import { Cart } from '$root/lib/store/toggleSeriesStore';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import { enhance } from '$app/forms';
	import suite from './form';
	import type { AddressOut } from '$root/lib/interface/address.interface';
	import CartList from '$root/lib/components/CartList.svelte';
	import { onMount } from 'svelte';
	export let data: PageServerData;
	onMount(() => {
		$showStep = 1;
	});
	$: addressList = data.address;
	$: user = data.user;

	const formdata = {} as AddressOut;
	let res = suite.get();
	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		res = suite(formdata, inputField.name);
	};

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
</script>

<Container divClass="flex flex-wrap py-20 w-full content-center justify-center">
	{#if $Cart[0]?.id}
		<div class="flex flex-col items-center gap-20">
			<div>
				{#if $showStep === 1}
					{#if addressList[0]?.id}
						<ul
							class="items-center w-full rounded-lg border border-gray-200 sm:flex dark:bg-gray-800 dark:border-gray-600 divide-x divide-gray-200 dark:divide-gray-600"
						>
							{#each addressList as address}
								<li class="w-full">
									<Card href="/user/address/{address.id}">
										<Checkbox class="p-3"
											><div class="space-y-2">
												<h1 class="font-bold capitalize">{user.firstname} {user.lastname}</h1>
												<p>{user.email}</p>
												<p class="font-semibold">
													{address.street}, {address.city}, {address.state}, {address.country}, {address.zipcode}
												</p>
											</div></Checkbox
										>
									</Card>
								</li>
							{/each}
						</ul>
					{:else}
						<div class="flex shadow-md">
							<div class="flex flex-wrap content-center justify-center rounded-l-md bg-white p-10">
								<div class="w-72">
									<div class="pb-10">
										<h1 class="text-xl font-semibold capitalize">create shipping address</h1>
									</div>

									<form class="flex flex-col space-y-6" method="post" use:enhance>
										<Label class="space-y-2">
											<span>Street</span>
											<Input
												type="text"
												bind:value={formdata.street}
												name="street"
												on:change={handleChange}
												placeholder="No 12, adelabu"
												required
											/>
											{#if res.getErrors('street')[0]}
												<Helper color="red">{res.getErrors('street') ?? ''}</Helper>
											{/if}
										</Label>
										<Label class="space-y-2">
											<span>City</span>
											<Input
												type="text"
												on:change={handleChange}
												name="city"
												bind:value={formdata.city}
												placeholder="surulere"
												required
											/>
											{#if res.getErrors('city')[0]}
												<Helper color="red">{res.getErrors('city')[0] ?? ''}</Helper>
											{/if}
										</Label>
										<Label class="space-y-2">
											<span>State</span>
											<Input
												type="text"
												on:change={handleChange}
												name="state"
												bind:value={formdata.state}
												placeholder="lagos"
												required
											/>
											{#if res.getErrors('state')[0]}
												<Helper color="red">{res.getErrors('state')[0] ?? ''}</Helper>
											{/if}
										</Label>
										<Label class="space-y-2">
											<span>Country</span>
											<Input
												type="text"
												on:change={handleChange}
												name="country"
												bind:value={formdata.country}
												placeholder="Nigeria"
												required
											/>
											{#if res.getErrors('country')[0]}
												<Helper color="red">{res.getErrors('country')[0] ?? ''}</Helper>
											{/if}
										</Label>
										<Label class="space-y-2">
											<span>zipcode</span>
											<Input
												type="text"
												on:change={handleChange}
												name="zipcode"
												bind:value={formdata.zipcode}
												placeholder="10112"
												required
											/>
											{#if res.getErrors('zipcode')[0]}
												<Helper color="red">{res.getErrors('zipcode')[0] ?? ''}</Helper>
											{/if}
										</Label>

										<Button
											disabled={!res.valid}
											type="submit"
											btnClass="bg-secondary px-4 py-2 rounded-full"
											class="w-full">Create Address</Button
										>
									</form>
								</div>
							</div>
						</div>
					{/if}
				{:else if $showStep === 2}
					<div class="h-[40rem] overflow-y-scroll px-10">
						<CartList cartStore={Cart} {data} />
					</div>
				{:else if $showStep === 3}
					<h1>complete other and redirect back to home page</h1>
				{/if}
			</div>
			<div>
				<Previous on:previous={previous} />
				<Next on:next={next} />
			</div>
		</div>
	{:else}
		<p>no items to checkout</p>
	{/if}
</Container>
