<script lang="ts">
	import AuthorDetailsCard from '$root/lib/components/AuthorDetailsCard.svelte';
	import DefaultMessage from '$root/lib/components/DefaultMessage.svelte';
	import Container from '$root/lib/components/layouts/Container.svelte';
	import Grid from '$root/lib/components/layouts/Grid.svelte';
	import NewReleaseCard from '$root/lib/components/NewReleaseCard.svelte';
	import SectionTitle from '$root/lib/components/SectionTitle.svelte';
	import type { PageServerData } from './$types';
	export let data: PageServerData;
	const { author, products } = data;
</script>

<Container divClass=" pt-10 pb-28 px-5">
	{#if author}
		<AuthorDetailsCard {author} max_lenght="full" />
	{:else}
		<DefaultMessage message="author data is not define" />
	{/if}
</Container>

{#if products[0]}
	<Container divClass="pb-28 ">
		<SectionTitle title="authors works" />
		<Grid gap={6}>
			{#each products as product}
				<NewReleaseCard {product} />
			{:else}
				<DefaultMessage message="No new release books" />
			{/each}
		</Grid>
	</Container>
{/if}
