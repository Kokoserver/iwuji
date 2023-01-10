<script lang="ts">
	import Section from '$root/lib/components/animation/FadeInOut.svelte';
	import type { PageServerData } from './$types';
	import {
		Badge,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		TableSearch
	} from 'flowbite-svelte';
	export let data: PageServerData;
	const order_list = data.order_list;
	$: searchTerm = '';
</script>

<Section>
	<TableSearch placeholder="Search by orderId " hoverable={true} bind:inputValue={searchTerm}>
		<TableHead>
			<TableHeadCell>ID</TableHeadCell>
			<TableHeadCell>OrderId</TableHeadCell>
			<TableHeadCell>status</TableHeadCell>
			<TableHeadCell>actions</TableHeadCell>
		</TableHead>
		<TableBody class="divide-y">
			{#each order_list as order, index}
				<TableBodyRow>
					<TableBodyCell>{index + 1}</TableBodyCell>
					<TableBodyCell>{order.orderId}</TableBodyCell>
					<TableBodyCell>
						{#if order.status.toLowerCase() === 'processing'}
							<Badge large color="blue">{order.status}</Badge>
						{:else if order.status.toLowerCase() === 'pending'}
							<Badge large color="yellow">{order.status}</Badge>
						{:else if order.status.toLowerCase() == 'completed'}
							<Badge large color="green">{order.status}</Badge>
						{:else if order.status.toLowerCase() == 'cancelled'}
							<Badge large color="red">{order.status}</Badge>
						{/if}
					</TableBodyCell>
					<TableBodyCell
						><a
							data-sveltekit-prefetch=""
							href="/dashboard/order/{order.orderId}"
							class="font-medium text-blue-600 hover:underline dark:text-blue-500 pr-5"
							data-sveltekit-prefecth=""
						>
							view
						</a>
					</TableBodyCell>
				</TableBodyRow>
			{/each}
		</TableBody>
	</TableSearch>
</Section>
