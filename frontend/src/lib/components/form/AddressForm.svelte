<script lang="ts">
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import suite from '$root/lib/form/address';
	import type { AddressIn } from '../../interface/address.interface';
	import { notification } from '../../notification';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';
	import { page } from '$app/stores';
	import { status } from '$root/lib/utils/status';
	export let initial_data = {} as AddressIn;
	export let method: 'POST' | 'PUT';
	export let buttonValue: string | undefined = undefined;
	export let redirectTo: string = '/address';
	export let reloadPage = false;

	const formdata = initial_data ?? {};

	let data: { message?: string; error?: string };
	$: error = data?.error;

	async function handleSubmit() {
		const res = await fetch('/api/user/address', {
			method: method,
			body: JSON.stringify(formdata)
		});
		data = await res.json();
		if (res.status === status.HTTP_200_OK) {
			notification.success(data.message ?? 'Address created successfully');
			if (redirectTo && !reloadPage) {
				await goto(redirectTo);
			} else {
				if (browser) {
					location.href = redirectTo;
				}
			}
		}
		if (data.error) {
			notification.danger(data.error);
		}
	}

	let res = suite.get();
	const handleChange = async (event: Event) => {
		const inputField = event.target as HTMLInputElement;
		res = suite(formdata, inputField.name);
	};
</script>

<div class="flex flex-wrap content-center justify-center rounded-l-md ">
	<div class="w-6/12">
		<div class="pb-10">
			<h1 class="text-xl font-semibold capitalize">shipping address</h1>
		</div>

		<form
			class="flex flex-col space-y-6 bg-gray-50 shadow-md p-10"
			on:submit|preventDefault={handleSubmit}
		>
			{#if initial_data && initial_data.id}
				<Input type="text" name="addressId" value={`${initial_data.id ?? ''}`} class="hidden" />
			{/if}

			{#if error}
				<Helper color="red">{error ?? ''}</Helper>
			{/if}
			<Label class="space-y-2">
				<span>Tel</span>
				<Input
					type="tel"
					bind:value={formdata.tel}
					name="tel"
					on:change={handleChange}
					placeholder="+2349071133025"
					required
				/>
				{#if res.getErrors('street')[0]}
					<Helper color="red">{res.getErrors('street') ?? ''}</Helper>
				{/if}
			</Label>
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

			{#if $page.url.searchParams.get('edit')}
				<Button
					type="submit"
					btnClass="bg-secondary px-4 py-2 rounded-full capitalize"
					class="w-full">edit address</Button
				>
			{:else}
				<Button
					type="submit"
					btnClass="bg-secondary px-4 py-2 rounded-full capitalize"
					class="w-full">{buttonValue ?? 'create address'}</Button
				>
			{/if}
		</form>
	</div>
</div>
