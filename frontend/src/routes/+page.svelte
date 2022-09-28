<script lang="ts">
	import Container from '$root/lib/components/layouts/Container.svelte';
	import Grid from '$root/lib/components/layouts/Grid.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	const { products, reviews, author } = data;
	$: latest_product = products.slice(1, products.length);
</script>

<section class="relative pb-28">
	<Container divClass="pt-10  px-5">
		{#if products.length > 0}
			<div class="flex flex-col md:flex-row items-center justify-center gap-6">
				<div class="md:w-1/2 p-2">
					<img src={products[0].cover_img.url} width="527" height="627" alt="" srcset="" />
				</div>
				<div class="md:w-2/5 space-y-4 p-3 ">
					<h1 class="font-semibold uppercase text-2xl text-center md:text-left">
						{products[0].name}
					</h1>
					<p class="font-normal text-gray-700 text-center md:text-left text-clip">
						{products[0].description.slice(1, 200)}...
					</p>
					<div
						class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start"
					>
						<a
							href="/books/{products[0].id}"
							class="rounded-full font-semibold bg-secondary px-4 py-3 text-center uppercase "
							>buy now</a
						>
						<a
							href="/books"
							class="rounded-full font-semibold border border-gray-700 px-4 py-3 text-center uppercase"
							>see more books</a
						>
					</div>
				</div>
			</div>
		{:else}
			<h1 class="text-4xl text-center font-semibold">No books yet</h1>
		{/if}
	</Container>
	<img src="/homepage design.svg" alt="" class="absolute top-90 left-0 right-0" />
</section>

<Container divClass="pb-28 px-5">
	{#if !reviews}
		<h3 class="font-bold text-3xl uppercase text-center pb-7">Reviews</h3>
	{/if}
	<Grid>
		{#each reviews as review, index}
			<div class="flex  justify-between  gap-4" id={`${review.id}`}>
				<div class="w-1/3">
					<img src="/books.jpg" alt="" srcset="" class="rounded-full w-24 h-24" />
				</div>
				<div class="w-2/3">
					<h1 class="capitalize font-semibold text-md text-gray-500">
						{review.user.firstname}
						{review.user.lastname}
					</h1>
					<p>{review.comment}</p>
				</div>
			</div>
		{/each}
	</Grid>
</Container>

<Container divClass=" pt-10 pb-28 px-5">
	{#if author.email}
		<div class="flex flex-col md:flex-row items-center justify-center gap-6">
			<div class="md:w-1/2 p-2">
				<img
					src={author?.profile_img?.url}
					width="500"
					height="500"
					alt={author?.profile_img?.alt}
				/>
			</div>
			<div class="md:w-2/5 space-y-4 p-3 ">
				<h1 class="font-semibold uppercase text-2xl text-center md:text-left">The author</h1>
				<p class="font-normal text-gray-700 text-center md:text-left">
					{author.description.slice(1, 400)}...
					<a href="/bio" class="font-normal text-blue-300 ">Read more</a>
				</p>
			</div>
		</div>
	{:else}
		<h1 class="text-4xl text-center font-semibold">Author's details not available</h1>
	{/if}
</Container>
<Container divClass="pb-28 ">
	<h3 class="font-bold text-3xl uppercase text-center pb-20">new release</h3>
	<Grid gap={6}>
		{#each latest_product as product}
			<div class="flex flex-col items-center space-y-7">
				<a href="/books/{product.id}">
					<img src={product.cover_img.url} alt={product.cover_img.alt} class="w-65 h-60" />
				</a>
				<h1 class="font-normal text-xl uppercase">{product.name}</h1>
			</div>
		{:else}
			<h1 class="text-4xl text-center font-semibold">No new release books</h1>
		{/each}
	</Grid>
	<div class="flex justify-end pt-20">
		<a href="/books" class="rounded-full font-semibold bg-secondary px-5 py-3 capitalize"
			>view more</a
		>
	</div>
</Container>
