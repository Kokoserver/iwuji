<script lang="ts">
	import AddressForm from '$root/lib/components/form/AddressForm.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	const { address, redirectTo, signal } = data;
</script>

<Container divClass="py-20 ">
	{#if signal === 'edit' && address}
		<AddressForm
			method="PUT"
			initial_data={address}
			buttonValue="update address"
			redirectTo={String(redirectTo)}
		/>
	{:else}
		<AddressForm method="POST" redirectTo={String(redirectTo)} />
	{/if}
</Container>
