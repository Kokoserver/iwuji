<script lang="ts">
	import { Card, Table } from 'flowbite-svelte';
	import type { LayoutServerData } from './$types';
	import Section from '$root/lib/components/animation/FadeInOut.svelte';
	import {
		Badge,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell,
		TableSearch
	} from 'flowbite-svelte';
	export let data: LayoutServerData;
</script>

<div>
	<div class="grid grid-cols-1 sm:grid-cols-1 lg:grid-cols-3 p-4 gap-4  place-content-center">
		<div
			class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group"
		>
			<div
				class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12"
			>
				<svg
					width="30"
					height="30"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"
					/></svg
				>
			</div>
			<div class="text-right">
				<p class="text-2xl">
					{data.order_list.filter((order) => order.status === 'success').length}
				</p>
				<p>Completed Orders</p>
			</div>
		</div>
		<div
			class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group"
		>
			<div
				class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12"
			>
				<svg
					width="30"
					height="30"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"
				>
					<path
						stroke-linecap="round"
						stroke-linejoin="round"
						d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z"
					/>
				</svg>
			</div>
			<div class="text-right">
				<p class="text-2xl">
					{data.order_list.filter((order) => {
						if (order.status === 'cancelled') {
							return order;
						}
					}).length}
				</p>
				<p>cancelled order</p>
			</div>
		</div>
		<div
			class="bg-blue-500 dark:bg-gray-800 shadow-lg rounded-md flex items-center justify-between p-3 border-b-4 border-blue-600 dark:border-gray-600 text-white font-medium group"
		>
			<div
				class="flex justify-center items-center w-14 h-14 bg-white rounded-full transition-all duration-300 transform group-hover:rotate-12"
			>
				<svg
					width="30"
					height="30"
					fill="none"
					viewBox="0 0 24 24"
					stroke="currentColor"
					class="stroke-current text-blue-800 dark:text-gray-800 transform transition-transform duration-500 ease-in-out"
					><path
						stroke-linecap="round"
						stroke-linejoin="round"
						stroke-width="2"
						d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
					/></svg
				>
			</div>
			<div class="text-right">
				<p class="text-2xl">
					{data.order_list.filter((order) => {
						if (order.status === 'processing' || order.status === 'pending') {
							return order;
						}
					}).length}
				</p>
				<p>Ongoing Order</p>
			</div>
		</div>
	</div>
</div>
<Section>
	<Table hoverable={true}>
		<TableHead>
			<TableHeadCell>ID</TableHeadCell>
			<TableHeadCell>OrderId</TableHeadCell>
			<TableHeadCell>status</TableHeadCell>
			<TableHeadCell>actions</TableHeadCell>
		</TableHead>
		<TableBody class="divide-y">
			{#each data.order_list as order, index}
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
	</Table>
</Section>
