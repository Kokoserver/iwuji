<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import type { PageServerData } from './$types';
	import { Iconinput, Next, Previous } from 'flowbite-svelte';
	import { bookType } from '$root/lib/store/toggleSeriesStore';

	export let data: PageServerData;
	let { products } = data;
	$bookType.is_series = false;
	$bookType.normal_book;
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
		const res = await fetch(`books/api?filter=${$bookType.filter}&is_series=${$bookType.is_series}`);
		products = await res.json();
	};
</script>

<Container divClass="mt-28 px-3 md:px-0">
	<div class="space-y-4 ">
		<Iconinput noBorder pointerEvent inputClass=" rounded-full" id="search" bind:value={$bookType.filter} placeholder="Search" class="p-4">
			<svg
				data-sveltekit-prefetch
				on:click={handleToggle}
				aria-hidden="true"
				class="w-5 h-5 text-gray-500 dark:text-gray-400 cursor-pointer"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg"
				><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg
			>
		</Iconinput>
		<div class="flex items-center justify-end space-x-5">
			<p class="capitalize">sorte by</p>
			<div class="flex rounded-full items-center">
				<span
					data-sveltekit-prefetch
					class="border border-transparent rounded-l-full font-semibold px-4 py-3 text-center capitalize  border-gray-600 cursor-pointer"
					class:active={$bookType.normal_book}
					on:click={handleToggle}
					id="normal_book"
				>
					books
				</span>
				<span
					data-sveltekit-prefetch
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
	{#each products as product}
		<div class="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-0 border-b border-b-blue-400 py-10">
			<div class="md:w-1/2 p-2">
				<img src={product.cover_img.url} width="427" height="527" alt={product.name} srcset="" />
			</div>
			<div class="md:w-2/5 space-y-4 p-3 ">
				<h1 class="font-semibold uppercase text-2xl text-center md:text-left">{product.name}</h1>
				<p class="font-normal text-gray-700 text-center md:text-left">
					{product.description.slice(1, 300)}...
				</p>
				<div class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start">
					<a href="/books/{product.id}" class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase ">preview</a>

					<a href="/" class="rounded-full font-semibold bg-yellow-200 px-4 py-3 text-center uppercase ">view on amazon</a>
				</div>
			</div>
		</div>
	{:else}
		<h1 class="text-center font-bold text-4xl">No books yet</h1>
	{/each}

	<div class="flex items-center justify-center py-20">
		<Previous on:previous={() => alert('previous is click')} icon />
		<Next on:next={() => alert('next is click')} icon />
	</div>
</Container>
