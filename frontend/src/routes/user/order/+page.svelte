<script lang="ts">
	import {
		Badge,
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		TableSearch
	} from 'flowbite-svelte';
	import DefaultMessage from '$root/lib/components/DefaultMessage.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import SectionTitle from '$root/lib/components/SectionTitle.svelte';
	import type { PageServerData } from '.svelte-kit/types/src/routes/user/order/$types';

	export let data: PageServerData;
	$: order_list = data.order_list;

	$: searchTerm = '';
</script>

<Container divClass="py-20 flex items-center justify-center">
	<div class="w-full md:w-3/5 space-y-6 ">
		<SectionTitle title="Orders" />
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
								href="/user/order/{order.orderId}"
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
	</div>
</Container>
