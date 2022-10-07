<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import Grid from '$root/lib/components/layouts/Grid.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	const { author, products } = data;
</script>

<Container divClass=" pt-10 pb-28 px-5">
	{#if author}
		<div class="flex flex-col md:flex-row items-center justify-center gap-6">
			<div class="md:w-1/2 p-2">
				<img src={author?.profile_img?.url} width="500" height="500" alt="" />
			</div>
			<div
				class="md:w-2/5 space-y-4 p-3  h-[35rem] {author.description.length > 1500 &&
					`overflow-y-scroll`}"
			>
				<p class="font-normal text-gray-700 text-center md:text-left">
					{author.description}
				</p>
			</div>
		</div>
	{:else}
		<h1 class="text-4xl font-bold text-center">author data is not define</h1>
	{/if}
</Container>

{#if products[0]}
	<Container divClass="pb-28 ">
		<h3 class="font-bold text-3xl uppercase text-center pb-20">authors works</h3>
		<Grid gap={6}>
			{#each products as product}
				<div class="flex flex-col items-center space-y-7">
					<a href="/books/{product.id}"
						><img
							src={product.cover_img.url}
							alt={product.cover_img.alt}
							srcset=""
							class="w-65 h-60"
						/></a
					>
					<h1 class="font-normal text-xl uppercase">{product.name}</h1>
				</div>
			{:else}
				<h1 class="text-4xl text-center font-semibold">No new release books</h1>
			{/each}
		</Grid>
	</Container>
{/if}
