<script lang="ts">
	import AuthorDetailsCard from '$root/lib/components/card/AuthorDetailsCard.svelte';
	import DefaultMessage from '$root/lib/components/utilities/DefaultMessage.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import Grid from '$root/lib/components/layouts/Grid.svelte';
	import NewReleaseCard from '$root/lib/components/card/NewReleaseCard.svelte';
	import ReviewCard from '$root/lib/components/card/ReviewCard.svelte';
	import SectionTitle from '$root/lib/components/utilities/SectionTitle.svelte';
	import type { PageServerData } from './$types';
	export const hydrate = false;
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
			<DefaultMessage message="No books yet" />
		{/if}
	</Container>
	<img src="/homepage design.svg" alt="design" class="absolute top-90 left-0 right-0" />
</section>

<Container divClass="pb-28 px-5">
	{#if !reviews}
		<SectionTitle title="Reviews" />
	{/if}
	<Grid>
		{#each reviews as review}
			<ReviewCard {review} />
		{/each}
	</Grid>
</Container>

<Container divClass=" pt-10 pb-28 px-5">
	{#if author !== undefined}
		<AuthorDetailsCard {author} max_lenght={300} />
	{:else}
		<DefaultMessage message="Author's details not available" />
	{/if}
</Container>
<Container divClass="pb-28 ">
	<SectionTitle title="new release" />
	<Grid gap={6}>
		{#each latest_product as product}
			<NewReleaseCard {product} />
		{:else}
			<DefaultMessage message="No new release books" />
		{/each}
	</Grid>
	<div class="flex justify-end pt-20">
		<a href="/books" class="rounded-full font-semibold bg-secondary px-5 py-3 capitalize"
			>view more</a
		>
	</div>
</Container>
