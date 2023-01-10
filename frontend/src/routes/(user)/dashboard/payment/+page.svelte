<script lang="ts">
	import Section from '$root/lib/components/animation/FadeInOut.svelte';
	import type { PaymentIn } from '$root/lib/interface/payment.interface';
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
	const payment_list = data.payment_list as PaymentIn[];

	$: searchTerm = '';
</script>

<Section>
	<TableSearch placeholder="Search by orderId " hoverable={true} bind:inputValue={searchTerm}>
		<TableHead>
			<TableHeadCell>ID</TableHeadCell>
			<TableHeadCell>payment ID</TableHeadCell>
			<TableHeadCell>status</TableHeadCell>
			<TableHeadCell>currency</TableHeadCell>
			<TableHeadCell>amount</TableHeadCell>
			<TableHeadCell>actions</TableHeadCell>
		</TableHead>
		<TableBody class="divide-y">
			{#each payment_list as payment, index}
				<TableBodyRow>
					<TableBodyCell>{index + 1}</TableBodyCell>
					<TableBodyCell>{payment.pay_ref}</TableBodyCell>
					<TableBodyCell>
						{#if payment.status.toLowerCase() === 'pending'}
							<Badge large color="yellow">{payment.status}</Badge>
						{:else if payment.status.toLowerCase() == 'success'}
							<Badge large color="green">{payment.status}</Badge>
						{:else if payment.status.toLowerCase() == 'fail'}
							<Badge large color="red">{payment.status}</Badge>
						{/if}
					</TableBodyCell>
					<TableBodyCell>{payment.currency}</TableBodyCell>
					<TableBodyCell>${payment.amount}</TableBodyCell>
					{#if payment.status === 'pending'}
						<TableBodyCell
							><a
								href="/dashboard/payment/verify/?tx_ref={payment.pay_ref}"
								class="font-medium text-blue-600 hover:underline dark:text-blue-500 pr-5"
								data-sveltekit-prefecth=""
							>
								Retry
							</a>
						</TableBodyCell>
					{:else}
						<TableBodyCell>completed</TableBodyCell>
					{/if}
				</TableBodyRow>
			{/each}
		</TableBody>
	</TableSearch>
</Section>
