<script lang="ts">
	import AddressForm from '$root/lib/components/form/AddressForm.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import type { AddressIn } from '$root/lib/interface/address.interface';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	$: signal = data.signal;
	$: redirectTo = data.redirectTo;
	$: address = data.address as AddressIn;
</script>

<Container divClass="flex flex-wrap py-20 w-full content-center justify-center">
	{#if signal === 'edit' && address?.id}
		<AddressForm
			method="PUT"
			initial_data={address}
			buttonValue="edit address"
			redirectTo={String(redirectTo)}
		/>
	{:else}
		<AddressForm method="POST" redirectTo={String(redirectTo)} />
	{/if}
</Container>
