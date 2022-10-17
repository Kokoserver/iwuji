<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import type { PageServerData } from './$types';
	import { Iconinput } from 'flowbite-svelte';
	import { bookType } from '$root/store/toggleSeriesStore';
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';
	import DefaultMessage from '$root/lib/components/utilities/DefaultMessage.svelte';
	import ProductCard from '$root/lib/components/card/ProductCard.svelte';
	import ProductVariationCard from '$root/lib/components/card/ProductVariationCard.svelte';

	export let data: PageServerData;

	onMount(() => {
		$bookType.normal_book = true;
	});
	$: products = data.products;
	$: variations = data.variations;
	$: is_series = $bookType.is_series;
	$: mormal_book = $bookType.normal_book;

	$bookType.is_series = false;
	$bookType.normal_book;
	const fetctData = async () => {
		const res = await fetch(
			`books/api?filter=${$bookType.filter}&is_series=${$bookType.is_series}`
		);
		if ($bookType.is_series) {
			variations = await res.json();
		} else if ($bookType.normal_book) {
			products = await res.json();
		}
	};

	const handleToggle = async (e: Event) => {
		const current_target = e.target as HTMLSpanElement;
		if (current_target.id === 'normal_book') {
			$bookType.normal_book = true;
			$bookType.is_series = false;
			document.getElementById('submit')?.click();
		} else if (current_target.id === 'series_book') {
			$bookType.is_series = true;
			$bookType.normal_book = false;
			document.getElementById('submit')?.click();
		}
		await fetctData();
	};

	const fetchDataOnkeyEnter = async () => {
		if (browser) {
			window.onkeypress = (event) => {
				if (event.key === 'Enter' && $bookType.filter !== '') {
					fetctData();
				}
			};
		}
	};
	fetchDataOnkeyEnter();
</script>

<Container divClass="mt-28 px-3 md:px-0">
	<div class="space-y-4 ">
		<Iconinput
			size="lg"
			noBorderInputClass="rounded-full w-full border"
			noBorder
			pointerEvent
			id="search"
			bind:value={$bookType.filter}
			placeholder="Search"
			class="p-4"
		>
			<svg
				data-sveltekit-prefetch=""
				on:click={handleToggle}
				aria-hidden="true"
				class="w-5 h-5 text-gray-500 dark:text-gray-400 cursor-pointer"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg"
				><path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
				/></svg
			>
		</Iconinput>
		<div class="flex items-center justify-end space-x-5">
			<p class="capitalize">sorte by</p>
			<div class="flex rounded-full items-center">
				<span
					data-sveltekit-prefetch=""
					class="border border-transparent rounded-l-full font-semibold px-4 py-3 text-center capitalize  border-gray-600 cursor-pointer"
					class:active={$bookType.normal_book}
					on:click={handleToggle}
					id="normal_book"
				>
					books
				</span>
				<span
					data-sveltekit-prefetch=""
					class="font-semibold border rounded-r-full px-4 py-3 text-center capitalize  border-gray-600 cursor-pointer"
					class:active={$bookType.is_series}
					on:click={handleToggle}
					id="series_book"
				>
					series
				</span>
			</div>
		</div>
	</div>
</Container>
<Container divClass="pt-10 pb-28 px-5 space-y-7">
	{#if is_series && variations}
		{#each variations as variation}
			<ProductVariationCard {variation} />
		{:else}
			<DefaultMessage message="No series books yet" />
		{/each}
	{/if}
	{#if mormal_book && products}
		{#each products as product}
			<ProductCard {product} />
		{:else}
			<DefaultMessage message="No books yet" />
		{/each}
	{/if}
</Container>
