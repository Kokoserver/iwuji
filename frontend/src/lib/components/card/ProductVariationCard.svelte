<script lang="ts">
	import type { VariationIn } from '../interface/variation.interface';

	export let variation: VariationIn;
</script>

<div
	class="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-0 border-b border-b-secondary py-10"
>
	<div class="md:w-1/2 p-2">
		<img src={variation.cover_img.url} width="427" height="527" alt={variation.name} srcset="" />
	</div>
	<div class="md:w-2/5 space-y-4 p-3 ">
		<h1 class="font-semibold uppercase text-2xl text-center md:text-left">
			{variation.name}
		</h1>
		<p class="font-normal text-gray-700 text-center md:text-left">
			{variation.description.slice(1, 300)}...
		</p>
		<div class="pt-6 space-x-4 flex items-start md:items-center justify-center md:justify-start">
			<a
				href="/books/{variation.id}/?is_series=true"
				class="rounded-full font-semibold bg-primary px-4 py-3 text-center uppercase ">preview</a
			>

			<a href="/" class="rounded-full font-semibold bg-primary px-4 py-3 text-center uppercase "
				>view on amazon</a
			>
		</div>
	</div>
</div>
