<script lang="ts">
	import { Button, Helper, Input, Label } from 'flowbite-svelte';
	import suite from '$root/routes/user/address/form';
	import type { AddressIn } from '../interface/address.interface';
	import { notification } from '../notification';
	import { goto } from '$app/navigation';
	import { browser } from '$app/environment';

	export let initial_data: AddressIn = {} as AddressIn;
	export let method: 'POST' | 'PUT';
	export let buttonValue: string | undefined = undefined;
	export let redirectTo: string = '/user/address';
	export let reloadPage = false;

	const formdata = {} as AddressIn;
	if (initial_data.id !== undefined) {
		formdata.id = initial_data.id;
		formdata.city = initial_data.city;
		formdata.tel = initial_data.tel;
		formdata.street = initial_data.street;
		formdata.zipcode = initial_data.zipcode;
		formdata.state = initial_data.state;
		formdata.country = initial_data.country;
	}
	let data: { message?: string; error?: string };
	$: error = data?.error;

	async function handleSubmit() {
		const res = await fetch('/user/address/api', {
			method: method,
			body: JSON.stringify(formdata)
		});
		data = await res.json();
		if (data.message) {
			notification.success(data.message);
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

<div class="flex shadow-md">
	<div class="flex flex-wrap content-center justify-center rounded-l-md bg-white p-10">
		<div class="w-72">
			<div class="pb-10">
				<h1 class="text-xl font-semibold capitalize">shipping address</h1>
			</div>

			<form class="flex flex-col space-y-6" on:submit|preventDefault={handleSubmit}>
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

				<Button
					type="submit"
					btnClass="bg-secondary px-4 py-2 rounded-full capitalize"
					class="w-full">{buttonValue ?? 'create address'}</Button
				>
			</form>
		</div>
	</div>
</div>
