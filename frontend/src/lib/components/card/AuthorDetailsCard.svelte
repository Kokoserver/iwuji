<script lang="ts">
	import type { AuthorIn } from '$root/lib/interface/author.interface';

	export let author: AuthorIn;
	export let max_lenght: number | 'full';
</script>

<div class="flex flex-col md:flex-row items-center justify-center gap-6">
	<div class="md:w-1/2 p-2">
		<img src={author.profile_img?.url} width="500" height="500" alt={author?.profile_img?.alt} />
	</div>
	<div class="md:w-2/5 space-y-4 p-3 ">
		<h1 class="font-semibold uppercase text-2xl text-center md:text-left">The author</h1>
		<p class="font-normal text-gray-700 text-center md:text-left">
			{#if max_lenght === 'full'}
				{author.description}
			{:else if typeof max_lenght === 'number'}
				{author.description.slice(1, max_lenght)}...
				<a href="/bio" class="font-normal text-blue-300 ">Read more</a>
			{/if}
		</p>
	</div>
</div>
