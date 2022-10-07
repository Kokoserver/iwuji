<script lang="ts">
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
	} from 'flowbite-svelte';
	import type { PageServerData } from '.svelte-kit/types/src/routes/user/address/$types';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import { page } from '$app/stores';
	import { delete_address } from './crud';
	import { AddressStore } from './store';
	import DefaultMessage from '$root/lib/components/DefaultMessage.svelte';
	export let data: PageServerData;
	$: $AddressStore = data.addressList;
</script>

<Container divClass="my-20">
	<Table>
		<caption
			class="p-5 text-lg font-semibold text-left text-gray-900 bg-white dark:text-white dark:bg-gray-800"
		>
			<a
				href="{$page.url}/create/?redirectTo={$page.url}"
				class="py-3 px-6 bg-primary rounded-full font-normal capitalize">create new address</a
			>
		</caption>
		<TableHead>
			<TableHeadCell class="!p-4">#ID</TableHeadCell>
			<TableHeadCell>Street</TableHeadCell>
			<TableHeadCell>city</TableHeadCell>
			<TableHeadCell>state</TableHeadCell>
			<TableHeadCell>zipcode</TableHeadCell>
			<TableHeadCell>Phone No</TableHeadCell>
			<TableHeadCell>country</TableHeadCell>
			<TableHeadCell>ACTION</TableHeadCell>
		</TableHead>
		<TableBody class="divide-y">
			{#each $AddressStore as address, index}
				<TableBodyRow>
					<TableBodyCell class="!p-4">
						{index + 1}
					</TableBodyCell>
					<TableBodyCell>{address.street.slice(0, 14)}...</TableBodyCell>
					<TableBodyCell>{address.city}</TableBodyCell>
					<TableBodyCell>{address.state}</TableBodyCell>
					<TableBodyCell>{address.zipcode}</TableBodyCell>
					<TableBodyCell>{address.tel}</TableBodyCell>
					<TableBodyCell>{address.country}</TableBodyCell>

					<TableBodyCell
						><a
							href="/user/address/edit/?id={address.id}&redirectTo={$page.url}"
							class="font-medium text-blue-600 hover:underline dark:text-blue-500 pr-5"
							data-sveltekit-prefecth
						>
							Edit
						</a>
						<button
							class="font-medium text-red-600 hover:underline dark:text-red-500"
							on:click={async () => await delete_address(address.id)}
						>
							Remove
						</button></TableBodyCell
					>
				</TableBodyRow>
			{:else}
				<DefaultMessage message="No address yet" />
			{/each}
		</TableBody>
	</Table>
</Container>
